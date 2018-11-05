# Raspberry Pi

## Pin layout

<a href="https://github.com/haptlab/uav-kanata/blob/master/images/rpi-pio-header.png?raw=true"><img src="https://github.com/haptlab/uav-kanata/blob/master/images/rpi-pio-header.png?raw=true" width="700px"></a>

|Description            |  |  | Description           |
|----------------------:|--:|:--|:----------------------|
|3.3V                   |1 |2 |5V                     |
|SDA (I2C)              |3 |4 |NC                     |
|SCL (I2C)              |5 |6 |NC                     |
|LED (Output)           |7 |8 |TWELITE TXD (HW UART)  |
|GND                    |9 |10|TWELITE RXD (HW UART)  |
|GPS RXD (SW UART)      |11|12|GPS TXD (SW UART)      |
|Main Motor PWM         |13|14|NC                     |
|Left Servoce PWM       |15|16|Right Servo PWM        |


## Installation

Enable Camera & I2C & UART

```
sudo raspi-config
```

Install some softwares

```
sudo apt-get install screen vim git tmux python3-pip i2c-tools
git config --global user.name "Your Name"
git config --global user.email [email address]
git config --global core.editor 'vim -c "set fenc=utf-8"'
git clone git@github.com:haptlab/uav-kanata.git
cd uav-kanata/rpi
pip3 install -r requirements.txt
```


## I2C Devices

### MPU9250
- 9 axis IMU sensor
- Slave address: 0x68

### VL53L0X
- ToF laser ranging sensor
- Slave address: 0x29

### BME280
- Pressure sensor
- Slave address: 0x76
 
 
## Twelite RED

PC: Parent

```
 a: set Application ID (0x01204444) 
 i: set Device ID (121=0x79) 
 c: set Channels (13,18,22) 
 x: set RF Conf (3) 
 r: set Role (0x0) 
 l: set Layer (0x1) 
 b: set UART baud (230400)
 B: set UART option (8N1) 
 m: set UART mode (T) 
 k: set Tx Trigger (sep=0x0d, min_bytes=0 dly=100[ms])
 h: set handle name [] 
 C: set crypt mode (0) 
 o: set option bits (0x00010000)
```

Rpi: Child

```
 a: set Application ID (0x01204444) 
 i: set Device ID (7=0x07) 
 c: set Channels (13,18,22) 
 x: set RF Conf (3) 
 r: set Role (0x0) 
 l: set Layer (0x1) 
 b: set UART baud (230400)
 B: set UART option (8N1) 
 m: set UART mode (T) 
 k: set Tx Trigger (sep=0x0d, min_bytes=0 dly=100[ms])
 h: set handle name [] 
 C: set crypt mode (0) 
 o: set option bits (0x00000000) 
```