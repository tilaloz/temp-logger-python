# -*- coding: utf-8 -*-
"""
Spyder Editor


"""
from w1thermsensor import W1ThermSensor
import logging
import time

#Set up Sensor
sensor = W1ThermSensor()

#Setup log file
logging.basicConfig(filename='temp.csv',
                    format='%(asctime)s,%(message)s',
                    filemode='w',
                    datefmt='%Y-%m-%d %H:%M:%S')

first = True

try:
    while (True):
        temp_f = sensor.get_temperature(W1ThermSensor.DEGREES_F)
        logging.warning(str(temp_f))
        print(str(temp_f))
        msg = 'Outside temperature at Harts is {0:.1f} DEG F'.format(temp_f)

        time.sleep(6)

except KeyboardInterrupt:
    print "Done Logging Temp"
    

    