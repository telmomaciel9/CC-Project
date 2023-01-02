from cache import Cache
from parser_db import Parser_BD
from parser_config import Parser_Config
from query import Query
from parser_st import Parser_ST
from logs import Logs
import threading
import socket
import os
import sys
import time


class SP:
    
    def __init__(self):
        self.dirConfig = sys.argv[1]
        aux = sys.argv[2].split(":")
        self.ip = aux[0]
        self.porta = int(aux[1])
        if(len(sys.argv)==5):
            self.timeout = sys.argv[3]
            self.debug = sys.argv[4]
        if(len(sys.argv)==4):
            self.debug = sys.argv[3]
        self.srvConfig = Parser_Config(self.dirConfig)
        self.srvConfig.parse_Config()
        self.logs = Logs(self.srvConfig.dir_logLocal,self.srvConfig.dir_logAll, self.debug)
        self.logs.EV("conf-file-read", self.dirConfig)
        self.logs.EV("log-file-create", self.srvConfig.dir_logLocal)
        self.srvCache = Cache()
        self.srvBD = Parser_BD(self.srvConfig.dir_bd)
        self.srvBD.parse_db(self.srvCache)
        self.logs.EV("database-file-read", self.srvConfig.dir_bd)
        self.srvST_list = Parser_ST(self.srvConfig.dir_ST)
        

    def cliente(self):
        print("[SERVER UDP MODE] - STARTING...")
        serverUDP = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        serverUDP.bind((self.ip, self.porta))		
	
        print("[SERVER UDP MODE] - LISTENING...")
        
        while True:
            query = Query()
            (msg,add) = serverUDP.recvfrom(1024)
            query.parse_message_condense(msg.decode('utf-8'))
            self.logs.QR_QE(True, str(add), query.query_info_name + " " + query.query_info_type)
            
            clientMsg = "Message from Client:\n -> {}  ".format(msg.decode('utf-8'))
            res=query.origina_resposta(self.srvCache,query)
            bytesToSend = str.encode(res)
            
            clientIP  = "Client IP Address: {}".format(add)
            
            print(clientMsg)
            print(clientIP)
            
            print(res)
            
            # Sending a reply to client
            serverUDP.sendto(bytesToSend, add)
            self.logs.RP_RR(True,str(add),  query.query_info_name + " " + query.query_info_type)

    def ss(self):
        print("[SERVER TCP MODE] - STARTING...")
        serverTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        serverTCP.bind((self.ip,self.porta))
        
        serverTCP.listen()
        print("[SERVER TCP MODE] - LISTENING...")
                    
        nTransDone = 0
                    
        while True:
            conn, addr = serverTCP.accept()
            print(f"[NEW CONNETION] {addr} CONNECTED.")
            msg = conn.recv(1024).decode('utf-8')
            print(f"[SP] - Message receive:\n -> {msg}")
            self.logs.QR_QE(True, addr)
            if msg == self.srvConfig.dominio:
                msg = str(len(self.srvBD.linhas))
                conn.send(msg.encode('utf-8'))
                self.logs.RP_RR(False, str(addr))
            msg = conn.recv(1024).decode('utf-8')
            print(f"[SP] - Message receive:\n -> {msg}")
            
            bytesSent = 0
            if msg == "ACCEPT":
                
                start = time.time()
                for i in range(len(self.srvBD.linhas)):
                    print(i+1)
                    msg = self.srvBD.linhas[i]
                    print(f"[SP] - SENDING MESSAGE:\n -> {msg}")
                    conn.send(bytes(msg,'utf-8'))
                    bytesSent+=len(msg)
                end =time.time()
                self.logs.ZT(str(addr),"SP", str(float(end-start)),str(bytesSent))     
            msg = conn.recv(1024).decode('utf-8')
            print(f"[SP] - Message receive:\n -> {msg}")
            if(msg.upper() == "DISCONNECT"):
                nTransDone = nTransDone + 1
                conn.close()  
            
        self.logs.EV("end-of-connection")
        
if __name__ == "__main__":
    srv = SP()
    #print(srv.srvCache)
    t1 = threading.Thread(target = srv.ss)
    t2 = threading.Thread(target = srv.cliente)
        
    
    t1.start()
    t2.start()
