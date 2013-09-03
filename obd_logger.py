#!/usr/bin/python
import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
libdir = os.path.join(currentdir,"lib","pyobdlib")
sys.path.insert(0, libdir)

import platform
from datetime import datetime
import time
import serial
import pyobdlib.io
import pyobdlib.sensors
from pyobdlib.utils import scan_serial


LOG_DIR = "logs"
PORTNAME = "/dev/ttyUSB0"
LOG_SENSORS = ["rpm", "speed", "load", "temp", "intake_air_temp", "engine_time", "fuel_rail_pressure", "bar_pressure", "control_module_voltage", "accelerator_pos_D" ]

sensor_idxs = []

filetime = datetime.now()
filename = os.path.join(currentdir, LOG_DIR, "obd-" + filetime.strftime("%Y%m%d_%H%M%S") + ".csv")
log_file = open(filename, "w", 128)

try:
	log_file.write("time," + ",".join(LOG_SENSORS) + "\n");
	
	# Set up OBD port
	port = pyobdlib.io.OBDDevice(PORTNAME, None, 2, 2)
	if port.state == 0:
		port.close()
		port = None
		raise Exception("Cannot connect to %s" % PORTNAME)
		
	for sensor_sname in LOG_SENSORS:
		for index, e in enumerate(pyobdlib.sensors.SENSORS):
			if sensor_sname == e.shortname:
				sensor_idxs.append(index)
				print "Logging item: "+e.name
				break
		
	# Logging
	print "Logging started"
	
	while True:
		timestamp = datetime.now()
		
		results = {}
		results["timestamp"] = str(timestamp)
		logstr = str(timestamp)
		for index in sensor_idxs:
			(name, value, unit) = port.sensor(index)
			logstr += "," + str(value)
			results[pyobdlib.sensors.SENSORS[index].shortname] = value

		logstr += "\n"
		log_file.write(logstr)
			
		# Sleep for a moment, as it is REALLY fast
		time.sleep(5)
	
finally:
	print "Finished"
	log_file.close()
	port.close()





