# -*- coding: utf-8 -*-
"""
Spyder Editor


"""
from w1thermsensor import W1ThermSensor
import logging
import time
#from email.mime.text import MIMEText
#from email.mime.application import MIMEApplication
#from email.mime.multipart import MIMEMultipart
#import smtplib

#Setup email
#recipients = ['sahuarita.pooltemp@gmail.com']
#emaillist = [elem.strip().split(',') for elem in recipients]
#fromaddr = 'sahuarita.pooltemp@gmail.com'
#username = fromaddr
#password = 'ThisIsABurnerPassword!'
 
# Code for sending an email
#def email(subject,filename):
#    server = smtplib.SMTP('smtp.gmail.com:587')
#    server.starttls()
#    server.ehlo()
#    server.login(username,password)
#    msg = MIMEMultipart()
#    msg['Subject'] = subject
#    msg['From'] = fromaddr
#    msg['Reply-to'] = fromaddr
     
#    msg.preamble = 'Multipart massage.\n'
     
#    part = MIMEText("Hi, should be good weather for making snow. Temp Log attached")
#    msg.attach(part)
     
#    part = MIMEApplication(open(filename,"rb").read())
#    part.add_header('Content-Disposition', 'attachment', filename=filename)
#    msg.attach(part)

#    server.sendmail(msg['From'], emaillist , msg.as_string())
#    server.quit()
    

#Set up Sensor


    
#sensor = W1ThermSensor()

#Setup log file
logging.basicConfig(filename = time.strftime("%Y%m%d%H%M%S",time.localtime()) + '_tempLogInF.csv',
                    format='%(asctime)s,%(message)s',
                    filemode='w',
                    datefmt='%Y-%m-%d %H:%M:%S')
#
first = True

name_list = [];
#name_list.append("YYYYMMDDHHMMSS")

try:
    while (True):
        #initialize the list for output       
        temp_list_f = []
        for sensor in W1ThermSensor.get_available_sensors():
            #NOT SURE IF THE SENSORS ARE ALWAYS THE SAME ORDER!!!
            if first:
                #Add the sensor ID to the header
                name_list.append(sensor.id)
            temp_list_f.append(sensor.get_temperature(W1ThermSensor.DEGREES_F))
        if first:
            #add the header to the output
            print(','.join(name_list))
            logging.warning(','.join(name_list))
        #add the time to the list        
        #temp_list_f.insert(0,time.strftime("%Y%m%d%H%M%S",time.localtime()))
        #output temp_list        
        print(','.join(map(str,temp_list_f)))
        logging.warning(','.join(map(str,temp_list_f)))
        first = False
        time.sleep(6)

except KeyboardInterrupt:
    print "Done Logging Temp"
    

    