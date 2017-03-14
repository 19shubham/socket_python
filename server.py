import socket
#define server ip address and port no.(socket address)
ip='127.0.0.1'
port=5000
#defining size of a buffer
size=1024

#creating a socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("we created a socket")

#connecting to a server
s.bind((ip,port))
print("connected to client")

#start listening
#20 no. of clients at a time
s.listen(20)
print("waiting for a connection")

#wait for a connection
while True:
	#accept connection
	conn,addr=s.accept()
	print("connected with"+addr[0]+" " +str(addr[1]))

	#get message from the client
	msg=conn.recv(size)
	#check if there is a msg
	if not msg:
		break;

	ser_msg='Hi from the server...'
	#send msg to the client
	conn.send(ser_msg);

s.close();