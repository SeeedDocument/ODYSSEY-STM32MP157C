// demo: CAN-BUS Shield, send data
// loovee@seeed.cc

#include <mcp_can.h>
#include <SPI.h>
#include "Seeed_SHT35.h"

/*SAMD core*/
#ifdef ARDUINO_SAMD_VARIANT_COMPLIANCE
  #define SERIAL SerialUSB
#else
  #define SERIAL Serial
#endif

// the cs pin of the version after v1.1 is default to D9
// v0.9b and v1.0 is default D10
const int SPI_CS_PIN = 9;
/*SAMD core*/
#ifdef ARDUINO_SAMD_VARIANT_COMPLIANCE
  #define SDAPIN  20
  #define SCLPIN  21
  #define RSTPIN  7
#else
  #define SDAPIN  A4
  #define SCLPIN  A5
  #define RSTPIN  2
#endif

MCP_CAN CAN(SPI_CS_PIN);                                    // Set CS pin
SHT35 sensor(SCLPIN);

void setup()
{
    SERIAL.begin(115200);

    while (CAN_OK != CAN.begin(CAN_500KBPS))              // init can bus : baudrate = 500k
    {
        SERIAL.println("CAN BUS Shield init fail");
        SERIAL.println(" Init CAN BUS Shield again");
        delay(100);
    }
    SERIAL.println("CAN BUS Shield init ok!");
    
    if(sensor.init())
    {
      SERIAL.println("sensor init failed!!!");
    }
    
}

unsigned char stmp[8] = {0, 0, 0, 0, 0, 0, 0, 0};
void loop()
{
   
    float temp,hum;
    int light = analogRead(A0);
    light = light/(1024.0) * 100.0;
    if(NO_ERROR!=sensor.read_meas_data_single_shot(HIGH_REP_WITH_STRCH,&temp,&hum))
    {
      SERIAL.println("read temp failed!!");
      SERIAL.println("   ");
      SERIAL.println("   ");
      SERIAL.println("   ");
    }
    else
    {
      // send data:  id = 0x00, standrad frame, data len = 8, stmp: data buf
      
      stmp[7] = (u8)temp;
      stmp[6] = 0;
      stmp[5] = (u8)hum;
      stmp[4] = 0;
      stmp[3] = (u8)light;
      stmp[2] = 0;    
      stmp[1] = random(30);
      stmp[0] = 0;    
      CAN.sendMsgBuf(0x00, 0, 8, stmp);
      
      SERIAL.println("read data :");
      SERIAL.print("temperature = ");
      SERIAL.print(temp);
      SERIAL.println(" ℃ ");

      SERIAL.print("humidity = ");
      SERIAL.print(hum);
      SERIAL.println(" % ");
      
      SERIAL.print("light = ");
      SERIAL.print(light);
      SERIAL.println(" % ");
      
      SERIAL.println("   ");
      SERIAL.println("   ");
      SERIAL.println("   ");
    }
    
    delay(100);                       // send data per 100ms
}

// END FILE