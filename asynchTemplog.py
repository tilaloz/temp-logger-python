# -*- coding: utf-8 -*-
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
        "Sensor" + sensor.id: []
        for sensor in W1ThermSensor.get_available_sensors()
    })

    #append to each of the lists
    for sensor in W1ThermSensor.get_available_sensors():
        row = pd.DataFrame(
                {"Sensor" + sensor.id: 
                sensor.get_temperature(Unit.DEGREES_F) 
                }, index=[datetime.now()])
        pd.concat([temperature_log, row], axis=1)
        print(temperature_log)

    while (True):
        row = pd.DataFrame(
                {"Sensor" + sensor.id: 
                (value := sensor.get_temperature(W1ThermSensor.DEGREES_F))
                for sensor in W1ThermSensor.get_available_sensors()
                if abs(value - temperature_log["Sensor" + sensor.id]) > LSB
                }, index=[datetime.now()])
        pd.concat([temperature_log, row], axis= 1)

        
        time.sleep(6)

except KeyboardInterrupt:
    row = pd.DataFrame(
                {f"Sensor{sensor.id}": 
                sensor.get_temperature(W1ThermSensor.DEGREES_F) 
                }, index=[datetime.now()])
    pd.concat([temperature_log, row],axis=1)
finally:
    for column in temperature_log:
        temperature_log[column].dropna().to_csv(temperature_log.index[0].strftime('%Y%m%d%H%M%S') + '_' + sensor.id + '_tempLogInF.csv')
    # print "Done Logging Temp"
    
