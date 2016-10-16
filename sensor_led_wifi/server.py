import socket
import sys
import time
import RPi.GPIO as GPIO

LED = 16
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('192.168.1.6', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(2)


ST_RESET = 0
ST_FIRSTSENSER = 1
ST_SECONDSENSER = 2
ST_INSIDE = 3
ST_INSIDE_FIRSTSENSER = 4
ST_INSIDE_SECONDSENSER = 5

STATE = ST_RESET

while True:
    if STATE == ST_RESET:
        # Wait for a connection
        print >>sys.stderr, 'waiting for a connection in reset'
        sock.settimeout(None)
        try:
            connection, client_address = sock.accept()
            try:
                print >>sys.stderr, 'connection from', client_address

                # Receive the data in small chunks and retransmit it
                data = connection.recv(16)
                print >>sys.stderr, 'received "%s"' % data

                if data == '15':
                    STATE = ST_FIRSTSENSER
                else:
                    STATE = ST_RESET
            finally:
                # Clean up the connection
                connection.close()
        except socket.timeout:
            STATE = ST_RESET
    elif STATE == ST_FIRSTSENSER:
        # Wait for a connection
        print >>sys.stderr, 'waiting for a connection in first senser'
        sock.settimeout(10)
        try:
            connection, client_address = sock.accept()
            try:
                print >>sys.stderr, 'connection from', client_address

                # Receive the data in small chunks and retransmit it
                data = connection.recv(16)
                print >>sys.stderr, 'received "%s"' % data

                if data == '16':
                    STATE = ST_SECONDSENSER
                else:
                    STATE = ST_FIRSTSENSER
            finally:
                # Clean up the connection
                connection.close()
        except socket.timeout:
            STATE = ST_RESET
    elif STATE == ST_SECONDSENSER:
        print 'lights up'
        GPIO.output(LED, GPIO.HIGH)
        sock.settimeout(None)
        STATE = ST_INSIDE;
    elif STATE == ST_INSIDE:
        try:
            print >>sys.stderr, 'waiting for a connection inside'
            connection, client_address = sock.accept()
            try:
                print >>sys.stderr, 'connection from', client_address

                # Receive the data in small chunks and retransmit it
                data = connection.recv(16)
                print >>sys.stderr, 'received "%s"' % data

                if data == '16':
                    STATE = ST_INSIDE_FIRSTSENSER
                else:
                    STATE = ST_INSIDE
            finally:
                # Clean up the connection
                connection.close()
        except socket.timeout:
            STATE = ST_INSIDE
    elif STATE == ST_INSIDE_FIRSTSENSER:
        # Wait for a connection
        print >>sys.stderr, 'waiting for a connection in inside first senser'
        sock.settimeout(10)
        try:
            connection, client_address = sock.accept()
            try:
                print >>sys.stderr, 'connection from', client_address

                # Receive the data in small chunks and retransmit it
                data = connection.recv(16)
                print >>sys.stderr, 'received "%s"' % data

                if data == '15':
                    STATE = ST_INSIDE_SECONDSENSER
                else:
                    STATE = ST_INSIDE_FIRSTSENSER
            finally:
                # Clean up the connection
                connection.close()
        except socket.timeout:
            STATE = ST_INSIDE_FIRSTSENSER;
    elif STATE == ST_INSIDE_SECONDSENSER:
        print 'lights down'
        GPIO.output(LED, GPIO.LOW)
        sock.settimeout(None)
        STATE = ST_RESET







