#!/user/bin/env python
#Program:
#	shutdown the Raspberry pi with a button
#History:
#	2014.8.3   First Release    HandcraftCavon

import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

while True:
	in_value = GPIO.input(11)
	if in_value == True:
		time.sleep(3)
		in_value = GPIO.input(11)
		if in_value == True:
			os.system('sudo poweroff')