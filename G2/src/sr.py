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
        if(len(sys.argv)==3):
            self.debug = ""
        self.srvConfig = Parser_Config(self.dirConfig)
        self.srvConfig.parse_Config()
        self.logs = Logs(self.srvConfig.dir_logLocal,self.srvConfig.dir_logAll, self.debug)
        self.logs.EV("conf-file-read", self.dirConfig)
        self.logs.EV("log-file-create", self.srvConfig.dir_logLocal)
        self.srvCache = Cache()
        self.srvBD = Parser_BD(self.srvConfig.dir_bd)
        self.srvST_list = Parser_ST(self.srvConfig.dir_ST)
        self.queue= queue.Queue()

    def cliente(self):
        print("[SERVER UDP MODE] - STARTING...")
        serverUDP = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        serverUDP.bind((self.ip, self.porta))
            
        print("[SERVER UDP MODE] - LISTENING...")
        
        while True:
            query = Query()
            bytesToSend = "ERROR - NO QUERY RESPONSE FOUND".encode('utf-8')
            
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
                entraST=1
                if query.query_info_name in self.srvConfig.ip_DD:
                    f=1
                    while f:
                        ipPorta = self.srvConfig.ip_DD[query.query_info_name].split(":")
                        if len(ipPorta)== 2:
                            ip = ipPorta[0]
                            porta = int(ipPorta[1])
                        elif len(ipPorta)==1:
                            porta = int(ipPorta[1])
                        
                        tST = threading.Thread(target=self.conectaServidor(ip,porta,msg.decode('utf-8'),self.queue))
                        tST.start()
                        
                        stMsg=self.queue.get()
                        if(stMsg!=0):
                            primeiraLinhaAux = stMsg.split("\n")
                            primeiraLinha= re.split(";|,| ",primeiraLinhaAux[0])
            
                            if(primeiraLinha[2]==str(0) or primeiraLinha[2]==str(2)):
                                bytesToSend = str.encode(str(stMsg))
                                f=0
                                entraST=0
                            elif(primeiraLinha[2]==str(1)):
                                ##faz para o sdt
                                listaIPs =[]
                                for i in range (len(primeiraLinhaAux)-1):
                                    frase = re.split(";|,| ",primeiraLinhaAux[i])
                                    if "ns" in frase[0]:
                                        listaIPs.append(frase[2])
                                
                                e=0
                                flag2 = True
                                while e<len(listaIPs) and flag2:
                                    ipPorta = listaIPs[e].split(":")
                                    if len(ipPorta)== 2:
                                        ip = ipPorta[0]
                                        porta = int(ipPorta[1])
                                    elif len(ipPorta)==1:
                                        porta = int(ipPorta[1])
                                    
                                    tST = threading.Thread(target=self.conectaServidor(ip,porta,msg.decode('utf-8'),self.queue))
                                    tST.start()
                                    tST.join()
                                    stMsg=self.queue.get()
                                    if(stMsg!=0):
                                        print(stMsg)
                                        primeiraLinhaAux = stMsg.split("\n")
                                        primeiraLinha= re.split(";|,| ",primeiraLinhaAux[0])
                        
                                        if(primeiraLinha[2]==str(0) or primeiraLinha[2]==str(2)):
                                            bytesToSend = str.encode(str(stMsg))
                                            flag2 = 0
                                            f=0
                                            entraST=0
                                    elif(stMsg==0):
                                        e=e+1
                        else:
                            f=0
                        
                #fazer para o st
                if entraST:   
                    print(len(self.srvST_list.sts))
                    flag=True
                    a = 0
                    while a < len(self.srvST_list.sts) and flag:
                        ipPorta = self.srvST_list.sts[a].split(":")
                        if len(ipPorta)== 2:
                            ip = ipPorta[0]
                            porta = int(ipPorta[1])
                        elif len(ipPorta)==1:
                            porta = int(ipPorta[1])
                        
                        tST = threading.Thread(target=self.conectaServidor(ip,porta,msg.decode('utf-8'),self.queue))
                        tST.start()
                
                        stMsg=self.queue.get()        
                        if(stMsg!=0):
                            primeiraLinhaAux = stMsg.split("\n")
                            primeiraLinha= re.split(";|,| ",primeiraLinhaAux[0])
            
                            if(primeiraLinha[2]==str(0) or primeiraLinha[2]==str(2)):
                                bytesToSend = str.encode(str(stMsg))
                                flag = False
                                
                            elif(primeiraLinha[2]==str(1)):
                                #faz para o sdt
                                listaIPs =[]
                                for i in range (len(primeiraLinhaAux)-1):
                                    frase = re.split(";|,| ",primeiraLinhaAux[i])
                                    if "ns" in frase[0]:
                                        listaIPs.append(frase[2])
                                
                                i=0
                                flag1 = True
                                while i<len(listaIPs) and flag1:
                                    ipPorta = listaIPs[i].split(":")
                                    if len(ipPorta)== 2:
                                        ip = ipPorta[0]
                                        porta = int(ipPorta[1])
                                    elif len(ipPorta)==1:
                                        porta = int(ipPorta[1])
                                    
                                    tST = threading.Thread(target=self.conectaServidor(ip,porta,msg.decode('utf-8'),self.queue))
                                    tST.start()
                                    
                                    stMsg=self.queue.get()
                                    if(stMsg!=0):
                                        primeiraLinhaAux = stMsg.split("\n")
                                        primeiraLinha= re.split(";|,| ",primeiraLinhaAux[0])
                        
                                        if(primeiraLinha[2]==str(0) or primeiraLinha[2]==str(2)):
                                            bytesToSend = str.encode(str(stMsg))
                                            flag1 = 0
                                            flag = 0 
                                        elif(primeiraLinha[2]==str(1)):
                                            ##faz para o sdt
                                            listaIPs =[]
                                            for i in range (len(primeiraLinhaAux)-1):
                                                frase = re.split(";|,| ",primeiraLinhaAux[i])
                                                if "ns" in frase[0]:
                                                    listaIPs.append(frase[2])
                                            
                                            e=0
                                            flag2 = True
                                            while e<len(listaIPs) and flag2:
                                                ipPorta = listaIPs[e].split(":")
                                                if len(ipPorta)== 2:
                                                    ip = ipPorta[0]
                                                    porta = int(ipPorta[1])
                                                elif len(ipPorta)==1:
                                                    porta = int(ipPorta[1])
                                                
                                                tST = threading.Thread(target=self.conectaServidor(ip,porta,msg.decode('utf-8'),self.queue))
                                                tST.start()
                                                tST.join()
                                                stMsg=self.queue.get()
                                                if(stMsg!=0):
                                                    print(stMsg)
                                                    primeiraLinhaAux = stMsg.split("\n")
                                                    primeiraLinha= re.split(";|,| ",primeiraLinhaAux[0])
                                    
                                                    if(primeiraLinha[2]==str(0) or primeiraLinha[2]==str(2)):
                                                        bytesToSend = str.encode(str(stMsg))
                                                        flag2 = 0
                                                        flag1 = 0
                                                        flag = 0
                                                elif(stMsg==0):
                                                    e=e+1
                    
                                            flag1 = 0
                                    elif(stMsg==0):
                                        i=i+1
                                    else:
                                        flag1=0
                                else:
                                    flag=0 
                        elif stMsg==0:
                            a=a+1
                            
    
            #Sending a reply to client
            serverUDP.sendto(bytesToSend, add)
            self.logs.RP_RR(True,str(add),  query.query_info_name + " " + query.query_info_type)
    
    
    def conectaServidor(self, ip, porta,query,q):
        try:
            srUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            srUDP.connect((ip, porta))
            print(f"[CONNECTED] Connected to {ip}:{porta}")
            
            srUDP.sendto(query.encode('utf-8'),(ip,porta))
            print(f"[MESSAGE SENT]\n{query}")
            msg = srUDP.recv(1024).decode('utf-8')
            q.put(msg)
            print(f"[MESSAGE RECEIVED FROM SERVER {ip}:{porta}]\n{msg}")
            srUDP.close()
        except socket.error as exc:
            print("Caught exception socket.error: %s" %exc)
            q.put(0)

        
        
if __name__ == "__main__":
    srv = SR()
    t2 = threading.Thread(target = srv.cliente)

    t2.start()
