import socket
import sys
import thread
class Server():
    def __init__(self,sock=None):
        if sock is None:
            self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        else:
            self.sock=sock
    def server(self):
        print "program control is in server"
        hostname=''
        port=51412
        self.sock.bind((hostname,port))
        self.sock.listen(1)
        print "Listening on port %d" %port
        #chunks=[]
        
        
        while 1:
            (clientname,address)=self.sock.accept()
            print "Connection from %s" % str(address)
            chunk=clientname.recv(4096)
            """if not chunk:
                print"Error:Socket connection broken"
                break"""
            #chunks.append(chunk)
            print chunk
            clientname.close()
        #print ''.join(chunks)
def main():
    p2p=Server()
    p2p.server()


if __name__=="__main__":
    main()

