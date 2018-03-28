import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

enable = 25
ms1 = 24
ms2 = 23
ms3 = 22
reset = 27
sleep = 18
step = 17
direction = 4

gpio.setup(direction, gpio.OUT)
gpio.setup(step, gpio.OUT)
gpio.setup(enable, gpio.OUT)
gpio.output(direction, gpio.HIGH);
gpio.output(step, gpio.LOW)
gpio.output(enable, gpio.HIGH)

gpio.cleanup()
