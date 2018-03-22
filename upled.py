#!/usr/bin/python3

import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(6, gpio.IN)
gpio.output(6,1)
time.sleep(5)
gpio.cleanup()
