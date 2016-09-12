import time
import RPi.GPIO as GPIO


SENSOR = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(SENSOR, GPIO.IN)

while True:
    time.sleep(0.5)
    if (GPIO.input(SENSOR)):
        print('Pin is high')
    else:
        print('Pin is low')


