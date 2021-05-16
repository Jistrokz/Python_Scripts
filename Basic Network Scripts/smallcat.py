#This is a Netcat substitute. In case the enviornment doesn't have netcat installed, this script can be used. 
import sys
import socket
import getopt
import threading
import subprocess

#Defining global variables

listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0

def usage ():
    print "KT's Garage Tools"
    print
    print "Usage: smallcat.py -t <Target_Host> -p <Port>"
    print "-l --listen                               - listen on [host]:[port] for incoming connections."
    print "-e --execute=file_to_run                  - Execute the given file upon receiving conenction."
    print "-c --command                              - Initialize a command shell."
    print "-u --upload=destination                   - Upon receiving connection upload a file and write to [destination]"
    print
    print
    print "Examples: "
    print "smallcat.py -t 192.168.0.1 -p 9999 -l -c"
    print "smallcat.py -t 192.168.0.1 -p 9999 -l -u=c:\\target.exe"
    print "smallcat.py -t 192.168.0.1 -p 9999 -l -e=\"cat /etc/passwd\""
    print "echo 'ABCDEFGHI' | smallcat.py -t 192.168.0.1 -p 135"
    sys.exit(0)

def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target

    if not len(sys.argv[1:]):
        usage()
    
    #read the command line options
    try:
        opts, args = getopt(sys.argv[1:],"hle:t:p:cu:",["help","listen","execute","target","port","command","uplaod"])
    
    except getopt.GetoptError as err:
        print str(err)
        usage()
    
    for o,a in opts:
        if o in ("-h", "--help"):
            usage()
        elif o in ("-l", "--listen"):
            listen = True
        elif o in ("-e", "--execute"):
            execute = a
        elif o in ("-c", "--command"):
            command = True
        elif o in ("-u", "--upload"):
            upload_destination = a
        elif o in ("-t", "--target")
            target = a
        elif o in ("-o", "--port")
            port = int(a)
        else:
            assert False, "Unhandeled Option"
    if not listen and len(target) and port  > 0:
        buffer = sys.stdin.read()
        client_sender(buffer)
    if listen:
        server_loop()
main()


