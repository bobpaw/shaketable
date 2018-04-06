import RPi.GPIO as gpio
import time

gpio.setwarnings(False)
gpio.cleanup()

gpio.setmode(gpio.BCM)

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

alive = True

def stopmotor (port):
	global alive
	alive = False
	gpio.output(sleep, gpio.HIGH)

# Setup Ports
gpio.setup([direction, step, enable, sleep, ms1, ms2, ms3], gpio.OUT)
gpio.setup([switchright, switchleft], gpio.IN)
gpio.output(direction, gpio.HIGH)
gpio.output(step, gpio.LOW)
gpio.output(enable, gpio.HIGH)

gpio.add_event_detect(switchright, gpio.RISING, stopmotor, 20)
gpio.add_event_detect(switchleft, gpio.RISING, stopmotor, 20)
gpio.output([ms1,ms2,ms3], gpio.LOW)

def set_step(step, ports):
	if not isinstance(step, str):
		return False
	if not isinstance(step, list):
		return False
	if step == "full":
		gpio.output(ports, gpio.LOW)
	elif step == "half":
		gpio.output(ports[0], gpio.HIGH)
		gpio.output(ports[1:], gpio.LOW)
	elif step == "quarter":
		gpio.output(ports[0], gpio.LOW)
		gpio.output(ports[1:], gpio.HIGH)
	elif step == "eighth":
		gpio.output(ports[:1], gpio.HIGH)
		gpio.output(ports[2], gpio.LOW)
	elif step == "sixteenth":
		gpio.output(ports[:1], gpio.LOW)
		gpio.output(ports[2], gpio.HIGH)
	return True

onoff = 0
set_step("full", [ms1,ms2,ms3])
try:
	while True:
		onoff ^= 1
		if onoff == 1:
			gpio.output(step, gpio.HIGH)
		else:
			gpio.output(step,gpio.LOW)
		time.sleep(.05)
except KeyboardInterrupt:
	pass
gpio.cleanup()
