import time
import RPi.GPIO as GPIO


LED = 16
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)
GPIO.setup(13, GPIO.OUT)
GPIO.output(13, GPIO.LOW)
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, GPIO.LOW)


while True:
    GPIO.output(LED, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(11, GPIO.LOW)
    time.sleep(0.5)
    #GPIO.output(LED, GPIO.LOW)
    time.sleep(0.5)





