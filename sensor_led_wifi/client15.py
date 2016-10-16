import socket
import sys
import time
import RPi.GPIO as GPIO

SENSOR =  7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(SENSOR, GPIO.IN)

sleep_time = 0.1



# Create a TCP/IP socket

while True:
    time.sleep(sleep_time)
    if (GPIO.input(SENSOR)):
        print('Pin is high')
        try:
	    # Connect the socket to the port where the server is listening
	    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	    server_address = ('192.168.1.6', 10000)
	    print >>sys.stderr, 'connecting to %s port %s' % server_address
	    sock.connect(server_address)

            # Send data
            message = '15'
            print >>sys.stderr, 'sending "%s"' % message
            sock.sendall(message)
        finally:
            print >>sys.stderr, 'closing socket'
            sock.close()
    	time.sleep(2.0)
    else:
        print('Pin is low')



