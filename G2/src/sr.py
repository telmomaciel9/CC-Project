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
import queue
import re
import pickle


class SR:
    
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
        self.queue= queue.Queue()



    def cliente(self):
        print("[SERVER UDP MODE] - STARTING...")
        serverUDP = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        serverUDP.bind((self.ip, self.porta))
            
        print("[SERVER UDP MODE] - LISTENING...")
        
        while True:
            query = Query()
            bytesToSend = "".encode('utf-8')
            
            (msg,add) = serverUDP.recvfrom(1024)
            query.parse_message_condense(msg.decode('utf-8'))
            self.logs.QR_QE(True, str(add), query.query_info_name + " " + query.query_info_type)
            
            clientIP  = "Client IP Address: {}".format(add)
            clientMsg = "Message from Client:\n -> {}  ".format(msg.decode('utf-8'))
            
            print(clientIP)
            print(clientMsg)
            
            resposta = query.origina_resposta(self.srvCache,query)
            print(resposta)
            if query.response_code==0:
                bytesToSend = resposta.encode('utf-8')
            
            elif query.response_code==1 or query.response_code==2:
                #fazer primeiro para o dd
                
                #fazer para o st
                ipPorta = self.srvST_list.sts[0].split(":")

                if len(ipPorta)== 2:
                    ip = ipPorta[0]
                    porta = int(ipPorta[1])
                elif len(ipPorta)==1:
                    porta = int(ipPorta[1])
                
                tST = threading.Thread(target=self.conectaServidor(ip,porta,msg.decode('utf-8'),self.queue))
                tST.start()
                
                stMsg=self.queue.get()
                
                primeiraLinhaAux = stMsg.split("\n")
                primeiraLinha= re.split(";|,| ",primeiraLinhaAux[0])

                if(primeiraLinha[2]==str(0) or primeiraLinha[2]==str(2)):
                    bytesToSend = str.encode(msg)
                    
                elif(primeiraLinha[2]==str(1)):
                    #faz para o sdt
                    listaIPs =[]
                    for i in range (len(primeiraLinhaAux)-1):
                        frase = re.split(";|,| ",primeiraLinhaAux[i])
                        if "ns" in frase[0]:
                            listaIPs.append(frase[2])
                    
                    i=0
                    flag = True
                    #while i<len(listaIPs):
                    ipPorta = listaIPs[i].split(":")
                    if len(ipPorta)== 2:
                        ip = ipPorta[0]
                        porta = int(ipPorta[1])
                    elif len(ipPorta)==1:
                        porta = int(ipPorta[1])
                    
                    tST = threading.Thread(target=self.conectaServidor(ip,porta,msg.decode('utf-8'),self.queue))
                    tST.start()
                    
                    stMsg=self.queue.get()
            
                    primeiraLinhaAux = stMsg.split("\n")
                    primeiraLinha= re.split(";|,| ",primeiraLinhaAux[0])
    
                    if(primeiraLinha[2]==str(0) or primeiraLinha[2]==str(2)):
                        bytesToSend = str.encode(msg)
                        flag = 0
                    elif(primeiraLinha[2]==str(1)):
                        #faz para o sub
                        #i=i+1
                        ##faz para o sdt
                        listaIPs =[]
                        for i in range (len(primeiraLinhaAux)-1):
                            frase = re.split(";|,| ",primeiraLinhaAux[i])
                            if "ns" in frase[0]:
                                listaIPs.append(frase[2])
                        
                        i=0
                        flag2 = True
                        #while i<len(listaIPs):
                        ipPorta = listaIPs[i].split(":")
                        if len(ipPorta)== 2:
                            ip = ipPorta[0]
                            porta = int(ipPorta[1])
                        elif len(ipPorta)==1:
                            porta = int(ipPorta[1])
                        
                        tST = threading.Thread(target=self.conectaServidor(ip,porta,msg.decode('utf-8'),self.queue))
                        tST.start()
                        
                        stMsg=self.queue.get()
                        print(stMsg)
                        primeiraLinhaAux = stMsg.split("\n")
                        primeiraLinha= re.split(";|,| ",primeiraLinhaAux[0])
        
                        if(primeiraLinha[2]==str(0) or primeiraLinha[2]==str(2)):
                            bytesToSend = str.encode(str(stMsg))
                            flag2 = 0

                        flag = 0
                            
    
            #Sending a reply to client
            serverUDP.sendto(bytesToSend, add)
            self.logs.RP_RR(True,str(add),  query.query_info_name + " " + query.query_info_type)

    
    def conectaServidor(self, ip, porta,query,q):
        srUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        srUDP.connect((ip, porta))
        print(f"[CONNECTED] Connected to {ip}:{porta}")
        
        srUDP.sendto(query.encode('utf-8'),(ip,porta))
        print(f"[MESSAGE SENT]\n{query}")
        msg = srUDP.recv(1024).decode('utf-8')
        q.put(msg)
        print(f"[MESSAGE RECEIVED FROM SERVER]\n{msg}")
        srUDP.close()
        

        
        
if __name__ == "__main__":
    srv = SR()
    t2 = threading.Thread(target = srv.cliente)

    t2.start()