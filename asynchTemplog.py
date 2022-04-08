# -*- coding: utf-8 -*-
"""
Spyder Editor


"""
from w1thermsensor import W1ThermSensor

import time

#Set up Sensor


    
#sensor = W1ThermSensor()

#Setup log file
#logging.basicConfig(filename = time.strftime("%Y%m%d%H%M%S",time.localtime()) + '_tempLogInF.csv',
#                    format='%(message)s',
#                    filemode='w')
#
#first = True
LSB = 0.115 #deg F
#first = 
#name_list = [];
#name_list.append("YYYYMMDDHHMMSS")
header = 'time (YYYYMMDDHHMMSS), Temp (deg F)\n'
#this version will not work if sensors are added or removed during measurement.
try:
    #initialize the lists    
    sensors = []
    current_temp = []
    last_temp = []
    first = []
    log = []
    #append to each of the lists
    for sensor in W1ThermSensor.get_available_sensors():   
        sensors.append(sensor.id) 
        first.append(True)
        current_temp.append(sensor.get_temperature(W1ThermSensor.DEGREES_F))
        last_temp.append(sensor.get_temperature(W1ThermSensor.DEGREES_F))
        log.append(open(time.strftime("%Y%m%d%H%M%S",time.localtime()) + '_' + sensor.id + '_tempLogInF.csv','w'))
    #
    while (True):
        for sensor in W1ThermSensor.get_available_sensors():
            index = sensors.index(sensor.id)
            current_temp[index] = sensor.get_temperature(W1ThermSensor.DEGREES_F)
            screen_output = sensor.id + ',' + str(current_temp[index])
            file_output = time.strftime("%Y%m%d%H%M%S",time.localtime()) + ',' + str(current_temp[index]) + '\n'
           
            if first[index]:
                #output the header        
                log[index].write(header)
                #initialize the list for time and sensor output 
                last_temp[index] = current_temp[index]
                #output temp_list        
                print(screen_output)
                log[index].write(file_output)
                first[index] = False
            elif abs(current_temp[index]- last_temp[index]) > LSB:
                #record
                last_temp[index] = current_temp[index]
                print(screen_output)
                log[index].write(file_output)
        
        time.sleep(6)

except KeyboardInterrupt:
    for sensor in W1ThermSensor.get_available_sensors():
        index = sensors.index(sensor.id)
        current_temp[index] = sensor.get_temperature(W1ThermSensor.DEGREES_F)
        file_output = time.strftime("%Y%m%d%H%M%S",time.localtime()) + ',' + str(current_temp[index]) + '\n'
        log[index].write(file_output)
finally: # Ensure that the file is always closed.
    for file in log:
        file.close()
    print "Done Logging Temp"
    