from cache import Cache
from parser_db import Parser_BD
from parser_config import Parser_Config
from query import Query
from logs import Logs
import threading
import socket
import os


class SP:
    
    def __init__(self):
        self.logs = Logs()
        self.srvConfig = Parser_Config("/home/rogan/Desktop/CC/trabalho/CC/G2/entrada/modeloconfig.txt")
        self.srvConfig.parse_Config()
        self.dirLogs= "/home/rogan/Desktop/CC/trabalho/CC/G2/saida/SP - "+self.srvConfig.dominio + ".txt"
        self.logs.escreve_log(self.dirLogs, "EV", "127.0.0.1","conf-file-read  -  /CC/G2/entrada/configDomA.txt")
        self.logs.escreve_log(self.dirLogs, "EV", "127.0.0.1","logs-file - "+self.dirLogs)
        self.srvCache = Cache()
        self.srvBD = Parser_BD("/home/rogan/Desktop/CC/trabalho/CC/G2/entrada/modeloDB.txt")
        self.srvBD.parse_db(self.srvCache)
        self.logs.escreve_log(self.dirLogs, "EV", "127.0.0.1","database-file-read  - CC/G2/entrada/modeloDB.txt")
        self.srvST_list = ""
        self.query = Query()
        
        
        
     
    def cliente(self):
        print("[SERVER UDP MODE] - STARTING...")
        serverUDP = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        serverUDP.bind(("127.0.0.1",20001))
            
        print("[SERVER UDP MODE] - LISTENING...")
        
        while True:
            (msg,add) = serverUDP.recvfrom(1024)
            self.query.parse_message_condense(msg.decode('utf-8'))
            self.logs.escreve_log(self.dirLogs, "QR", str(add), self.query.message_id + " " + self.query.flags + self.query.query_info_name + " " + self.query.query_info_type)
            
            clientMsg = "Message from Client:\n -> {}  ".format(msg.decode('utf-8'))
            
            bytesToSend = str.encode(self.query.origina_resposta(self.srvCache,self.query,clientMsg))
            self.logs.escreve_log(self.dirLogs, "RP", str(add), self.query.message_id + " " + self.query.flags + self.query.query_info_name + " " + self.query.query_info_type)
            clientIP  = "Client IP Address: {}".format(add)
            
            print(clientMsg)
            print(clientIP)
    
            # Sending a reply to client
            serverUDP.sendto(bytesToSend, add)
             
     
    def ss(self):
        print("[SERVER TCP MODE] - STARTING...")
        serverTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        serverTCP.bind(("127.0.0.1",20001))
        
        serverTCP.listen(10)
        print("[SERVER TCP MODE] - LISTENING...")
        
        conn, addr = serverTCP.accept()
        print(f"[NEW CONNETION] {addr} CONNECTED.")
     
        
        msg = conn.recv(1024).decode('utf-8')
        print(f"[SP] - Message receive:\n -> {msg}")
        if msg == self.srvConfig.dominio:
            msg = str(len(self.srvBD.linhas))
            conn.send(msg.encode('utf-8'))
            
        msg = conn.recv(1024).decode('utf-8')
        print(f"[SP] - Message receive:\n -> {msg}")
        
        
        bytesSent = 0
        if msg == "ACCEPT":
            
            for i in range(len(self.srvBD.linhas)):
                print(i+1)
                msg = self.srvBD.linhas[i]
                print(f"[SP] - SENDING MESSAGE:\n -> {msg}")
                conn.send(bytes(msg,'utf-8'))
                bytesSent+=len(msg)
                
        msg = conn.recv(1024).decode('utf-8')
        print(f"[SP] - Message receive:\n -> {msg}")
        if(msg.upper() == "DISCONNECT"):
            self.logs.escreve_log(self.dirLogs, "ZT", str(addr), "SP - "+str(bytesSent))
        conn.close()       

        
if __name__ == "__main__":
    srv = SP()
    t1 = threading.Thread(target = srv.cliente)
    t2 = threading.Thread(target = srv.ss)
        
    t1.start()
    t2.run()


    