import socket
import sys, traceback
import threading
import thread
import select
SOCKET_LIST=[]
TO_BE_SENT=[]
class Server(threading.Thread):

    def init(self):
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        self.sock.bind(('',5535))
        self.sock.listen(2)
        SOCKET_LIST.append(self.sock)
        print "Server started on port 5535"

    def run(self):
        while 1:
            read,write,err=select.select(SOCKET_LIST,[],[],0)            
            for sock in read:
                if sock==self.sock:                    
                    sockfd,addr=self.sock.accept()
                    print str(addr)
                    SOCKET_LIST.append(sockfd)
                    print SOCKET_LIST
                else:
                    try:
                        s=sock.recv(1024)
                        if s=='':
                            print str(sock.getpeername())                            
                            continue
                        else:
                            TO_BE_SENT.append(s)                                                      
                    except:
                        print str(sock.getpeername())                    
                    
            
class handle_connections(threading.Thread):
    def run(self):        
        while 1:
            read,write,err=select.select([],SOCKET_LIST,[],0)
            for items in TO_BE_SENT:
                for s in write:
                    try:
                        print "Sending to %s"%(str(s.getpeername()))
                        s.send(items)                                             
                        
                    except:
                        traceback.print_exc(file=sys.stdout)
                TO_BE_SENT.remove(items)                 
                


if __name__=='__main__':
    srv=Server()
    srv.init()
    srv.start()
    print SOCKET_LIST
    handle=handle_connections()    
    handle.start()   

