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

Seeed NPi-STM32MP157C is an open source hardware development board based on the STM32MP157C microcontroller by Seeed Studio. Seeed NPi-STM32MP157C not only provides all of the system's source code for users to learn how to turn it into an arm development board, but it's similar in size to a Raspberry Pi. Although the house sparrow is small, but be fullies equipped. It includes a high performance flexible WiFi/bluetooth interface and two Grove connectors,  which make it easier to connect to the large grove sensor family. It supports the MIPI DSI interface and CAN FD interface, also compatible with Raspberry Pi's 40-pin interface.

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
- Industrial
- Automation and process control
- The man-machine interface
- Sensor center
- Robot

## Hardware Overview

![]()

Pin illustration


### Pin Function

Seeed NPi-STM32MP157C's 40-pin is fully compatible with Raspberry Pi's 40PIN, including GPIO, IIC, UART, SPI, IIS and PWM pins, as described below.

#### GPIO

GPIO, Short for general type input and output, functions are similar to p0-p3 of 8051, it's connecting pin can be used freely by the user by program control, The PIN can be used as a general input (GPI) or general output (GPO) or general input and output (GPIO) based on practical considerations. For example, it can be used as CLK generator, chip select etc. The following figure shows the location of GPIO in the pin-map.

!!!Note

    In GPIO mode, each digital I/O can generate an interrupt.


![enter image description here]()


#### UART

A universal asynchronous transceiver, often referred to as a UART, the data it will transmit will be converted between serial communication and parallel communication. As a chip that converts a parallel input signal into a serial output signal, UART is usually integrated into the connection of other communication interfaces. The following figure shows the location of UART in pin-map.

!!!Note

    There is a dedicated connector for connecting to the UART0 pin and for connection debugging.There is also a serial extended connection port.


![enter image description here]()


#### I2C

I2C is short for IICBus, so the Chinese should be called integrated circuit bus, it is a serial communication bus, using a multi-master-slave structure. The following figure shows the location of I2C in pin-map.

!!!Note

     The first I2C bus is used to read the EEPROMS on the Cape add-on board and cannot be used for other digital I/O port operations without affecting this functionality, but you can still use it to add other I2C devices to the available addresses. The second I2C bus is available for you to configure and use.

![enter image description here]()

#### SPI

SPI stands for serial peripheral interface, a high-speed, full-duplex, synchronous communication bus, only four wires are used in the pin of the chip, which saves the pin of the chip, it also saves space for PCB layout. Because it's easy to use, more and more chips are integrated with the SPI communication protocol. The following figure shows the location of SPI in the pin-map.

!!!Note

    To move data out quickly, you might consider using one of the SPI ports.

![enter image description here]()

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


**Serial console**

Now that your Seeed NPi-STM32MP157C is up, you may want to access your Linux system through the console, then set up WiFi, and so on. Two serial port access methods are provided for Linux access: 

- A. OTG USB port - You need to run a Linux system on a circuit board.

- B. UART port - Used to debug low-level problems.

**A. Connect via OTG**

- **Step 1.** Take a USB type-c cable and make sure it's a data cable, plug it into Seeed NPi-STM32MP157C's USB type-c port, and then plug the other end of the USB type-c cable into your computer. 

![]()

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

PyQt is one of the most popular Python adhesives for Qt cross-platform c++ frameworks.

```bash
sed -i 's/deb.debian.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apt/sources.list
sudo apt-get update
sudo apt-get install python3 python3-distutils python3-pyqt5 git  
export QT_QPA_PLATFORM=linuxfb:fb=/dev/fb0

```

## Resourses
-----
- **[PDF]** [STM32MP157C Datasheet](https://github.com/SeeedDocument/Seeed-NPi-STM32MP157C/raw/master/Hardware/stm32mp157c.pdf)
- **[SCH]** [Seeed STM32MP157C SOM](https://github.com/SeeedDocument/Seeed-NPi-STM32MP157C/raw/master/Hardware/Seeed%20SoM%20-%20STM32MP157C%20v1.0_191212.pdf)
- **[SCH]** [Seeed STM32MP157C NPi](https://github.com/SeeedDocument/Seeed-NPi-STM32MP157C/raw/master/Hardware/Seeed%20NPi%20-%20STM32MP157C%20v1.0_191212.pdf)
