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

Seeed NPi-STM32MP157C是由Seeed Studio基于STM32MP157C微控制器的开源硬件开发板。Seeed NPi-STM32MP157C不仅能提供系统的所有源码来供用户学习使之变成arm开发板，而且其大小与树莓派的大小类似，但麻雀虽小却五脏俱全，包括高性能灵活的 WiFi /蓝牙接口和两个 Grove 连接器，使其更容易连接到大型 Grove 传感器系列，支持MIPI DSI接口和CAN FD接口，同时也兼容树莓派的40-pin接口。

 [![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.1e729b66GJVV3r&id=533937368398)

## 产品特性

- 16位 512M RAM & 4GB eMMC
- USB OTG 可外接 USB 设备
- 2.4G WiFi & BT 4.2 （可外接天线）
- Grove 接口(一个IIC一个数字)
- 3.5mm 音频插孔
- 基于 Debian 的 Linux 系统
- 兼容树莓派的40-PIN GPIO
- 支持千兆以太网
- 支持MIPI DSI显示
- 支持DVP摄像头
- 支持音频播放
- 可通过DC接口额外供电（建议使用12V/2A电源输入）

## 规格参数

|项目|参数值|
|----|------|
|处理器|  STM32MP157C(Arm® Cortex®-A7 和 Cortex®-M4双架构处理器)|
|内存|	512M DDR3|
|板载闪存	|4GB eMMC|
|CPU支持	| 3D 图形加速器和CAN FD协议和MIPI DSI显示|
|USB支持 |供电与通信|
|USB |USB2.0 主机	x2|
|Grove 连接口|2个(I2C 和 Digital) |
|GPIO	|40-PIN引脚|
|以太网	|千兆级|
|工作温度	|0 ~ 75 ℃|

## 创意应用

- 物联网
- 智慧之家
- 工业
- 自动化与过程控制
- 人机接口
- 传感器中心
- 机器人

## 硬件概述

![]()

引脚说明图


### 引脚功能

Seeed NPi-STM32MP157C的40-PIN完全兼容树莓派的40PIN，包括GPIO,IIC,UART,SPI，IIS以及PWM引脚，下面我们将分别进行介绍.

#### GPIO

GPIO，通用型之输入输出的简称，功能类似8051的P0—P3，其接脚可以供使用者由程控自由使用，PIN脚依现实考量可作为通用输入（GPI）或通用输出（GPO）或通用输入与输出（GPIO），如当clk generator, chip select等。下图是GPIO在PIN-MAP中的位置。

!!!Note
    - 在GPIO模式下，每个数字I / O都可产生中断

![enter image description here]()

#### UART

通用异步收发传输器，通常称作UART。它将要传输的资料在串行通信与并行通信之间加以转换。作为把并行输入信号转成串行输出信号的芯片，UART通常被集成于其他通讯接口的连结上。下图是UART在PIN-MAP中的位置。

!!!Note
    - 有一个专用连接头用于连接 UART0 引脚并用于连接调试。 另外还有一个串行扩展连接端口。

![enter image description here]()


#### I2C

I2C其实是IICBus简称，所以中文应该叫集成电路总线，它是一种串行通信总线，使用多主从架构。下图是I2C在PIN-MAP中的位置。

!!!Note
     第一个 I2C 总线用于读取 Cape 附加板上的 EEPROMS ，不能用于其他数字 I / O 端口操作，而不会影响该功能，但您仍然可使用它在可用地址中添加其他 I2C 设备。 第二个 I2C 总线可供您配置和使用。

![enter image description here]()

#### SPI

SPI是串行外设接口的缩写，是一种高速的，全双工，同步的通信总线，并且在芯片的管脚上只占用四根线，节约了芯片的管脚，同时为PCB的布局上节省空间，提供方便，正是出于这种简单易用的特性，越来越多的芯片集成了这种通信协议。下图是SPI在PIN-MAP中的位置。

!!!Note
    为了快速移出数据，您可以考虑使用其中一个 SPI 端口。

![enter image description here]()

## 软件入门指导

### 准备工作


**准备材料**

- Seeed NPi-STM32MP157C
- Wi-Fi 网络
- 4GB (或更大) SD 卡和 SD 读卡器
- PC 或 Mac
- [USB To Uart Adapter](https://www.seeedstudio.com/USB-To-Uart-5V%26amp%3B3V3-p-1832.html) (可选的)
- 用于供电的12V/2ADC接口适配器 (可选的)
- 一根 USB Type-C 线

<div class="admonition warning">
<p class="admonition-title">注意</p>
请轻轻插入 USB 线，否则可能会损坏接口。请使用内部有 4 根线的 USB 线，2 根线的不能传输数据。如果您不确定您的线，可以点击 <a href="https://www.seeedstudio.com/Micro-USB-Cable-48cm-p-1475.html"><B>此处</B></a> 购买
</div>


**镜像安装**

与 Raspberry Pi 类似，您需要从 SD 卡安装 Seeed NPi-STM32MP157C 映像才能启动并运行。我们提供两种启动 Seeed NPi-STM32MP157C 的方法。您可以从 SD 卡启动或从 eMMC 启动。

**A. 从 SD 卡启动**

点击此处下载 [固件](https://github.com/Seeed-Studio/seeed-linux-images)，进入`STM32MP1`文件夹选择你想下载的固件


- **步骤 1.** 进入`STM32MP1`文件夹选择你想下载的固件 :

- **步骤 2.** 用 SD 读卡器将 SD 卡接入 PC 或 MAC。需要大于 4G 的 SD 卡。

- **步骤 3.** <font face="">点击此处下载 <a href="https://etcher.io/">Etcher</a>，然后使用 Etcher 将 ```*.img.xz``` 文件直接写入到 SD 卡。或者将 ```*.img.xz``` 文件解压缩为 ```*.img``` 文件，然后用其他镜像写入工具将其刻录到 SD 卡。
<br>
<br>点击加号图标添加刚下载的镜像文件，软件会自动选择您插入的 SD 卡。然后点击 Flash！开始写入。大约需要 10 分钟完成。</font>

![](https://github.com/SeeedDocument/Respeaker_V2/raw/master/img/v2-flash-sd.png)


- **步骤 4.** 将镜像写入 SD 卡后，将 SD 卡插入 Seeed NPi-STM32MP157C 。使用 USB Type-C 端口为主板供电，写入过程中请勿取出 SD 卡。Seeed NPi-STM32MP157C 将从 SD 卡启动，您可以看到 PWR 和 USER LED 点亮。USER 配置为启动时以心跳模式闪烁。现在，转到下一部分 : 串口控制台。


**串口控制台**

现在您的Seeed NPi-STM32MP157C已经启动了，您可能希望通过控制台访问 Linux 系统，然后来设置 WiFi 等。提供了两种串口访问方式进行linux访问:

- A. OTG USB 端口 - 需要在电路板上运行 Linux 系统

- B. UART 端口 - 用于调试低级问题

**A. 通过 OTG 连接**

- **步骤 1.** 找一条  USB Type-C 线，并确保它是数据线，插入 Seeed NPi-STM32MP157C 的 USB Type-C 端口 ，然后将 USB Type-C 线的另一端插入电脑。

![]()

- **步骤 2.** 检查计算机串口是否启用 :

    - Windows : 检查设备管理器，应该有新的串行设备名为 ```COMx```，其中 x 是一个越来越大的数字。如果您使用 windows XP/7/8，也许需要安装 [windows CDC 驱动程序](https://github.com/respeaker/get_started_with_respeaker/blob/master/files/ReSpeaker_Gadget_CDC_driver.7z)。
    - Linux : ls ```/dev/ttyACM*```，应该得到 ```/dev/ttyACMx``` 其中 x 取决于您使用的 USB 端口.
    - Mac : ls ```/dev/cu.usb*```，应该得到 ```/dev/cu.usbmodem14xx``` 其中 xx 取决于您使用的 USB 端口。


- **步骤 3.** 使用您最喜欢的串口调试工具来连接串口，串口有 : 115200 波特率，8 位，奇偶校验无，停止位 1，流量控制无。举些例子 :

    - Windows : 使用 [PUTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)，选择 ```Serial``` 协议，填入 Seeed NPi-STM32MP157C 对应的 COM 端口，```115200``` 波特率，8 位，奇偶校验无，停止位 1，流量控制无。
    - Linux : 取决于 USB To TTL Adapter，应该是 ```screen /dev/ttyACM0(,1, and so on) 115200``` 或 ```screen /dev/ttyUSB0(,1, and so on) 115200```
    - Mac : 取决于 USB To TTL Adapter，应该是 ```screen /dev/cu.usbserial1412(,1422, and so on) 115200``` 或 ```screen /dev/cu.usbmodem1412(,1422, and so on) 115200```


- **步骤 4.** 默认用户名是 ```debian```，密码是 ```temppwd```

**B. 通过 UART 端口连接**

在本节中，我们将引导您使用将连接到 Seeed NPi-STM32MP157C 的 Uart 端口 (位于 Seeed NPi-STM32MP157C 右上方) 的 USB 转 TTL 适配器，建立计算机与 Seeed NPi-STM32MP157C 的连接。

- **步骤 1.** 使用 USB To TTL Adapter 连接 Uart 端口和 PC/Mac。请注意，RX/TX 的电压为 3.3V。如果您没有 USB To TTL Adapter，点击 [此处](https://item.taobao.com/item.htm?id=550981934087) 购买.（RX->TX,TX->RX）

- **步骤 2.** 使用以下串口调试工具，波特率为 115200 :
    - Windows : 使用 [PUTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)，选择 ```Serial``` 协议，填入 Seeed NPi-STM32MP157C 对应的 COM 端口，```115200``` 波特率，8 位，奇偶校验无，停止位 1，流量控制无。
    - Linux : 取决于 USB To TTL Adapter，应该是 ```screen /dev/ttyACM0(,1, and so on) 115200``` 或 ```screen /dev/ttyUSB0(,1, and so on) 115200```。
    - Mac : 取决于 USB To TTL Adapter，应该是 ```screen /dev/cu.usbserial1412(,1422, and so on) 115200``` 或 ```screen /dev/cu.usbmodem1412(,1422, and so on) 115200```。

- **步骤 3.** 默认用户名是 ```debian```，密码是 ```temppwd```

- **步骤 4.** 如果没有 USB to TTL Adapter，也可以使用 Arduino。如果使用 Arduino，将跳线的一端连接到 Arduino 的 RESET 引脚，另一端连接到 Arduino 的 GND 引脚。这将绕过您的 Arduino 的 ATMEGA MCU，并将您的 Arduino 转换为一个 USB to TTL adapter，请参看 [此处](https://www.youtube.com/watch?v=qqSLwK1DP8Q) 的视频教程。现在将 Arduino 的 GND 引脚连接到 Seeed NPi-STM32MP157C 的 Uart 端口的 GND 引脚。将 Arduino 上的 Rx 引脚连接到 Seeed NPi-STM32MP157C 的 Uart 端口上的 Rx 引脚。将 Arduino 上的 Tx 引脚连接到 Seeed NPi-STM32MP157C 的 Uart 端口上的 Tx 引脚。最后，通过 Arduino 的 USB 电缆将 Arduino 连接到 PC/Mac。现在通过输入以下命令检查您的 PC/Mac 是否找到您的 Arduino :

```
ls /dev/cu.usb* (Mac)
ls /dev/ttyACM* (Linux)
```
应该得到类似这样的反馈 :

```
/dev/cu.usbmodem14XX where XX will vary depending on which USB port you used (on Mac)
/dev/ttyACMX where X will vary depending on which USB port you used  (on Linux)
```
现在按照上述步骤通过串行连接连接到 Seeed NPi-STM32MP157C。一般在我们第一次开机的时候需要做这样的操作，因为您接下将设置 Seeed NPi-STM32MP157C 进行 Wi-Fi 连接，然后通过 SSH 或 VNC 进行连接。

**网络设置**

**A. Wi-Fi 设置**

通过网络管理工具`connmanctl`配置 Seeed NPi-STM32MP157C 的网络，`connmanctl`已经安装在 Seeed NPi-STM32MP157C 的镜像上。按照下面的操作指令就能轻松完成配置。

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

现在使用下面的命令找到 Seeed NPi-STM32MP157C 的 IP 地址。

```
ifconfig
```

**B. 以太网连接**

您可以使用以太网线连接到网络。只需插上连接到互联网的以太网线即可。

**通过 SSH 连接**

**A. SSH**

SSH 为 Secure Shell 的缩写，由 IETF 的网络小组（Network Working Group）所制定；SSH 为建立在应用层基础上的安全协议。SSH 是较可靠，专为远程登录会话和其他网络服务提供安全性的协议。我们的提供的镜像中没有自带ssh这个协议所以我们需要通过串口去进行配置，从而实现通过ssh协议进行设备的与电脑之间的通信。输入下面的命令将在Seeed NPi-STM32MP157C中安装ssh服务。

```bash
sudo apt-get install openssh-server -y
systemctl start ssh.service
```

下面，我们将使用SSH对Seeed NPi-STM32MP157C进行访问，Windows 用户，可用第三方 SSH 客户端。对于 Linux/Mac 用户，SSH 客户端是内置的。

- Windows 用户 : 使用 PUTTY，选择 SSH 协议，填写正确的 IP 地址并单击 open。用户名是debian,密码是temppwd。

- Linux/Mac 用户 :
```
ssh debian@IP
// password: temppwd
```

<div class="admonition note" >
<p class="admonition-title">Note</p>
请注意，如果使用 SSH 时性能体验下降，请切换到更畅通的 WiFi 网络。
</div>

### Pyqt

PyQt是用于Qt跨平台c++框架的最流行的Python黏合之一,

```bash
sed -i 's/deb.debian.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apt/sources.list
sudo apt-get update
sudo apt-get install python3 python3-distutils python3-pyqt5 git  
export QT_QPA_PLATFORM=linuxfb:fb=/dev/fb0

```

## 资源下载
-----
- **[PDF]** [STM32MP157C Datasheet](https://github.com/SeeedDocument/Seeed-NPi-STM32MP157C/raw/master/Hardware/stm32mp157c.pdf)
- **[SCH]** [Seeed STM32MP157C SOM](https://github.com/SeeedDocument/Seeed-NPi-STM32MP157C/raw/master/Hardware/Seeed%20SoM%20-%20STM32MP157C%20v1.0_191212.pdf)
- **[SCH]** [Seeed STM32MP157C NPi](https://github.com/SeeedDocument/Seeed-NPi-STM32MP157C/raw/master/Hardware/Seeed%20NPi%20-%20STM32MP157C%20v1.0_191212.pdf)
