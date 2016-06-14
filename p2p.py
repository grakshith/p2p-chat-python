#! /usr/bin/env python

import socket
import sys
import time
import threading
class Server(threading.Thread):
    def run(self):
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print "Server started successfully\n"
        hostname=''
        port=51412
        self.sock.bind((hostname,port))
        self.sock.listen(1)
        print "Listening on port %d\n" %port        
        #time.sleep(2)    
        (clientname,address)=self.sock.accept()
        print "Connection from %s\n" % str(address)        
        while 1:
            chunk=clientname.recv(4096)            
            print str(address)+':'+chunk 

class Client(threading.Thread):    
    def connect(self,host,port):
        self.sock.connect((host,port))
    def client(self,host,port,msg):               
        sent=self.sock.send(msg)           
        print "Sent\n"
    def run(self):
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            host=raw_input("Enter the hostname\n>>")            
            port=int(raw_input("Enter the port\n>>"))
        except EOFError:
            print "Error"
            return 1
        
        print "Connecting\n"
        s=''
        self.connect(host,port)
        print "Connected\n"
        while 1:            
            print "Waiting for message\n"
            msg=raw_input('>>')
            if msg=='exit':
                break
            if msg=='':
                continue
            print "Sending\n"
            self.client(host,port,msg)
        return(1)
if __name__=='__main__':
    srv=Server()
    srv.daemon=True
    print "Starting server"
    srv.start()
    time.sleep(1)
    print "Starting client"
    cli=Client()
    print "Started successfully"
    cli.start()
    
    
