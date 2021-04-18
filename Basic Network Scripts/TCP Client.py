import socket

#Indicate where to send the data and at which port
TargetHost = "www.google.com"
TargetPort = 80

#Creating a Socket object
#We first create a socket object with the AF_INET and SOCK_STREAM parameters.
#The AF_INET parameter indicates that we are using standard IPv4 address or hostname
# and SOCK_STR indicates that this will be a TCP client. We then connect to the server

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the client
#We can now connect the client to the server and send it somer data

client.connect((TargetHost, TargetPort))

#send some data

client.send("GET / HTTP/1.1\r\nHOST: google.com\r\n\r\n")

#recvieve some data back

response = client.recv(4096)

print response