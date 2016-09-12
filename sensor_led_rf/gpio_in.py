import time
import RPi.GPIO as GPIO
from pi_switch import RCSwitchSender

sender = RCSwitchSender()
sender.enableTransmit(0) # use WiringPi pin 0


SENSOR =  7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(SENSOR, GPIO.IN)

sleep_time = 0.1

while True:
    time.sleep(sleep_time)
    if (GPIO.input(SENSOR)):
        print('Pin is high')
        sender.sendDecimal(777, 24);
    	time.sleep(10.0)
    else:
        print('Pin is low')


