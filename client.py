
import socket
#define client ip address and port nmber(socket address)
ip='127.0.0.1'
port=5000
#defining size of a buffer
size=1024

#creating a socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("we created a socket")

#connecting to a server
s.connect((ip,port))
print("connected to server")

#sending a message to a server
msg="hi!! My name is jaroli"
s.send(msg)
print("msg is sent to server")

#receiving data from the server
data=s.recv(size)
print data


