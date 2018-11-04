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

## I2C Devices

### MPU9250
- 9 axis IMU sensor

### VL53L0X
- ToF laser ranging sensor

### BME280
- Pressure sensor
