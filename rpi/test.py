#!/usr/bin/env python3

import time
import BME280
import VL53L0X
import pigpio
import math

SEA_LEVEL_PRESSURE = 1013.25

PIN_ELEVON_SERVO_RIGHT = 22
PIN_ELEVON_SERVO_LEFT = 23
PIN_LED = 4
PIN_GPS_TX = 18

GPS_BAUDRATE = 19200

DIFF_ELEVON_SERVO_RIGHT = 0
DIFF_ELEVON_SERVO_LEFT = 14

def get_altitude(pressure):
    return 44330 * (1.0 - math.pow(pressure / SEA_LEVEL_PRESSURE, 0.1903))


def set_elevon_servo(right, left):
    """
    right: -100 to +100
    left: -100 to +100
    servo: 700 - 1500 - 2300
    """

    if right < -100:
        right = -100
    elif right > 100:
        right = 100

    if left < -100:
        left = -100
    elif left > 100:
        left = 100

    right_servo = int(-1 * (right + DIFF_ELEVON_SERVO_RIGHT) * 6 + 1500)
    left_servo = int((left + DIFF_ELEVON_SERVO_LEFT) * 6 + 1500)

    pi.set_servo_pulsewidth(PIN_ELEVON_SERVO_RIGHT, right_servo)
    pi.set_servo_pulsewidth(PIN_ELEVON_SERVO_LEFT, left_servo)


if __name__ == "__main__":
    pi = pigpio.pi()
 
    if not pi.connected:
        exit(0)

    pi.set_mode(PIN_LED, pigpio.OUTPUT)

    pigpio.exceptions = False
    status = pi.bb_serial_read_close(PIN_GPS_TX)
    pigpio.exceptions = True

    status = pi.bb_serial_read_open(PIN_GPS_TX, GPS_BAUDRATE)
    print(status)

    for i in range(10000):
        (count, data) = pi.bb_serial_read(PIN_GPS_TX)
        print(count, data)
        time.sleep(0.01)

    #for i in range(10):
    #    pi.write(PIN_LED, i % 2)
    #    time.sleep(1)

    for i in range(1):
        set_elevon_servo(0, 0)
        time.sleep(1)
        set_elevon_servo(-100, -100)
        time.sleep(1)
        set_elevon_servo(0, 0)
        time.sleep(1)
        set_elevon_servo(100, 100)
        time.sleep(1)

        #pi.set_servo_pulsewidth(22, 1500)
        #pi.set_servo_pulsewidth(23, 1500)
        #time.sleep(1)
        #pi.set_servo_pulsewidth(22, 2300)
        #pi.set_servo_pulsewidth(23, 2300)
        #time.sleep(1)
        #pi.set_servo_pulsewidth(22, 1500)
        #pi.set_servo_pulsewidth(23, 1500)
        #time.sleep(1)
        #pi.set_servo_pulsewidth(22, 700)
        #pi.set_servo_pulsewidth(23, 700)
        #time.sleep(1)

    set_elevon_servo(0, 0)
    #pi.set_servo_pulsewidth(22, 1500)
    #pi.set_servo_pulsewidth(23, 1500)
 
    #s = BME280.sensor(pi)

    #tof = VL53L0X.VL53L0X()
    #tof.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)
 
    #for i in range(10):
    #    t, p, h = s.read_data()
    #    altitude = get_altitude(p/100.0)
    #    print("h={:.2f} p={:.1f} t={:.2f} a={:.2f}".format(h, p/100.0, t, altitude))

    #    distance = tof.get_distance()
    #    if (distance > 0):
    #        print("%d mm" % (distance))

    #    time.sleep(1.0)
 
    #s.cancel()
    #tof.stop_ranging()

    pi.stop()


