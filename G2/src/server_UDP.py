import socket
from query import Query
from cache import Cache
from parser_db import Parser_BD

class Server_UDP:
    
    def __init__(self):
        self.serverCache = Cache()
        self.bd = Parser_BD("/home/rogan/Desktop/CC/trabalho/CC/G2/entrada/modeloDB.txt")
        self.query = Query()
        
    def regista_serverCache(self):
        self.bd.parse_db(self.serverCache)
                
    def origina_resposta(self, mensagem):
        out = mensagem + "\n"
        for list in self.serverCache.mat:
            if list[1] == self.query.query_info_type:
                out += str(list) +'\n'
            
        return out
    
    
             
    def inicia_comunicacao(self):    
        bufferSize = 1024
        
        # Create a datagram socket
        UDPServer = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    
        # Bind to address and ip
        UDPServer.bind(("127.0.0.1", 20001))
    
        # Listen for incoming datagrams
        while(True):
    
            (msg,add) = UDPServer.recvfrom(bufferSize)
            self.query.parse_message_condense(msg.decode('utf-8'))
            
            clientMsg = "Message from Client-{}:  ".format(msg.decode('utf-8'))
            
            msgFromServer = (self.origina_resposta(msg.decode('utf-8')))
            bytesToSend = str.encode(msgFromServer)
            
            
            clientIP  = "Client IP Address:{}".format(add)
            
            
            print(clientMsg)
            print(clientIP)
    
            # Sending a reply to client
            UDPServer.sendto(bytesToSend, add)
            
if __name__ == "__main__":
    srv = Server_UDP()
    srv.regista_serverCache()
    print(srv.serverCache)
    srv.inicia_comunicacao()
