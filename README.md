---
name: ODYSSEY – STM32MP157C 
category: ODYSSEY – STM32MP157C 
bzurl: https://www.seeedstudio.com/SeeedStudio-BeagleBone-Green-Wireless-p-2650.html
oldwikiname: SeeedStudio_BeagleBone_Green_Wireless
prodimagename: BBGW_cover.png
wikiurl: http://wiki.seeedstudio.com/cn/BeagleBone_Green_Wireless
sku: 102010048
---

# ODYSSEY – STM32MP157C 

ODYSSEY – STM32MP157C是基于STM32MP157C的单板计算机，STM32MP157C是工作在650Mhz的双核Arm-Cortex-A7核心处理器，该处理器还集成了Arm Cortex-M4协处理器，使其适合于实时任务。 ODYSSEY – STM32MP157C以SoM（模块上系统）和载板的形式创建。 SoM由MPU，PMIC，RAM组成，并且载板采用Raspberry Pi尺寸.载板包括所有必需的外围设备，包括千兆以太网，WiFi / BLE，DC电源，USB主机，USB-C，MIPI-DSI，用于摄像机和音频的DVP等。通过该板，客户可以快速评估SoM并进行部署,SoM可以轻松快捷地放在自己的载板上.

 [![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.1e729b66GJVV3r&id=533937368398)

## 产品特性

- 体积小巧,功能强大
- 可扩展的工业级
- 开源硬件/ SDK / API / BSP / OS

## 规格参数

|项目|参数值|
|----|------|
|外围设备接口|2 x USB Host <br>1 x 千兆以太网接口<br>1 x 3.5mm音频接口<br>1 x MIPI DSI显示器接口<br>1 x DVP摄像头接口<br>2 x Grove (GPIO & I2C)<br>1 x SD卡接口(在板子背面)|
|WiFi/蓝牙|WiFi 802.11 b/g/n 2.4GHz<br>蓝牙4.1|
|板载LED|1 x 复位LED<br>3 x 用户自定义LED<br>1 x 电源LED|
|电源|1 x DC 接口(建议使用12V/2A电源输入)<br>1 x USB Type-C|
|按键|1 x 复位按键<br>1 x 用户按键<br>1 x 拨码按键|
|尺寸|56mm x 85mm|
|工作温度	|0 ~ 75 ℃|

## 创意应用

- 消费者
- 工业
- 白色家电
- 医疗
- 高端可穿戴设备

## 硬件概述

ODYSSEY – STM32MP157C 包括两个部分,分别是 Seeed NPi - STM32MP157C 母板和 [Seeed SoM - STM32MP157C](https://github.com/SeeedDocument/Seeed-NPi-STM32MP157C/blob/master/SOM_STM32P1.md).

下面是Seeed NPi - STM32MP157C的硬件详细说明

![](https://github.com/SeeedDocument/Seeed-NPi-STM32MP157C/raw/master/IMG/front.png)

![](https://github.com/SeeedDocument/Seeed-NPi-STM32MP157C/raw/master/IMG/back.png)

- **1.Seeed SoM - STM32MP157C插槽:** 安装Seeed SoM - STM32MP157C的区域,如果用户想要取下核心板,慢慢将核心板翘起来,然后再取下,切忌用手暴力拆取.

- **2.DC电源输入口:** 12V~24V/2A (建议使用12V/2A电源输入).

- **3.ETH接口:** 网线接口可接千兆级网络

- **4.USB Host:** 两个USB Host接口

- **5.USB Device:** USB 2.0 Type C 如果使用Type C作为板子电源输入,应使用5V/3A电源适配器

- **6.Digital Grove接口:** 连接数字引脚的Grove接口

- **7.IIC Grove接口:** 连接IIC引脚的Grove接口

- **8.美标3.5mm:** 音频接口

- **9.MIPI DSI 接口:** 连接带MIPI DSI 接口的显示器(FPC 20Pin 1.0mm)

- **10.40 PIN GPIO接口:** 兼容树莓派的40-PIN

- **11.AP6236:** 2.4G WiFi & BT 4.2 控制芯片

- **12.滑动开关:** 可通过滑动开关选择SD卡或eMMC启动

- **13.Debug UART:** 系统默认的调试串口可以进入该串口去访问系统,后面会详细介绍如何操作.

- **14.JST 1.0mm:** 3VRTC电池接口

- **15.RST 按键:** 系统复位按键

- **16.PWR 按键:** 长按约8S关机；短按可开机

- **17.User 按键:** 用户可编程按键

- **18.PWR LED:** 开发板电源灯

- **19.User LED:** 用户可编程LED

- **20.ACA-5036-A2-CC-S:** 板载2.4G陶瓷天线

- **21.IPEX 1代:** 外接2.4G外接天线座子(使用外接天线时,需要移除R49,焊上R51 0Ω)

- **22.SD卡槽:**  插入装有系统的micro-SD卡的区域

- **23.DVP摄像机接口:** 连接带DVP接口的摄像头(FPC 20Pin 1.0mm)

- **24.KSZ9031:** 1000M网线驱动网卡

- **25.STMPS2252MTR:** 电源开关芯片

- **26.MP9943:** Buck DCDC 电源芯片

- **27.WM8960:** 音频编解码芯片

- **28.MP2161:** Buck DCDC 电源芯片

### 引脚功能

![](https://github.com/SeeedDocument/Seeed-NPi-STM32MP157C/raw/master/IMG/GPIO.png)

ODYSSEY – STM32MP157C 的40-PIN完全兼容树莓派的40PIN,包括GPIO,I2C,UART,SPI,I2S引脚.

## 软件入门指导

### 准备工作

**准备材料**

- ODYSSEY – STM32MP157C 
- Wi-Fi 网络
- 4GB (或更大) SD 卡和 SD 读卡器
- PC 或 Mac
- [USB To Uart Adapter](https://www.seeedstudio.com/USB-To-Uart-5V%26amp%3B3V3-p-1832.html) (可选的)
- 用于供电的12V/2ADC接口适配器 (可选的)
- 一根 USB Type-C 线

<div class="admonition warning">
<p class="admonition-title">注意</p>
请轻轻插入 USB 线,否则可能会损坏接口.请使用内部有 4 根线的 USB 线,2 根线的不能传输数据.如果您不确定您的线,可以点击 <a href="https://www.seeedstudio.com/Micro-USB-Cable-48cm-p-1475.html"><B>此处</B></a> 购买
</div>


**镜像安装**

与 Raspberry Pi 类似,您需要从 SD 卡安装 ODYSSEY – STM32MP157C  映像才能启动并运行.我们提供两种启动 ODYSSEY – STM32MP157C  的方法.您可以从 SD 卡启动或从 eMMC 启动.

**A. 从 SD 卡启动**

点击此处下载 [固件](https://github.com/Seeed-Studio/seeed-linux-images),进入`STM32MP1`文件夹选择你想下载的固件


- **步骤 1.** 进入`STM32MP1`文件夹选择你想下载的固件 :

- **步骤 2.** 用 SD 读卡器将 SD 卡接入 PC 或 MAC.需要大于 4G 的 SD 卡.

- **步骤 3.** <font face="">点击此处下载 <a href="https://etcher.io/">Etcher</a>,然后使用 Etcher 将 ```*.img.xz``` 文件直接写入到 SD 卡.或者将 ```*.img.xz``` 文件解压缩为 ```*.img``` 文件,然后用其他镜像写入工具将其刻录到 SD 卡.
<br>
<br>点击加号图标添加刚下载的镜像文件,软件会自动选择您插入的 SD 卡.然后点击 Flash！开始写入.大约需要 10 分钟完成.</font>

![](https://github.com/SeeedDocument/Respeaker_V2/raw/master/img/v2-flash-sd.png)


- **步骤 4.** 将镜像写入 SD 卡后,将 SD 卡插入 ODYSSEY – STM32MP157C  .使用 USB Type-C 端口为主板供电,写入过程中请勿取出 SD 卡.ODYSSEY – STM32MP157C  将从 SD 卡启动,您可以看到 PWR 和 USER LED 点亮.USER 配置为启动时以心跳模式闪烁.现在,转到下一部分 : 串口控制台.

**B. 从 eMMC 卡启动**

点击此处下载 [固件](https://github.com/Seeed-Studio/seeed-linux-images),进入`STM32MP1`文件夹选择你想下载的固件.

- **步骤 1.** 进入`STM32MP1`文件夹选择你想下载的固件 :

- **步骤 2.** 用 SD 读卡器将 SD 卡接入 PC 或 MAC.需要大于 4G 的 SD 卡.

- **步骤 3.** <font face="">点击此处下载 <a href="https://etcher.io/">Etcher</a>,然后使用 Etcher 将 ```*.img.xz``` 文件直接写入到 SD 卡.或者将 ```*.img.xz``` 文件解压缩为 ```*.img``` 文件,然后用其他镜像写入工具将其刻录到 SD 卡.
<br>
<br>点击加号图标添加刚下载的镜像文件,软件会自动选择您插入的 SD 卡.然后点击 Flash！开始写入.大约需要 10 分钟完成.</font>

![](https://github.com/SeeedDocument/Respeaker_V2/raw/master/img/v2-flash-sd.png)

- **步骤 4.** 将镜像写入 SD 卡后,将 SD 卡插入 ODYSSEY – STM32MP157C  .使用 USB Type-C 端口为主板供电,写入过程中请勿取出 SD 卡.ODYSSEY – STM32MP157C  将从 SD 卡启动,您可以看到 PWR 和 USER LED 点亮.USER 配置为启动时以心跳模式闪烁.

- **步骤 5.** 将滑动开关拨到eMMC,然后重启即可.

**串口控制台**

现在您的ODYSSEY – STM32MP157C 已经启动了,您可能希望通过控制台访问 Linux 系统,然后来设置 WiFi 等.提供了两种串口访问方式进行linux访问:

- A. OTG USB 端口 - 需要在电路板上运行 Linux 系统

- B. UART 端口 - 用于调试低级问题

**A. 通过 OTG 连接**

- **步骤 1.** 找一条  USB Type-C 线,并确保它是数据线,插入 ODYSSEY – STM32MP157C  的 USB Type-C 端口 ,然后将 USB Type-C 线的另一端插入电脑.

- **步骤 2.** 检查计算机串口是否启用 :

    - Windows : 检查设备管理器,应该有新的串行设备名为 ```COMx```,其中 x 是一个越来越大的数字.如果您使用 windows XP/7/8,也许需要安装 [windows CDC 驱动程序](https://github.com/respeaker/get_started_with_respeaker/blob/master/files/ReSpeaker_Gadget_CDC_driver.7z).
    - Linux : ls ```/dev/ttyACM*```,应该得到 ```/dev/ttyACMx``` 其中 x 取决于您使用的 USB 端口.
    - Mac : ls ```/dev/cu.usb*```,应该得到 ```/dev/cu.usbmodem14xx``` 其中 xx 取决于您使用的 USB 端口.


- **步骤 3.** 使用您最喜欢的串口调试工具来连接串口,串口有 : 115200 波特率,8 位,奇偶校验无,停止位 1,流量控制无.举些例子 :

    - Windows : 使用 [PUTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html),选择 ```Serial``` 协议,填入 ODYSSEY – STM32MP157C  对应的 COM 端口,```115200``` 波特率,8 位,奇偶校验无,停止位 1,流量控制无.
    - Linux : 取决于 USB To TTL Adapter,应该是 ```screen /dev/ttyACM0(,1, and so on) 115200``` 或 ```screen /dev/ttyUSB0(,1, and so on) 115200```
    - Mac : 取决于 USB To TTL Adapter,应该是 ```screen /dev/cu.usbserial1412(,1422, and so on) 115200``` 或 ```screen /dev/cu.usbmodem1412(,1422, and so on) 115200```


- **步骤 4.** 默认用户名是 ```debian```,密码是 ```temppwd```

**B. 通过 UART 端口连接**

在本节中,我们将引导您使用将连接到 ODYSSEY – STM32MP157C  的 Uart 端口 (位于 ODYSSEY – STM32MP157C  右上方) 的 USB 转 TTL 适配器,建立计算机与 ODYSSEY – STM32MP157C  的连接.

- **步骤 1.** 使用 USB To TTL Adapter 连接 Uart 端口和 PC/Mac.请注意,RX/TX 的电压为 3.3V.如果您没有 USB To TTL Adapter,点击 [此处](https://item.taobao.com/item.htm?id=550981934087) 购买.（RX->TX,TX->RX）

- **步骤 2.** 使用以下串口调试工具,波特率为 115200 :
    - Windows : 使用 [PUTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html),选择 ```Serial``` 协议,填入 ODYSSEY – STM32MP157C  对应的 COM 端口,```115200``` 波特率,8 位,奇偶校验无,停止位 1,流量控制无.
    - Linux : 取决于 USB To TTL Adapter,应该是 ```screen /dev/ttyACM0(,1, and so on) 115200``` 或 ```screen /dev/ttyUSB0(,1, and so on) 115200```.
    - Mac : 取决于 USB To TTL Adapter,应该是 ```screen /dev/cu.usbserial1412(,1422, and so on) 115200``` 或 ```screen /dev/cu.usbmodem1412(,1422, and so on) 115200```.

- **步骤 3.** 默认用户名是 ```debian```,密码是 ```temppwd```

- **步骤 4.** 如果没有 USB to TTL Adapter,也可以使用 Arduino.如果使用 Arduino,将跳线的一端连接到 Arduino 的 RESET 引脚,另一端连接到 Arduino 的 GND 引脚.这将绕过您的 Arduino 的 ATMEGA MCU,并将您的 Arduino 转换为一个 USB to TTL adapter,请参看 [此处](https://www.youtube.com/watch?v=qqSLwK1DP8Q) 的视频教程.现在将 Arduino 的 GND 引脚连接到 ODYSSEY – STM32MP157C  的 Uart 端口的 GND 引脚.将 Arduino 上的 Rx 引脚连接到 ODYSSEY – STM32MP157C  的 Uart 端口上的 Rx 引脚.将 Arduino 上的 Tx 引脚连接到 ODYSSEY – STM32MP157C  的 Uart 端口上的 Tx 引脚.最后,通过 Arduino 的 USB 电缆将 Arduino 连接到 PC/Mac.现在通过输入以下命令检查您的 PC/Mac 是否找到您的 Arduino :

```
ls /dev/cu.usb* (Mac)
ls /dev/ttyACM* (Linux)
```
应该得到类似这样的反馈 :

```
/dev/cu.usbmodem14XX where XX will vary depending on which USB port you used (on Mac)
/dev/ttyACMX where X will vary depending on which USB port you used  (on Linux)
```
现在按照上述步骤通过串行连接连接到 ODYSSEY – STM32MP157C .一般在我们第一次开机的时候需要做这样的操作,因为接下将对 ODYSSEY – STM32MP157C  进行 Wi-Fi 连接,然后通过 SSH 或 VNC 进行连接.

**网络设置**

**A. Wi-Fi 设置**

通过网络管理工具`connmanctl`配置 ODYSSEY – STM32MP157C  的网络,`connmanctl`已经安装在 ODYSSEY – STM32MP157C  的镜像上.按照下面的操作指令就能轻松完成配置.

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

现在使用下面的命令找到 ODYSSEY – STM32MP157C  的 IP 地址.

```
ifconfig
```

**B. 以太网连接**

您可以使用以太网线连接到网络.只需插上连接到互联网的以太网线即可.

**通过 SSH 连接**

**A. SSH**

SSH 为 Secure Shell 的缩写,由 IETF 的网络小组（Network Working Group）所制定；SSH 为建立在应用层基础上的安全协议.SSH 是较可靠,专为远程登录会话和其他网络服务提供安全性的协议.我们的提供的镜像中没有自带ssh这个协议所以我们需要通过串口去进行配置,从而实现通过ssh协议进行设备的与电脑之间的通信.输入下面的命令将在ODYSSEY – STM32MP157C 中安装ssh服务.

```bash
sudo apt-get install ssh -y
```

下面,我们将使用SSH对ODYSSEY – STM32MP157C 进行访问,Windows 用户,可用第三方 SSH 客户端.对于 Linux/Mac 用户,则可以使用内置的SSH.

- Windows 用户 : 使用 PUTTY,选择 SSH 协议,填写正确的 IP 地址并单击 open.用户名是debian,密码是temppwd.

- Linux/Mac 用户 :
```
ssh debian@IP
// password: temppwd
```

<div class="admonition note" >
<p class="admonition-title">Note</p>
请注意,如果使用 SSH 时性能体验下降,请切换到更畅通的 WiFi 网络.
</div>

## CANBUS通信

下面是基于ODYSSEY – STM32MP157C 利用[2 Channel CAN BUS FD Shield for Raspberry Pi](https://www.seeedstudio.com/2-Channel-CAN-BUS-FD-Shield-for-Raspberry-Pi-p-4072.html)进行CANBUS通信的历程,首先利用[Seeeduino V4.2](https://www.seeedstudio.com/Seeeduino-V4-2-p-2517.html)采集环境的温度和湿度然后通过Seeeduino V4.2上面的[CAN-BUS Shield V2](https://www.seeedstudio.com/CAN-BUS-Shield-V2.html)与ODYSSEY – STM32MP157C 上面的2 Channel CAN BUS FD Shield for Raspberry Pi通信。

### 准备工作

**准备材料**

- ODYSSEY – STM32MP157C 
- Wi-Fi 网络
- 4GB (或更大) SD 卡和 SD 读卡器
- PC 或 Mac
- [USB To Uart Adapter](https://www.seeedstudio.com/USB-To-Uart-5V%26amp%3B3V3-p-1832.html) (可选的)
- 用于供电的12V/2ADC接口适配器 (可选的)
- 一根 USB Type-C 线
- 两根双公头杜邦线
- [CAN-BUS Shield V2](https://www.seeedstudio.com/CAN-BUS-Shield-V2.html)
- [Seeeduino V4.2](https://www.seeedstudio.com/Seeeduino-V4-2-p-2517.html)
- [2 Channel CAN BUS FD Shield for Raspberry Pi](https://www.seeedstudio.com/2-Channel-CAN-BUS-FD-Shield-for-Raspberry-Pi-p-4072.html)
- [Grove - Light Sensor v1.2](https://www.seeedstudio.com/Grove-Light-Sensor-v1-2.html)
- [Grove - I2C High Accuracy Temp&Humi Sensor (SHT35)](https://www.seeedstudio.com/catalogsearch/result/?q=sht35)

**硬件连接**

- **步骤 1.** 根据[安装指南](http://wiki.seeedstudio.com/2-Channel-CAN-BUS-FD-Shield-for-Raspberry-Pi/#mounting-guide)将2 Channel CAN BUS FD Shield for Raspberry Pi插入到ODYSSEY – STM32MP157C上面

- **步骤 2.** 将 CAN BUS Shield V2 插入 Seeeduino V4.2

- **步骤 3.** 使用杜邦线将2 Channel CAN BUS FD Shield for Raspberry Pi将CAN-BUS Shield V2进行连接

|2 Channel CAN BUS FD Shield for Raspberry Pi|CAN-BUS Shield V2|
|:----:|:------:|
|CAN_0_L|CANL|
|CAN_0_H|CANH|

- **步骤 4.** 将ODYSSEY – STM32MP157C 和Seeeduino V4.2供电

**依赖项安装**

- **步骤 1.** 安装`python`的相关环境

```bsah
sudo apt-get update
sudo apt-get install python3 python3-distutils python3-pyqt5  python3-pip python3-numpy -y
sudo pip3 install python-can
git clone --depth=1 https://github.com/pyqtgraph/pyqtgraph.git
cd ~/pyqtgraph
sudo python3 setup.py install
```
- **步骤 2.** 安装`git`

```bsah
sudo apt-get install git -y
```

- **步骤 3.** 安装`make`相关环境

```bsah
sudo apt-get install make device-tree-compiler gcc -y
```

### 软件安装

**安装CAN-HAT和LCD驱动**

- **步骤 1.** 检测当前linux的内核版本并安装对应的头文件

```bash
dpkg -l | grep linux
sudo apt-get install linux-headers-4.19.9-stm32-r1 -y
```

- **步骤 2.** 从github上面获取`seeed-linux-dtverlays`编译并安装对应的驱动

```bash
git clone https://github.com/Seeed-Studio/seeed-linux-dtverlays
cd seeed-linux-dtverlays
make && make install_stm32mp1
sudo mkdir -p /lib/modules/4.19.9-stm32-r1/kernel/drivers/net/can/spi/
cd ~/seeed-linux-dtverlays/modules/mcp25xxfd
make && sudo make install
```

- **步骤 3.** 将编译好的`dtbo`文件加载到`/boot/uEnv.txt`中,重启使其生效.

```bash
sudo echo uboot_overlay_addr0=/lib/firmware/stm32mp1-seeed-lcd-01-overlay.dtbo >> /boot/uEnv.txt
sudo echo uboot_overlay_addr1=/lib/firmware/stm32mp1-MCP2517FD-can0-overlay.dtbo >> /boot/uEnv.txt
sudo reboot
```
- **步骤 4.** 使用`dmesg`查看设备是否安装成功，安装成功会出现下面的信息.
```bash
debian@npi:~$ dmesg | grep spi
[    1.057609] spi_stm32 44009000.spi: driver initialized
[    9.852726] mcp25xxfd spi0.0: Linked as a consumer to regulator.6
[    9.966510] mcp25xxfd spi0.0: MCP2517 successfully initialized.

debian@npi:~$ ifconfig -a
can0: flags=128<NOARP>  mtu 16
        unspec 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00  txqueuelen 10  (UNSPEC)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```
**配置CAN-HAT和LCD**

- **步骤 1.** 配置`can-bus`

```bash
sudo ip link set can0 up type can bitrate 500000 dbitrate 8000000 restart-ms 1000 berr-reporting on fd on
sudo ifconfig can0 txqueuelen 65536

debian@npi:~$ ip -details link show can0
3: can0: <NOARP,UP,LOWER_UP,ECHO> mtu 16 qdisc pfifo_fast state UNKNOWN mode DEFAULT group default qlen 10
    link/can  promiscuity 0 minmtu 0 maxmtu 0
    can state ERROR-ACTIVE (berr-counter tx 0 rx 0) restart-ms 0
          bitrate 500000 sample-point 0.875
          tq 25 prop-seg 34 phase-seg1 35 phase-seg2 10 sjw 1
          mcp25xxfd: tseg1 2..256 tseg2 1..128 sjw 1..128 brp 1..256 brp-inc 1
          mcp25xxfd: dtseg1 1..32 dtseg2 1..16 dsjw 1..16 dbrp 1..256 dbrp-inc 1
          clock 40000000numtxqueues 1 numrxqueues 1 gso_max_size 65536 /gso_max_segs 65535
```

- **步骤 2.** 配置`lcd`环境

```bash
export QT_QPA_PLATFORM=linuxfb:fb=/dev/fb0
```

### 运行Demo

在`ODYSSEY – STM32MP157C`上面运行下面的代码

```bash
cd ~
git clone https://github.com/SeeedDocument/Seeed-NPi-STM32MP157C.git
cd ~/Seeed-NPi-STM32MP157C/examples
python3 QtViewerForStm32p1.py
```
在`Seeeduino V4.2`上面运行[CanBus_SendForArduino.ino](https://github.com/SeeedDocument/Seeed-NPi-STM32MP157C/blob/master/examples/CanBus_SendForArduino.ino).


## 资源下载
-----
- **[PDF]** [STM32MP157C Datasheet](https://github.com/SeeedDocument/Seeed-NPi-STM32MP157C/raw/master/Hardware/stm32mp157c.pdf)
- **[SCH]** [Seeed STM32MP157C SOM](https://github.com/SeeedDocument/Seeed-NPi-STM32MP157C/raw/master/Hardware/Seeed%20SoM%20-%20STM32MP157C%20v1.0_191212.pdf)
- **[SCH]** [Seeed STM32MP157C NPi](https://github.com/SeeedDocument/Seeed-NPi-STM32MP157C/raw/master/Hardware/Seeed%20NPi%20-%20STM32MP157C%20v1.0_191212.pdf)

## 技术支持

您可以将技术问题发送到 [forum](http://forum.seeedstudio.com/). <br /><p style="text-align:center"><a href="https://www.seeedstudio.com/act-4.html?utm_source=wiki&utm_medium=wikibanner&utm_campaign=newproducts" target="_blank"><img src="https://github.com/SeeedDocument/Wiki_Banner/raw/master/new_product.jpg" /></a></p>