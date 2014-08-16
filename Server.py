from socket import *

HOST = ''
PORT = 8000
s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1) 
conn, addr = s.accept()
print 'Connected by', addr
while True:
    data = conn.recv(1024)
    print "Received ", repr(data)
    reply = raw_input("Reply: ")
    conn.sendall(reply)
conn.close()
