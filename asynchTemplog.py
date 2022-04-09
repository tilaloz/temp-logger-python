#!/usr/bin/python
#-*- coding: utf-8 -*-
"""
Spyder Editor


"""
from w1thermsensor import W1ThermSensor, Unit

import time
import pandas as pd
from datetime import datetime
import numpy as np

LSB = 0.115 #deg F

try:  
    temperature_log = pd.DataFrame({
        f"Sensor{sensor.id}": []
        for sensor in W1ThermSensor.get_available_sensors()
    })

    #append to each of the lists
    row = pd.DataFrame(
            {f"Sensor{sensor.id}": 
            sensor.get_temperature(Unit.DEGREES_F) 
            for sensor in W1ThermSensor.get_available_sensors()}, index=[datetime.now()])
    temperature_log = pd.concat([temperature_log, row])

    while (True):
        for sensor in W1ThermSensor.get_available_sensors():
            if abs(sensor.get_temperature(Unit.DEGREES_F) - float(temperature_log[f"Sensor{sensor.id}"].iat[-1])) > LSB:
                row = pd.DataFrame(
                        {f"Sensor{sensor.id}": 
                        sensor.get_temperature(Unit.DEGREES_F)
                        for sensor in W1ThermSensor.get_available_sensors()
                        }, index=[datetime.now()])
                temperature_log = pd.concat([temperature_log, row])
                print(temperature_log)
                break
        time.sleep(6)

except KeyboardInterrupt:
    row = pd.DataFrame(
                {f"Sensor{sensor.id}": 
                sensor.get_temperature(Unit.DEGREES_F) 
                }, index=[datetime.now()])
    temperature_log = pd.concat([temperature_log, row])
finally:
    temperature_log.to_csv(f"{temperature_log.index[0].strftime('%Y%m%d%H%M%S')}_Temperature_Data.csv", index_label="Time")
