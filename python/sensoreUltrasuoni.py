import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24

print("Running...")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False) # accendo il sensore
time.sleep(2)

try:
	while(True):
		GPIO.output(TRIG, True)
		time.sleep(0.00001) # invio del segnale
		GPIO.output(TRIG, False)

		while(GPIO.input(ECHO) == 0):
    			pulse_start = time.time()

		while(GPIO.input(ECHO) == 1):
    			pulse_end = time.time()

		pulse_duration = pulse_end - pulse_start

		distance = pulse_duration * 17150
		distance = round(distance, 2)
		print(f"Distanza: {distance}cm")
		time.sleep(3)
except(KeyboardInterrupt):
	print("CTRL+C pressed, quitting...")
	GPIO.cleanup()