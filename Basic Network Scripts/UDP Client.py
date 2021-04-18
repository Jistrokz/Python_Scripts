import socket

TargetHost = "127.0.0.1"
TargetPort = 80

#Creating a Socket object, similar to the one in TCP
#We have to change the socket type from SOCK_STREAM to SOCK_DGRM for UDP

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#send some data
#THe next step is to simply call "sendto()" by passing the data and server the data needs to be sent to.
#Because UDP is a connectionless protocol, there is no need to call "connect()" beforehand.

client.sendto("THIS IS A TEST",(TargetHost, TargetPort))

#Lastly, we have to receive the UDP data back

data, addr = client.recvfrom(4096)

print data

