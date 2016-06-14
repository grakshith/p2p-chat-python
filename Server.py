#! /usr/bin/env python

import socket
import sys, traceback, signal
import threading
import thread
import select
SOCKET_LIST=[]
TO_BE_SENT=[]
SENT_BY={}
class Server(threading.Thread):

    
    def init(self):
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.sock.bind(('',5535))
        #self.sock.listen(2)
        #SOCKET_LIST.append(self.sock)
        print "Server started on port 5535"

    def send_sock(self):
        return self.sock
    def run(self):
        while 1:
            #read,write,err=select.select(SOCKET_LIST,[],[],0)     
#            for sock in read:
#                if sock==self.sock:                    
#                    sockfd,addr=self.sock.accept()
#                    print str(addr)
#                    SOCKET_LIST.append(sockfd)
#                    print SOCKET_LIST[len(SOCKET_LIST)-1]
#               else:
            try:
                s,addr=self.sock.recvfrom(1024)
                if addr not in SOCKET_LIST:
                    if s == "!@#$!@#$%$#@!$#@!":
                        SOCKET_LIST.append(addr)
                elif s=='':
                    print str(addr)                           
                    continue
                else:
                    TO_BE_SENT.append(s)
                    SENT_BY[s]=(str(addr))
            except:
                print str(addr)                    
                    
            
class handle_connections(threading.Thread):
    def get_sock(self,server):
        self.sock=server.send_sock()
    def run(self):        
        while 1:
            #read,write,err=select.select([],SOCKET_LIST,[],0)
            for items in TO_BE_SENT:
                for s in SOCKET_LIST:
                    try:
                        if(str(s) == SENT_BY[items]):
                        	print("Ignoring %s"%(str(s)))
                        	continue
                        print "Sending to %s"%(str(s))
                        self.sock.sendto(str(s)+":"+items,s)                                             
                        
                    except:
                        traceback.print_exc(file=sys.stdout)
                TO_BE_SENT.remove(items)
                del(SENT_BY[items])         
                


if __name__=='__main__':
    try:
        srv=Server()
        srv.setDaemon(True)
        srv.init()
        srv.start()
        print SOCKET_LIST
        handle=handle_connections()
        handle.setDaemon(True) 
        handle.get_sock(srv)   
        handle.start()
        print "CTRL+C to terminate\n"
        signal.pause()
    except(KeyboardInterrupt):
        print "Exiting"
        sys.exit()   

