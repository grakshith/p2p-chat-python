#! /usr/bin/env python

import socket
import sys
import time
import threading
import select, signal
import traceback
class Server(threading.Thread):
    def initialise(self,receive):
        self.receive=receive
    def run(self):
        lis=[]
        lis.append(self.receive)
        while 1:
            read,write,err=select.select(lis,[],[])
            for item in read:
                try:
                    s,addr=item.recvfrom(1024)
                    if s!='':
                        chunk=s                
                        print str('\n>>>')+':'+chunk
                except:
                    traceback.print_exc(file=sys.stdout)
                    break

class Client(threading.Thread):    
    def connect(self,host,port):
        self.sock.connect((host,port))
    def client(self,host,port,msg):               
        sent=self.sock.sendto(msg,(host,port))           
        #print "Sent\n"
    def run(self):
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        #self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        try:
            host=raw_input("Enter the hostname\n>>")            
            port=int(raw_input("Enter the port\n>>"))
        except EOFError:
            print "Error"
            return 1
        
        print "Connecting\n"
        self.client(host,port,"!@#$!@#$%$#@!$#@!")
        #self.connect(host,port)
        print "Connected\n"
        receive=self.sock
        time.sleep(1)
        srv=Server()
        srv.initialise(receive)
        srv.daemon=True
        print "Starting service"
        srv.start()
        while 1:            
            #print "Waiting for message\n"
            msg=raw_input()
            if msg=='exit':
                break
            if msg=='':
                continue
            #print "Sending\n"
            self.client(host,port,msg)
        return(1)
if __name__=='__main__':
    try:
        print "Starting client"
        cli=Client()
        cli.setDaemon(True)    
        print "CTRL+C to terminate"
        cli.start()
        signal.pause()
    except(KeyboardInterrupt):
        print "Exiting"
        sys.exit()
