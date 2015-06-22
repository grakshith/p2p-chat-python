import socket
import sys
import thread
class Client():
    def __init__(self,sock=None):
        if sock is None:
            self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        else:
            self.sock=sock
    def connect(self,host,port):
        self.sock.connect((host,port))
    def client(self,host,port,msg):
        print "Connecting"
        self.connect(host,port)
        print "Connected"
        #msg=raw_input('')
        totalsent=0
        while totalsent<len(msg):
            sent=self.sock.send(msg[totalsent:])
            if sent ==0:
                raise RuntimeError("broken connection")
            totalsent+=sent
        self.sock.close()

def main():
    p2p=Client()
    host=raw_input("Enter the hostname\n")
    port=int(raw_input("Enter the port\n"))
    s=''
    #p2p.connect(host,port)
    while 1:     
        msg=raw_input('')
        if msg=='exit':
            break
        p2p.client(host,port,msg)
        

if __name__=="__main__":
    main()
    
