from cache import Cache
from parser_db import Parser_BD
from parser_config import Parser_Config
from query import Query
import threading
import socket


class SP:
    
    def __init__(self):
        self.srvCache = Cache()
        self.srvBD = Parser_BD("/home/rogan/Desktop/CC/trabalho/CC/G2/entrada/modeloDB.txt")
        self.srvConfig = Parser_Config()
        self.srvST_list = ""
        self.query = Query()
        self.srvBD.parse_db(self.srvCache)
        self.srvConfig.parse_Config("/home/rogan/Desktop/CC/trabalho/CC/G2/entrada/configDomA.txt")
    #
        
    def origina_resposta(self, mensagem):
        out = mensagem + "\n"
        for list in self.srvCache.mat:
            if(list[1] == self.query.query_info_type or list[1] == "NS"):
                for i in range(5):            
                    out = out + str(list[i]) + " "
                out = out + "\n"
        return out
        
     
    def cliente(self):
        print("[SERVER UDP MODE] - STARTING...")
        serverUDP = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        
        serverUDP.bind(("127.0.0.1",20001))
            
        print("[SERVER UDP MODE] - LISTENING...")
        
        while True:
            (msg,add) = serverUDP.recvfrom(1024)
            self.query.parse_message_condense(msg.decode('utf-8'))
            
            clientMsg = "Message from Client-{}:  ".format(msg.decode('utf-8'))
            
            msgFromServer = (self.origina_resposta(msg.decode('utf-8')))
            bytesToSend = str.encode(msgFromServer)
            
            clientIP  = "Client IP Address:{}".format(add)
            
            
            print(clientMsg)
            print(clientIP)
    
            # Sending a reply to client
            serverUDP.sendto(bytesToSend, add)
            
            
    def handle_ss(self,conn,addr):
        print(f"[NEW CONNETION] {addr} CONNECTED.")
     
        connected = True
        while connected:
            msg = conn.recv(1024).decode('utf-8')
            if msg == "!DISCONNECT":
                connected = False
            
            print(f"[{addr}] {msg}")
            msg = f"MESSAGE RECEIVED: {msg}"
            conn.send(msg.encode('utf-8'))
        conn.close()
     
    def ss(self):
        print("[SERVER TCP MODE] - STARTING...")
        serverTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        serverTCP.bind(("127.0.0.1",20001))
        
        serverTCP.listen()
        print("[SERVER TCP MODE] - LISTENING...")
        
        while True:
            conn, addr = serverTCP.accept()
            thread = threading.Thread(target=self.handle_ss, args=(conn,addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}")        

        
if __name__ == "__main__":
    srv = SP()
    t1 = threading.Thread(target = srv.cliente)
    t2 = threading.Thread(target = srv.ss)
        
    t1.start()
    t2.start()


    