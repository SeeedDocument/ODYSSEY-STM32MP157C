# SOM – STM32MP157C 


## 产品特性

- 体积小巧,功能强大
- 可扩展的工业级
- 开源硬件/ SDK / API / BSP / OS

## 创意应用

- 消费者
- 工业
- 白色家电
- 医疗
- 高端可穿戴设备

## 规格参数

|项目|参数值|
|----|------|
|MPU(STM32MP157C)|1 x 32-bit dual-core Arm Cortex-A7 <br>1 x 32-bit Arm Cortex-M4 with FPU/MPU|
|PMU|1 x ST PMIC STPMIC1A |
|RAM|1 x 512MB DDR3 RAM|
|Flash|1 x 4GB EMMC|
|外围接口|3 x 板对板70-Pin连接器|

## 硬件概述

下面是Seeed SOM - STM32MP157C的硬件详细说明

![](https://github.com/SeeedDocument/Seeed-NPi-STM32MP157C/raw/master/IMG/SOM-overview.png)

- **1.STM32MP157C:** 开发板的主控制芯片(Arm® Cortex®-A7 和 Cortex®-M4双架构处理器)

- **2.MT41K256M16TW-107:P:** 512M16bitRAM内存芯片

- **3.STPMIC1APQR:** 电源管理芯片

- **4.EMMC04G-M627:** 4GeMMC内存

- **5.LED:** 当供电成功时,PWR会被点亮,当系统正常运行时,USER将会无限循环闪烁.

- **6.70-PIN接口:** 可以从下面的表格来查找每个引脚对应的功能

|Pin 封装编号|Pin 编号|Pin 名称|Pin 类型|可选择的功能|附加功能|
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
|AC4|32|PF14|I/O|TRACED6,DFSDM1_CKIN6,I2C4_SCL,I2C1_SCL,ETH1_GMII_RXD6,FMC_A8,EVENTOUT|ADC2_INP6,ADC2_INN2|
|Y5|33|PF13|I/O|TRACED5,DFSDM1_DATIN6,I2C4_SMBA,I2C1_SMBA,DFSDM1_DATIN3,ETH1_GMII_RXD5,FMC_A7,EVENTOUT|ADC2_INP2|
|Y4|34|PF15|I/O|TRACED7,I2C4_SDA,I2C1_SDA, ETH1_GMII_RXD7,FMC_A9, EVENTOUT|-|
|-|35|GND|S|-|-|
|L3|36|PD14|I/O|TIM4_CH3,SAI3_MCLK_B,UART8_CTS,FMC_AD0/FMC_D0,EVENTOUT|-|
|U3|37|ANA0|A|-|ADC1_INP0,ADC1_INN1,ADC2_INP0,ADC2_INN1|
|J2|38|PD15|I/O|TIM4_CH4,SAI3_MCLK_A,UART8_CTS,FMC_AD1/FMC_D1,LCD_R1,EVENTOUT|-|
|U4|39|ANA1|A|-|ADC1_INP1,ADC2_INP1|
|R2|40|PWR_ON|O|-|PWR_ONLP|
|-|41|GND|S|-|-|
|K2|42|PC13|I/O|EVENTOUT|RTC_OUT1/RTC_TS/RTC_LSCO,TAMP_IN1/TAMP_OUT2/TAMP_OUT3,WKUP3|
|T2|43|PA14|I/O|DBTRGO,DBTRGI,MCO2,EVENTOUT|-|
|AB3|44|PA0|I/O|TIM2_CH1/TIM2_ETR,TIM5_CH1,TIM8_ETR,TIM15_BKIN,USART2_CTS/USART2_NSS,UART4_TX,SDMMC2_CMD,SAI2_SD_B,ETH1_GMII_CRS/ETH1_MII_CRS,EVENTOUT|ADC1_INP16,WKUP1|
|G2|45|PZ4|I/O|I2C6_SCL,I2C2_SCL,I2C5_SCL,I2C4_SCL,EVENTOUT|-|
|-|46|PONKEYN|S|-|-|
|B6|47|PD4|I/O|SAI3_FS_A,USART2_RTS/USART2_DE,SDMMC3_D1,DFSDM1_CKIN0,FMC_NOE,EVENTOUT|-|
|-|48|GDN|S|-|-|
|Y9|49|PF12|I/O|TRACED4,ETH1_GMII_RXD4,FMC_A6,EVENTOUT|ADC1_INP6,ADC1_INN2|
|M3|50|NRST|I/O|-|-|
|AC11|51|PF8|I/O|TRACED12,TIM16_CH1N,SPI5_MISO,SAI1_SCK_B,UART7_RTS/UART7_DE,TIM13_CH1,QUADSPI_BK1_IO0,EVENTOUT|-|
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

- **7.70-PIN接口:**可以从下面的表格来查找每个引脚对应的功能

|Pin 封装编号|Pin 编号|Pin 名称|Pin 类型|可选择的功能|附加功能|
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

- **8.70-PIN接口:**可以从下面的表格来查找每个引脚对应的功能

|Pin 封装编号|Pin 编号|Pin 名称|Pin 类型|可选择的功能|附加功能|
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
,下面我们将分别进行介绍.

#### GPIO

GPIO,通用型之输入输出的简称,功能类似8051的P0—P3,其接脚可以供使用者由程控自由使用,PIN脚依现实考量可作为通用输入（GPI）或通用输出（GPO）或通用输入与输出（GPIO）,如当时钟产生器,片选等,具体位置参考上图.

!!!Note
    - 在GPIO模式下,每个数字I / O都可产生中断

#### UART

通用异步收发传输器,通常称作UART.它将要传输的资料在串行通信与并行通信之间加以转换.作为把并行输入信号转成串行输出信号的芯片,UART通常被集成于其他通讯接口的连结上.具体位置参考上图.

!!!Note
    - 有一个专用连接头用于连接 UART0 引脚并用于连接调试. 另外还有一个串行扩展连接端口.

#### I2C

I2C其实是IICBus简称,所以中文应该叫集成电路总线,它是一种串行通信总线,使用多主从架构.具体位置参考上图.

!!!Note
     第一个 I2C 总线用于读取 Cape 附加板上的 EEPROMS ,所以不能用于其他数字I/ O端口操作,但您仍然可使用它在可用地址中添加其他 I2C 设备. 第二个 I2C 总线可供您配置和使用.

#### SPI

SPI是串行外设接口的缩写,是一种高速的,全双工,同步的通信总线,并且在芯片的管脚上只占用四根线,节约了芯片的管脚,同时为PCB的布局上节省空间,提供方便,正是出于这种简单易用的特性,越来越多的芯片集成了这种通信协议具体位置参考上图.

!!!Note
    为了快速移出数据,您可以考虑使用其中一个 SPI 端口.

#### I2S

I2S总线是飞利浦公司为数字音频设备之间的音频数据传输而制定的一种总线标准,该总线专责于音频设备之间的数据传输,广泛应用于各种多媒体系统.具体位置参考上图.
