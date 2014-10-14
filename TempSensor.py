# Copyright (c) 2012 Matthew Kirk
# Licensed under MIT License, see
# http://www.cl.cam.ac.uk/freshers/raspberrypi/tutorials/temperature/LICENSE
# Edited to add database support 2014 Bertie Scott to be used under the same licence as above
# https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/temperature/

import MySQLdb
import time
import os

# Login information contained below should be kept secure

while True:
	db = MySQLdb.connect(host="", #your host, usually localhost
                     user="", #your username
                      passwd="", #your password
                      db="") #name of the data base

	cur = db.cursor() 
	SQLQ = "INSERT INTO TBL_Temp(Time, Temp, CPUTemp) VALUES (%s, %s, %s)"
	tfile = open("/sys/bus/w1/devices/w1_bus_master1/28-000006222efb/w1_slave") # change 28-000006222efb to your model number 
	text = tfile.read()
	tfile.close()
	temperature_data = text.split()[-1]
	temperature = float(temperature_data[2:])
	temperature = temperature / 1000
	UTime =  int(time.time())
	CPUTempC = "/opt/vc/bin/vcgencmd measure_temp > CPUTEMP"
	os.system(CPUTempC)
	CPUFile = open("CPUTEMP")
	CPUText = CPUFile.read()
	CPUFile.close()
	TempCPU = CPUText[5:9]
	TempCPU = eval(TempCPU)
	print "TIME: " ,UTime
	print "TEMP: " ,temperature
	print "CPU TEMP: " ,TempCPU
	cur.execute(SQLQ, (UTime, temperature, TempCPU))
	db.commit()
	time.sleep(595)