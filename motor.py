import RPi.GPIO as gpio
import time
import random

# Ensure GPIO is cleaned up, and don't warn that I'm cleaning without needing to
gpio.setwarnings(False)
gpio.cleanup()

gpio.setmode(gpio.BCM)

# List of ports
enable = 25
ms1 = 24
ms2 = 23
ms3 = 22
reset = 27
sleep = 18
step = 17
direction = 4
switchleft = 12
switchright = 20

iteration = 0
alive = True
delaytime = .01

# Interrupt to stop motor
def stopmotor (port):
	global alive
	alive = False
	print("Motor stopped")
	gpio.output(sleep, gpio.LOW)

# Function to write to driver for different microstep precisions
def set_step(step, ports):
	if not isinstance(step, str) or not isinstance(step, int):
		return False
	if not isinstance(step, list):
		return False
	if step == "full" or step == 1:
		gpio.output(ports, gpio.LOW)
	elif step == "half" or step == 2:
		gpio.output(ports[0], gpio.HIGH)
		gpio.output(ports[1:], gpio.LOW)
	elif step == "quarter" or step == 4:
		gpio.output(ports[0], gpio.LOW)
		gpio.output(ports[1:], gpio.HIGH)
	elif step == "eighth" or step == 8:
		gpio.output(ports[:1], gpio.HIGH)
		gpio.output(ports[2], gpio.LOW)
	elif step == "sixteenth" or step == 16:
		gpio.output(ports[:1], gpio.LOW)
		gpio.output(ports[2], gpio.HIGH)
	return True

# Setup Ports
gpio.setup([direction, step, reset, enable, sleep, ms1, ms2, ms3], gpio.OUT)
gpio.setup([switchright, switchleft], gpio.IN)
gpio.output(direction, gpio.HIGH)
gpio.output(step, gpio.LOW)

# Actually turn driver on
gpio.output(enable, gpio.LOW)
gpio.output(sleep, gpio.HIGH)
gpio.output(reset, gpio.HIGH)

# Add interrupts for both limit switches
gpio.add_event_detect(switchright, gpio.RISING, stopmotor, 20)
gpio.add_event_detect(switchleft, gpio.RISING, stopmotor, 20)

try:
	while True:
		iteration += 1
		# An attempt at random-ish precision changes
		if iteration % 10 == 0:
			iteration = 0
			a = [2 ** i for i in range(5)][random.randint(0, 4)]
			print(a)
			gpio.output(enable, gpio.HIGH)
			set_step(a, [ms1,ms2,ms2])
			gpio.output(enable, gpio.LOW)
		gpio.output(step, gpio.HIGH)
		time.sleep(delaytime)
		gpio.output(step,gpio.LOW)
		time.sleep(delaytime)
except KeyboardInterrupt:
	# Break for Ctrl-C
	pass
gpio.cleanup()
