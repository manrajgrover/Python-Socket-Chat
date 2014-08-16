from socket import *

HOST = 'localhost'
PORT = 8000
s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    message = raw_input("Your Message: ")
    s.send(message)
    print "Awaiting reply"
    reply = s.recv(1024)
    print "Received ", repr(reply)
s.close()
