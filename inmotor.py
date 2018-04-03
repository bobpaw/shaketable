#!/usr/bin/python3

import RPi.GPIO as gpio
import time
import random

in_pins = [18,17,27,22]
gpio.setwarnings(False)
gpio.cleanup()
gpio.setmode(gpio.BCM)
gpio.setup(in_pins, gpio.OUT)
direction = 1
way = list(range(8))
def change_dir (port):
	global way
	way.reverse()

button = 23
gpio.setup(button, gpio.IN, gpio.PUD_DOWN)

gpio.add_event_detect(button, gpio.RISING, change_dir, 20)

order = [
[0,0,0,1],
[0,0,1,1],
[0,0,1,0],
[0,1,1,0],
[0,1,0,0],
[1,1,0,0],
[1,0,0,0],
[1,0,0,1] ]

try:
	while True:
		for o in way:
			for i in range(4):
				if order[o][i] == 1:
					gpio.output(in_pins[i], gpio.HIGH)
				else:
					gpio.output(in_pins[i], gpio.LOW)
			time.sleep(.005)
except KeyboardInterrupt:
	gpio.cleanup()
