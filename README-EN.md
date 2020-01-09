---
name: Seeed NPi-STM32MP157C
category: Seeed NPi-STM32MP157C
bzurl: https://www.seeedstudio.com/SeeedStudio-BeagleBone-Green-Wireless-p-2650.html
oldwikiname: SeeedStudio_BeagleBone_Green_Wireless
prodimagename: BBGW_cover.png
wikiurl: http://wiki.seeedstudio.com/cn/BeagleBone_Green_Wireless
sku: 102010048
---

# Seeed NPi-STM32MP157C

![]()

Seeed NPi-STM32MP157C is an open source hardware development board based on the STM32MP157C microcontroller by Seeed Studio. Seeed NPi-STM32MP157C not only provides all of the system's source code for users to learn how to turn it into an arm development board, but it's similar in size to a Raspberry Pi. Although the house sparrow is small, but be fullies equipped. It includes a high performance flexible WiFi/bluetooth interface and two Grove connectors,  which make it easier to connect to the various grove sensor family. It supports the MIPI DSI interface and CAN FD interface, also compatible with Raspberry Pi's 40-pin interface.

 [![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.1e729b66GJVV3r&id=533937368398)

## Features

- 16-bit 512M RAM & 4GB eMMC
- USB OTG: can be attached to USB devices
- 2.4G WiFi & BT 4.2 （External antenna is available）
- Grove interface (one IIC and one Digital)
- 3.5mm Audio jack
- Debian-based Linux system
- 40-PIN GPIO compatible with Raspberry Pi
- Support for gigabit Ethernet
- Support for MIPI DSI display
- Support DVP camera
- Support audio playback
- Additional power supply through DC interface (12V/2A power input is recommended)

## Specification

|Item|Values|
|----|------|
|CPU | STM32MP157C<br>(Arm® Cortex®-A7 and Cortex®-M4 Dual architecture processor) |
|Memory | 512M DDR3 |
|On-board flash memory | 4GB eMMC |
|CPU support | 3D graphics accelerator, CAN FD agreement, MIPI DSI display |
|USB support | Power supply and communication |
|USB | USB2.0 host	x2 |
|Grove interface | Two (IIC and Digital) |
|GPIO | 40-PIN |
|Ethernet | Gigabit |
|Operating temperature | 0 ~ 75 ℃ |

## Application

- The Internet of things
- The home of wisdom
- Automation and process control
- The man-machine interface
- Sensor center
- Robot

## Hardware Overview

Seeed NPi-STM32MP157C consists of two parts: Seeed NPi - STM32MP157C and Seeed SoM - STM32MP157C.

Seeed NPi-STM32MP157C hardware details follow:

 ![](https://github.com/SeeedDocument/Seeed-NPi-STM32MP157C/raw/master/IMG/front.png)

 ![](https://github.com/SeeedDocument/Seeed-NPi-STM32MP157C/raw/master/IMG/back.png)

- **1.Seeed Som-stm32mp157c Slot :** Install the Seeed som-stm32mp157c area, if the user wants to remove the core board, slowly tilt the core board up and then remove, never remove by hand.

- **2.DC Power Input Port :** 12V~24V/2A (12V/2A power input is recommended).

- **3.ETH Interface :** Network cable interface can be connected to gigabit level network.

- **4.USB Host:** Two USB Host ports.

- **5.USB Device:** USB 2.0 Type C. If Type C is used as board power input, a 5V/3A power adapter should be used.

- **6.Digital Grove Interface:** Connect the Grove interface to the digital pin. 

- **7.IIC Grove Interface:** Connect the Grove interface to the IIC pin.

- **8.American Standard 3.5mm:**  Audio interface.

- **9.MIPI DSI Interface:** Connect to a display with a MIPI DSI interface(FPC 20Pin 1.0mm).

- **10.40 PIN GPIO Interface:** Compatible with Raspberry Pi's 40-PIN.

- **11.AP6236:** 2.4G WiFi & BT 4.2 control chip.

- **12.Slide Switch:** Can be used to select SD card or eMMC to start.

- **13.Debug UART:** The system default debugging serial port can enter this serial port to access the system, we'll talk more about how to do that later.

- **14.JST 1.0mm:** 3VRTC battery interface.

- **15.RST Key:** system reset key.

- **16.PWR Button:** Long press about 8S to shut down, short press to boot.

- **17.User Button:** User programmable buttons.

- **18.PWR LED:** Development board power led.

- **19.User LED:** User programmable led.

- **20.ACA-5036-A2-CC-S:** Onboard 2.4G ceramic antenna.

- **21.The IPEX 1 generation:** External 2.4 G external antenna seat(When using an external antenna, need remove R49, R51 0Ω welding)

- **22.SD card slot:** Is the area where a micro-sd card with the system is inserted.

- **23.DVP camera interface :** Connect to camera with DVP interface (FPC 20Pin 1.0mm).

- **24.KSZ9031:** 1000M Network cable drive network card.

- **25.STMPS2252MTR:** Power switch chip.

- **26.MP9943:** Buck DCDC Power chip.

- **27.WM8960:** Audio codec chip.

- **28.MP2161:** Buck DCDC Power chip.

The following is a detailed description of Seeed SoM - STM32MP157C's hardware.

![](https://github.com/SeeedDocument/Seeed-NPi-STM32MP157C/raw/master/IMG/SOM-overview.png)

- **1.STM32MP157C:** Main control chip of development board(Arm® Cortex®-A7 and Cortex®-M4 dual-architecture processors).

- **2.MT41K256M16TW-107:P:** 512M 16bit RAM memory chip.

- **3.STPMIC1APQR:** Power management chip.

- **4.EMMC04G-M627:** 4GeMMC memory.

- **5.LED:** When the power supply is successful, the PWR will be turned on, and when the system is running normally, the USER will flicker indefinitely.

- **6.70-PIN Interface:** You can find the function for each pin from the table below

|Pin package number|Pin number|Pin name|Pin type|Optional function|additional function|
|:------:|:------:|:------:|:------:|:------:|:------:|
|-|1|5V_VIN|S|-|-|
|-|2|3V3|S|-|-|
|-|3|5V_VIN|S|-|-|
|-|4|3V3|S|-|-|
|-|5|5V_VIN|S|-|-|
|-|6|3V3|S|-|-|
|-|7|5V_VIN|S|-|-|
|-|8|3V3|S|-|-|
|-|9|5V_VIN|S|-|-|
|-|10|3V3|S|-|-|
|-|11|5V_VIN|S|-|-|
|-|12|VDD|S|-|-|
|-|13|5V_VIN|S|-|-|
|-|14|VDD|S|-|-|
|-|15|5V_VIN|S|-|-|
|-|16|VBUS_OTG|S|-|-|
|-|17|BST_OUT|S|-|-|
|-|18|VBUS_OTG|S|-|-|
|-|19|BST_OUT|S|-|-|
|-|20|VBUS_SW|S|-|-|
|-|21|BST_OUT|S|-|-|
|-|22|VBUS_SW|S|-|-|
|-|23|1V8_AUDIO|S|-|-|
|-|24|VBUS_SW|S|-|-|
|-|25|1V2_HDMI|S|-|-|
|-|26|VBAT|S|-|-|
|-|27|3V3_HDMI|S|-|-|
|-|28|VBAT|S|-|-|
|-|29|-|-|-|-|
|-|30|-|-|-|-|
|R4|31|VREF+|S|-|-|
|AC4|32|PF14|I/O|TRACED6, DFSDM1_CKIN6,I2C4_SCL, I2C1_SCL,ETH1_GMII_RXD6, FMC_A8,EVENTOUT|ADC2_INP6,ADC2_INN2|
|Y5|33|PF13|I/O|TRACED5, DFSDM1_DATIN6,I2C4_SMBA, I2C1_SMBA,DFSDM1_DATIN3,ETH1_GMII_RXD5, FMC_A7,EVENTOUT|ADC2_INP2|
|Y4|34|PF15|I/O|TRACED7, I2C4_SDA,I2C1_SDA, ETH1_GMII_RXD7,FMC_A9, EVENTOUT|-|
|-|35|GND|S|-|-|
|L3|36|PD14|I/O|TIM4_CH3, SAI3_MCLK_B,UART8_CTS,FMC_AD0/FMC_D0,EVENTOUT|-|
|U3|37|ANA0|A|-|ADC1_INP0,ADC1_INN1,ADC2_INP0,ADC2_INN1|
|J2|38|PD15|I/O|TIM4_CH4, SAI3_MCLK_A,UART8_CTS,FMC_AD1/FMC_D1,LCD_R1,EVENTOUT|-|
|U4|39|ANA1|A|-|ADC1_INP1,ADC2_INP1|
|R2|40|PWR_ON|O|-|PWR_ONLP|
|-|41|-|-|-|-|
|-|42|GND|S|-|-|
|-|43|-|-|-|-|
|-|44|PA14|I/O|DBTRGO, DBTRGI, MCO2, EVENTOUT|-|
|-|45|PONKEYN|I|-|-|
|-|46|-|-|-|-|
|-|47|-|-|-|-|
|-|48|-|-|-|-|
|-|49|-|-|-|-|
|-|50|-|-|-|-|
|-|51|-|-|-|-|
|-|52|-|-|-|-|
|-|53|-|-|-|-|
|-|54|-|-|-|-|
|-|55|-|-|-|-|
|-|56|-|-|-|-|
|-|57|-|-|-|-|
|-|58|-|-|-|-|
|-|59|-|-|-|-|
|-|60|-|-|-|-|
|-|61|-|-|-|-|
|-|62|-|-|-|-|
|-|63|-|-|-|-|
|-|64|-|-|-|-|
|-|65|-|-|-|-|
|-|66|-|-|-|-|
|-|67|-|-|-|-|
|-|68|-|-|-|-|
|-|69|-|-|-|-|
|-|70|-|-|-|-|

- **7.70-PIN Interface:** You can find the function for each pin from the table below

|Pin package number|Pin number|Pin name|Pin type|Optional function|additional function|
|:------:|:------:|:------:|:------:|:------:|:------:|
|-|1|5V_VIN|S|-|-|
|-|2|3V3|S|-|-|
|-|3|5V_VIN|S|-|-|
|-|4|3V3|S|-|-|
|-|5|5V_VIN|S|-|-|
|-|6|3V3|S|-|-|
|-|7|5V_VIN|S|-|-|
|-|8|3V3|S|-|-|
|-|9|5V_VIN|S|-|-|
|-|10|3V3|S|-|-|
|-|11|5V_VIN|S|-|-|
|-|12|VDD|S|-|-|
|-|13|5V_VIN|S|-|-|
|-|14|VDD|S|-|-|
|-|15|5V_VIN|S|-|-|
|-|16|VBUS_OTG|S|-|-|
|-|17|BST_OUT|S|-|-|
|-|18|VBUS_OTG|S|-|-|
|-|19|BST_OUT|S|-|-|
|-|20|VBUS_SW|S|-|-|
|-|21|BST_OUT|S|-|-|
|-|22|VBUS_SW|S|-|-|
|-|23|1V8_AUDIO|S|-|-|
|-|24|VBUS_SW|S|-|-|
|-|25|1V2_HDMI|S|-|-|
|-|26|VBAT|S|-|-|
|-|27|3V3_HDMI|S|-|-|
|-|28|VBAT|S|-|-|
|-|29|-|-|-|-|
|-|30|-|-|-|-|
|R4|31|VREF+|S|-|-|
|AC4|32|PF14|I/O|TRACED6, DFSDM1_CKIN6,I2C4_SCL, I2C1_SCL,ETH1_GMII_RXD6, FMC_A8,EVENTOUT|ADC2_INP6,ADC2_INN2|
|Y5|33|PF13|I/O|TRACED5, DFSDM1_DATIN6,I2C4_SMBA, I2C1_SMBA,DFSDM1_DATIN3,ETH1_GMII_RXD5, FMC_A7,EVENTOUT|ADC2_INP2|
|Y4|34|PF15|I/O|TRACED7, I2C4_SDA,I2C1_SDA, ETH1_GMII_RXD7,FMC_A9, EVENTOUT|-|
|-|35|GND|S|-|-|
|L3|36|PD14|I/O|TIM4_CH3, SAI3_MCLK_B,UART8_CTS,FMC_AD0/FMC_D0,EVENTOUT|-|
|U3|37|ANA0|A|-|ADC1_INP0,ADC1_INN1,ADC2_INP0,ADC2_INN1|
|J2|38|PD15|I/O|TIM4_CH4, SAI3_MCLK_A,UART8_CTS,FMC_AD1/FMC_D1,LCD_R1,EVENTOUT|-|
|U4|39|ANA1|A|-|ADC1_INP1,ADC2_INP1|
|R2|40|PWR_ON|O|-|PWR_ONLP|
|-|41|-|-|-|-|
|-|42|GND|S|-|-|
|-|43|-|-|-|-|
|-|44|PA14|I/O|DBTRGO, DBTRGI, MCO2, EVENTOUT|-|
|-|45|PONKEYN|I|-|-|
|-|46|-|-|-|-|
|-|47|-|-|-|-|
|-|48|-|-|-|-|
|-|49|-|-|-|-|
|-|50|-|-|-|-|
|-|51|-|-|-|-|
|-|52|-|-|-|-|
|-|53|-|-|-|-|
|-|54|-|-|-|-|
|-|55|-|-|-|-|
|-|56|-|-|-|-|
|-|57|-|-|-|-|
|-|58|-|-|-|-|
|-|59|-|-|-|-|
|-|60|-|-|-|-|
|-|61|-|-|-|-|
|-|62|-|-|-|-|
|-|63|-|-|-|-|
|-|64|-|-|-|-|
|-|65|-|-|-|-|
|-|66|-|-|-|-|
|-|67|-|-|-|-|
|-|68|-|-|-|-|
|-|69|-|-|-|-|
|-|70|-|-|-|-|

- **8.70-PIN Interface:** You can find the function for each pin from the table below

|Pin package number|Pin number|Pin name|Pin type|Optional function|additional function|
|:------:|:------:|:------:|:------:|:------:|:------:|
|-|1|5V_VIN|S|-|-|
|-|2|3V3|S|-|-|
|-|3|5V_VIN|S|-|-|
|-|4|3V3|S|-|-|
|-|5|5V_VIN|S|-|-|
|-|6|3V3|S|-|-|
|-|7|5V_VIN|S|-|-|
|-|8|3V3|S|-|-|
|-|9|5V_VIN|S|-|-|
|-|10|3V3|S|-|-|
|-|11|5V_VIN|S|-|-|
|-|12|VDD|S|-|-|
|-|13|5V_VIN|S|-|-|
|-|14|VDD|S|-|-|
|-|15|5V_VIN|S|-|-|
|-|16|VBUS_OTG|S|-|-|
|-|17|BST_OUT|S|-|-|
|-|18|VBUS_OTG|S|-|-|
|-|19|BST_OUT|S|-|-|
|-|20|VBUS_SW|S|-|-|
|-|21|BST_OUT|S|-|-|
|-|22|VBUS_SW|S|-|-|
|-|23|1V8_AUDIO|S|-|-|
|-|24|VBUS_SW|S|-|-|
|-|25|1V2_HDMI|S|-|-|
|-|26|VBAT|S|-|-|
|-|27|3V3_HDMI|S|-|-|
|-|28|VBAT|S|-|-|
|-|29|-|-|-|-|
|-|30|-|-|-|-|
|R4|31|VREF+|S|-|-|
|AC4|32|PF14|I/O|TRACED6, DFSDM1_CKIN6,I2C4_SCL, I2C1_SCL,ETH1_GMII_RXD6, FMC_A8,EVENTOUT|ADC2_INP6,ADC2_INN2|
|Y5|33|PF13|I/O|TRACED5, DFSDM1_DATIN6,I2C4_SMBA, I2C1_SMBA,DFSDM1_DATIN3,ETH1_GMII_RXD5, FMC_A7,EVENTOUT|ADC2_INP2|
|Y4|34|PF15|I/O|TRACED7, I2C4_SDA,I2C1_SDA, ETH1_GMII_RXD7,FMC_A9, EVENTOUT|-|
|-|35|GND|S|-|-|
|L3|36|PD14|I/O|TIM4_CH3, SAI3_MCLK_B,UART8_CTS,FMC_AD0/FMC_D0,EVENTOUT|-|
|U3|37|ANA0|A|-|ADC1_INP0,ADC1_INN1,ADC2_INP0,ADC2_INN1|
|J2|38|PD15|I/O|TIM4_CH4, SAI3_MCLK_A,UART8_CTS,FMC_AD1/FMC_D1,LCD_R1,EVENTOUT|-|
|U4|39|ANA1|A|-|ADC1_INP1,ADC2_INP1|
|R2|40|PWR_ON|O|-|PWR_ONLP|
|-|41|-|-|-|-|
|-|42|GND|S|-|-|
|-|43|-|-|-|-|
|-|44|PA14|I/O|DBTRGO, DBTRGI, MCO2, EVENTOUT|-|
|-|45|PONKEYN|I|-|-|
|-|46|-|-|-|-|
|-|47|-|-|-|-|
|-|48|-|-|-|-|
|-|49|-|-|-|-|
|-|50|-|-|-|-|
|-|51|-|-|-|-|
|-|52|-|-|-|-|
|-|53|-|-|-|-|
|-|54|-|-|-|-|
|-|55|-|-|-|-|
|-|56|-|-|-|-|
|-|57|-|-|-|-|
|-|58|-|-|-|-|
|-|59|-|-|-|-|
|-|60|-|-|-|-|
|-|61|-|-|-|-|
|-|62|-|-|-|-|
|-|63|-|-|-|-|
|-|64|-|-|-|-|
|-|65|-|-|-|-|
|-|66|-|-|-|-|
|-|67|-|-|-|-|
|-|68|-|-|-|-|
|-|69|-|-|-|-|
|-|70|-|-|-|-|


### Pin Function

![](https://github.com/SeeedDocument/Seeed-NPi-STM32MP157C/raw/master/IMG/GPIO.png)

Seeed NPi-STM32MP157C's 40-pin is fully compatible with Raspberry Pi's 40PIN, including GPIO, IIC, UART, SPI, IIS and PWM pins, as described below.

#### GPIO

GPIO, Short for general type input and output, functions are similar to p0-p3 of 8051, it's connecting pin can be used freely by the user by program control, The PIN can be used as a general input (GPI) or general output (GPO) or general input and output (GPIO) based on practical considerations. For example, it can be used as CLK generator, chip select etc. Refer to the figure above for specific locations.

!!!Note
    - In GPIO mode, each digital I/O can generate an interrupt.

#### UART

A universal asynchronous transceiver, often referred to as a UART, the data it will transmit will be converted between serial communication and parallel communication. As a chip that converts a parallel input signal into a serial output signal, UART is usually integrated into the connection of other communication interfaces. Refer to the figure above for specific locations.

!!!Note
    - There is a dedicated connector for connecting to the UART0 pin and for connection debugging.There is also a serial extended connection port.

#### I2C

I2C is short for IICBus, so the Chinese should be called integrated circuit bus, it is a serial communication bus, using a multi-master-slave structure. Refer to the figure above for specific locations.

!!!Note
    - The first I2C bus is used to read the EEPROMS on the Cape add-on board and cannot be used for other digital I/O port operations without affecting this functionality, but you can still use it to add other I2C devices to the available addresses. The second I2C bus is available for you to configure and use.

#### SPI

SPI stands for serial peripheral interface, a high-speed, full-duplex, synchronous communication bus, only four wires are used in the pin of the chip, which saves the pin of the chip, it also saves space for PCB layout. Because it's easy to use, more and more chips are integrated with the SPI communication protocol. Refer to the figure above for specific locations.

!!!Note
    - To move data out quickly, you might consider using one of the SPI ports.

#### I2S

I2S bus is a pci bus developed by philips for audio data transmission between digital audio devices, the bus is dedicated to data transfer between audio devices, widely used in a variety of multimedia systems. Refer to the figure above for specific locations.


## Introduction To Software

### Preparatory work


**Materials required**

- Seeed NPi-STM32MP157C
- Wi-Fi network
- 4GB (or more memory) SD card and SD card reader
- PC or Mac
- [USB To Uart Adapter](https://www.seeedstudio.com/USB-To-Uart-5V%26amp%3B3V3-p-1832.html) (optional)
- 12V/2A DC interface adapter for power supply (optional)
- A USB type-c cable

<div class="admonition warning">
<p class="admonition-title">notice</p>
Please insert the USB cable gently, otherwise the interface may be damaged. Please use the USB cable with 4 internal cables, and the USB cable with 2 cables cannot transfer data. If you are not sure, you can click <a href="https://www.seeedstudio.com/Micro-USB-Cable-48cm-p-1475.html"><B>HERE</B></a> to buy.
</div>


**Mirror Installation**

Like Raspberry Pi, you need to install the Seeed NPi-STM32MP157C image from your SD card to get it up and running. We offer two ways to start Seeed NPi-STM32MP157C. You can boot from an SD card or from eMMC.

**A. Boot from SD card**

Click here to download [Firmware](https://github.com/Seeed-Studio/seeed-linux-images), go to the `STM32MP1` folder and select the firmware you want to download.


- **Step 1.** Go to the `STM32MP1` folder and select the firmware you want to download:

- **Step 2.** Connect an SD card to a PC or MAC with an SD card reader, an SD card with more than 4G memory is required.

- **Step 3.** <font face="">Click here to download <a href="https://etcher.io/">Etcher</a>, then use the Etcher to write the  ```*.img.xz``` file directly to the SD card. Or extract the ```*.img.xz``` file into a ```*.img``` file, and then burn it to an SD card using another mirror write tool. 
<br>
<br>Click the plus icon to add the newly downloaded image file and the software will automatically select the SD card you inserted. Then click Flash! writing. It takes about 10 minutes to finish.</font>

![](https://github.com/SeeedDocument/Respeaker_V2/raw/master/img/v2-flash-sd.png)


- **Step 4.** After writing the image to the SD card, insert the SD card into Seeed NPi-STM32MP157C. Use USB type-c port to power the motherboard. Do not take out the SD card during writing. Seeed NPi-STM32MP157C will boot from the SD card, you can see the PWR and USER LED lighting. Now, go to the next section: the serial console.

**B. Boot from eMMC card**

Click here to download [firmware](https://github.com/Seeed-Studio/seeed-linux-images) and go to the `STM32MP1` folder to select the firmware you want to download.

- **Step 1.** Go to`STM32MP1` folder to select the firmware you want to download.

- **Step 2.** Connect an SD card to a PC or MAC with an SD card reader, an SD card with more than 4G memory is required.

- **Step 3.** <font face="">Click here to download <a href="https://etcher.io/">Etcher</a>, then use the Etcher to write the  ```*.img.xz``` file directly to the SD card. Or extract the ```*.img.xz``` file into a ```*.img``` file, and then burn it to an SD card using another mirror write tool. 
<br>
<br>Click the plus icon to add the newly downloaded image file, and the software will automatically select the SD card you inserted. Then click Flash! Start writing. Takes about 10 minutes to complete.</font>

![](https://github.com/SeeedDocument/Respeaker_V2/raw/master/img/v2-flash-sd.png)

- **Step 4.** After writing the image to the SD card, insert the SD card into Seeed NPi STM32MP157C. use USB type-c port to power the motherboard, do not take out the SD card during writing. Seeed NPi STM32MP157C will start from the SD card, and you can see the PWR and USER LED light up.

- **Step 5.** Set the slide switch to eMMC and restart.

**Serial console**

Now that your Seeed NPi-STM32MP157C is up, you may want to access your Linux system through the console, then set up WiFi, and so on. Two serial port access methods are provided for Linux access: 

- A. OTG USB port - You need to run a Linux system on a circuit board.

- B. UART port - Used to debug low-level problems.

**A. Connect via OTG**

- **Step 1.** Take a USB type-c cable and make sure it's a data cable, plug it into Seeed NPi-STM32MP157C's USB type-c port, and then plug the other end of the USB type-c cable into your computer. 

- **Step 2.** Check whether the computer serial port is enabled:

    - Windows : Check the device manager, there should be a new serial device named ```COMx```, x is a bigger and bigger number. If you are using Windows XP/7/8, you may need to install [windows CDC driver](https://github.com/respeaker/get_started_with_respeaker/blob/master/files/ReSpeaker_Gadget_CDC_driver.7z).
    - Linux : ls ```/dev/ttyACM*```, should be ```/dev/ttyACMx``` x depends on the USB port you use.
    - Mac : ls ```/dev/cu.usb*```, should be ```/dev/cu.usbmodem14xx``` xx depends on the USB port you use.


- **Step 3.** Use your favorite serial debugging tool to connect to serial ports: 115200 baud rate, 8 bits, no parity bits, a stop bit 1, no flow control. Here are some examples:

    - Windows : Use [PUTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html), select ```Serial``` protocol, fill in the COM port corresponding to Seeed NPi-STM32MP157C,```115200``` baud rate, 8 bit, no parity bits, a stop bit 1, no flow control.
    - Linux : Depending on the USB To TTL Adapter, should be ```screen /dev/ttyACM0(,1, and so on) 115200``` or ```screen /dev/ttyUSB0(,1, and so on) 115200```.
    - Mac : Depending on the USB To TTL Adapter, should be ```screen /dev/cu.usbserial1412(,1422, and so on) 115200``` or ```screen /dev/cu.usbmodem1412(,1422, and so on) 115200```.


- **Step 4.** The default user name is ```debian```, the password is ```temppwd```.

**B. Connect via UART port**

In this section, we'll walk you through the use of the USB to TTL adapter, which connects to the Seeed NPi-STM32MP157C's Uart port(Located at the upper right of Seeed NPi-STM32MP157C), to establish a connection between your computer and Seeed NPi-STM32MP157C.

- **Step 1.** Connect Uart port To PC/Mac using USB To TTL Adapter. Note: The voltage of RX/TX is 3.3v. If you don't have USB To TTL Adapter, click [HERE](https://item.taobao.com/item.htm?id=550981934087) to buy.（RX->TX,TX->RX）

- **Step 2.** Using the following serial debugging tools, the baud rate is 115200:
    - Windows : Use [PUTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html), 选择 ```Serial``` protocol, fill in the COM port corresponding to Seeed NPi-STM32MP157C,```115200``` baud rate, 8 bit, no parity bits, a stop bit 1, no flow control.
    - Linux : Depending on the USB To TTL Adapter, should be ```screen /dev/ttyACM0(,1, and so on) 115200``` or ```screen /dev/ttyUSB0(,1, and so on) 115200```.
    - Mac : Depending on the USB To TTL Adapter, should be ```screen /dev/cu.usbserial1412(,1422, and so on) 115200``` or ```screen /dev/cu.usbmodem1412(,1422, and so on) 115200```.

- **Step 3.** The default user name is ```debian```, the password is ```temppwd```

- **Step 4.** If you don't have USB to TTL Adapter, you can also use Arduino. If you use Arduino, connect one end of the jumper to the Arduino's RESET pin and the other end to the Arduino's GND pin. This will bypass your Arduino's ATMEGA MCU and turn your Arduino into a USB to TTL adapter. Please refer [HERE](https://www.youtube.com/watch?v=qqSLwK1DP8Q) Video tutorial. Now connect the GND pin of Arduino to the GND pin of Seeed NPi-STM32MP157C's Uart port. Connect Rx pins on Arduino to Rx pins on Seeed NPi-STM32MP157C's Uart port. Connect the Tx pin on the Arduino to the Tx pin on the Seeed NPi-STM32MP157C Uart port. Finally, connect the Arduino to the PC/Mac via the Arduino's USB cable. Now check to see if your PC/Mac has found your Arduino by typing the following command:

```
ls /dev/cu.usb* (Mac)
ls /dev/ttyACM* (Linux)
```
You should get feedback like this:

```
/dev/cu.usbmodem14XX where XX will vary depending on which USB port you used (on Mac)
/dev/ttyACMX where X will vary depending on which USB port you used  (on Linux)
```
Now follow the steps above to connect to Seeed NPi-STM32MP157C via a serial connection. This is usually what we need to do when we first boot up, as you will then set up Seeed NPi-STM32MP157C for Wi-Fi connection and then SSH or VNC connection.

**Network Settings**

**A. Wi-Fi Settings**

Configure the Seeed NPi-STM32MP157C network through the network management tool `connmanctl`, which has been installed on the Seeed NPi-STM32MP157C image. Follow these instructions to easily complete the configuration. 

```
robot@ev3dev:~$ sudo connmanctl
Error getting VPN connections: The name net.connman.vpn was not provided by any
connmanctl> enable wifi
Enabled wifi
connmanctl> scan wifi
Scan completed for wifi
connmanctl> services
*AO Wired                ethernet_b827ebbde13c_cable
                         wifi_e8de27077de3_hidden_managed_none
    AH04044914           wifi_e8de27077de3_41483034303434393134_managed_psk
    Frissie              wifi_e8de27077de3_46726973736965_managed_psk
    ruijgt gast          wifi_e8de27077de3_7275696a67742067617374_managed_psk
    schuur               wifi_e8de27077de3_736368757572_managed_psk
connmanctl> agent on
Agent registered
connmanctl> connect wifi_e8de27077de3_41      # You can use the TAB key at this point to autocomplete the name
connmanctl> connect wifi_e8de27077de3_41483034303434393134_managed_psk
Agent RequestInput wifi_e8de27077de3_41483034303434393134_managed_psk
  Passphrase = [ Type=psk, Requirement=mandatory ]
Passphrase? *************
Connected wifi_e8de27077de3_41483034303434393134_managed_psk
connmanctl> quit
```

Now use the following command to find Seeed NPi-STM32MP157C's IP address. 
```
ifconfig
```

**B. Ethernet connection**

You can connect to the network using an Ethernet cable. Just plug in the Ethernet cable to the Internet.

**SSH connection**

**A. SSH**

SSH, short for Secure Shell, is formulated by the Network Working Group of IETF. SSH is a security protocol based on the application layer. SSH is a more reliable protocol that provides security for remote login sessions and other network services. There is no SSH protocol in the image provided by us, so we need to configure it through the serial port, so as to realize the communication between the device and the computer through SSH protocol. Enter the following command to install the SSH service in Seeed NPi-STM32MP157C.

```bash
sudo apt-get install openssh-server -y
systemctl start ssh.service
```

Next, we'll use SSH to access Seeed NPi-STM32MP157C. Windows users can use third-party SSH clients. For Linux/Mac users, the SSH client is built in.

- Windows users : Use PUTTY, select SSH protocol, fill in the correct IP address and click open. The user name is debian and the password is temppwd.

- Linux/Mac users :
```
ssh debian@IP
// password: temppwd
```

<div class="admonition note" >
<p class="admonition-title">Note</p>
If the performance experience degrades while using SSH, please switch to a more accessible WiFi network.
</div>

### Pyqt

PyQt is one of the most popular Python adhesives for Qt cross-platform c++ frameworks, next I'll use Pyqt for our application.

```bash

sudo sed -i 's/deb.debian.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apt/sources.list
sudo apt-get update
sudo apt-get install python3 python3-distutils python3-pyqt5 git  

export QT_QPA_PLATFORM=linuxfb:fb=/dev/fb0

git clone https://github.com/Seeed-Studio/seeed-linux-dtverlays
cd seeed-linux-dtverlays

 ```
## Resourses
-----
- **[PDF]** [STM32MP157C Datasheet](https://github.com/SeeedDocument/Seeed-NPi-STM32MP157C/raw/master/Hardware/stm32mp157c.pdf)
- **[SCH]** [Seeed STM32MP157C SOM](https://github.com/SeeedDocument/Seeed-NPi-STM32MP157C/raw/master/Hardware/Seeed%20SoM%20-%20STM32MP157C%20v1.0_191212.pdf)
- **[SCH]** [Seeed STM32MP157C NPi](https://github.com/SeeedDocument/Seeed-NPi-STM32MP157C/raw/master/Hardware/Seeed%20NPi%20-%20STM32MP157C%20v1.0_191212.pdf)
