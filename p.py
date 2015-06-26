import socket
import sys
import time
import threading
class Server(threading.Thread):
    """def __init__(self,sock=None):
        if sock is None:
            self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
        else:
            self.sock=sock"""
    
    def run(self):
    #self.l.acquire()
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print "program control is in server"
        hostname=''
        port=51412
        self.sock.bind((hostname,port))
        self.sock.listen(1)
        print "Listening on port %d" %port
        #chunks=[]
        time.sleep(2)
    #self.l.release()
        (clientname,address)=self.sock.accept()
        print "Connection from %s" % str(address)
        
        while 1:
            chunk=clientname.recv(4096)
            """if not chunk:
                print"Error:Socket connection broken"
                break"""
            #chunks.append(chunk)
            print chunk
            #clientname.close()
        #print ''.join(chunks)

    """def main(self):
        
        self.run()"""

class Client(threading.Thread):
    """def __init__(self,l,sock=None):
        if sock is None:
            self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.l=l
        else:
            self.sock=sock"""
    def connect(self,host,port):
        self.sock.connect((host,port))
    def client(self,host,port,msg):
        print "Connecting"
        #self.connect(host,port)
        print "Connected"
        #msg=raw_input('')
        totalsent=0
        #while totalsent<len(msg):
        sent=self.sock.send(msg)
            #"""if sent ==0:
            #    raise RuntimeError("broken connection")
            #totalsent+=sent"""
    #print "Socket closed"
        #self.sock.close()

    def run(self):
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            host=raw_input("Enter the hostname\n")
            print host
            port=int(raw_input("Enter the port\n"))
        except EOFError:
            print "Error"
            return 1
        
        
        s=''
        self.connect(host,port)
        while 1:
            #p2p=Client()
            print "Waiting for msg"
            msg=raw_input('')
            if msg=='exit':
                break
            print "Sending"
            self.client(host,port,msg)

def srvr():
    srv=Server()
    srv.start()
def client():
    cli=Client()
    cli.start()
#def printLogs()
if __name__=='__main__':
    srv=Server()
    srv.daemon=True
    srv.start()
    cli=Client()
    cli.start()
    
    
