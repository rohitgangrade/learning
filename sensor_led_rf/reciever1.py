
# -*- coding: utf-8 -*-
"""
@author     Alexander Rüedlinger <a.rueedlinger@gmail.com>
@date       31.07.2015

"""


from pi_switch import RCSwitchReceiver
import time
import RPi.GPIO as GPIO


LED = 16
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)






receiver = RCSwitchReceiver()

receiver.enableReceive(2)

receiver.resetAvailable()
num = 0
led_state = False

while True:
    if receiver.available():
        received_value = receiver.getReceivedValue()
        if received_value:
            num += 1
            print("Received[%s]:" % num)
            print(received_value)
            print("%s / %s bit" % (received_value, receiver.getReceivedBitlength()))
            print("Protocol: %s" % receiver.getReceivedProtocol())
            print("")
            led_state = not led_state 
            GPIO.output(LED, led_state)
            time.sleep(1.0)
        receiver.resetAvailable()
