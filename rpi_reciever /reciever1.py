
# -*- coding: utf-8 -*-
"""
@author     Alexander Rüedlinger <a.rueedlinger@gmail.com>
@date       31.07.2015

"""


from pi_switch import RCSwitchReceiver

receiver = RCSwitchReceiver()

receiver.enableReceive(2)

if (receiver):
    print("Receiver got")

receiver.resetAvailable()
if receiver.available():
    print("Receiver av")
num = 0

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
        receiver.resetAvailable()
