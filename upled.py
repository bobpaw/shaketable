#!/usr/bin/python3

import RPi.GPIO as gpio
import time
import random

def killchannel(channel):
	gpio.output(10,0)

gpio.setmode(gpio.BCM)
gpio.setup(10, gpio.OUT)
gpio.setup(9, gpio.IN)
sttime = time.time()
gpio.output(10,1)
gpio.add_event_detect(9, gpio.RISING, killchannel, 100)
sum = 0
try:
	while (1):
		sum = sum + random.random()
		print(sum)
		time.sleep(1)
except (KeyboardInterrupt):
	pass
gpio.cleanup()
