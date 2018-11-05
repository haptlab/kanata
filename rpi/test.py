#!/usr/bin/env python3

import time
import BME280
import VL53L0X
import pigpio
import math

SEA_LEVEL_PRESSURE = 1013.25

def get_altitude(pressure):
    return 44330 * (1.0 - math.pow(pressure / SEA_LEVEL_PRESSURE, 0.1903))


if __name__ == "__main__":
    pi = pigpio.pi()
 
    if not pi.connected:
        exit(0)
 
    s = BME280.sensor(pi)

    tof = VL53L0X.VL53L0X()
    tof.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)
 
    for i in range(10):
        t, p, h = s.read_data()
        altitude = get_altitude(p/100.0)
        print("h={:.2f} p={:.1f} t={:.2f} a={:.2f}".format(h, p/100.0, t, altitude))

        distance = tof.get_distance()
        if (distance > 0):
            print("%d mm" % (distance))

        time.sleep(1.0)
 
    s.cancel()
    tof.stop_ranging()
    pi.stop()


