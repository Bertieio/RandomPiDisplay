# Copyright (c) 2012 Matthew Kirk
# Licensed under MIT License, see
# http://www.cl.cam.ac.uk/freshers/raspberrypi/tutorials/temperature/LICENSE
# Edited to add database support 2014 Bertie Scott to be used under the same licence as above
# https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/temperature/

import MySQLdb
import time
import os, glob

# Login information contained below should be kept secure
os.system("sudo modprobe w1-therm")
os.system("sudo modprobe w1-gpio")
while True:
	Start = time.time()
	db = MySQLdb.connect(host="",	# Your host, usually localhost
		user="",		# Your username
		passwd="",		# Your password
		db="")			# Name of the data base

	cur = db.cursor() 
	SQLQ = "INSERT INTO TBL_Temp(Time, Temp, CPUTemp) VALUES (%s, %s, %s)"
	tfile = open(glob.glob("/sys/bus/w1/devices/w1_bus_master1/"+"28*")[0]+"/w1_slave")	# Auto-finds your device
	text = tfile.read()
	tfile.close()
	temperature_data = text.split()[-1]
	temperature = float(temperature_data[2:])/1000.0
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
	End = time.time()
	time.sleep(600-(End-Start))	# Loops every 600 seconds, depending on how long it took to execute
