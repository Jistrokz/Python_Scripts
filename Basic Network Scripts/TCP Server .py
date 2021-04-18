import socket
import threading

BindIP = "0.0.0.0"
BindPort = 99999

server - socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((BindIP,BindPort))

#This is for our client handling thread
def HandleClient(ClientSocket):

    #Print what the client sends
    request = ClientSocket.recv(4096)

    print "[*] %s" % request

    #send back a packet

    ClientSocket.send("ACK!")

    ClientSocket.close()

while True:

    client , addr = server.accept()
    print "[*] Acceptewd Conenction from: %s:%d" % (addr[0],addr[1])

    #spin up our client thread to handle incoming data

    ClientHandler = threading.Thread(target=HandleClient,args=(client,))
    ClientHandler.start