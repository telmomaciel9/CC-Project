import socket
from cache import Cache
from parser_config import Parser_Config
from logs import Logs
from query import Query
import threading
import sys
import time

class SS:
    
    def __init__(self):
        self.dirConfig = sys.argv[1]
        self.ipPorta = sys.argv[2].split(":")
        self.ip = self.ipPorta[0]
        self.porta = int(self.ipPorta[1])
        if(len(sys.argv)==5):
            self.timeout = sys.argv[3]
            self.debug = sys.argv[4]
        if(len(sys.argv)==4):
            self.debug = sys.argv[3]
        if(len(sys.argv)==3):
            self.debug = ""
        self.ssConfig = Parser_Config(self.dirConfig)    
        self.ssConfig.parse_Config()
        self.logs = Logs(self.ssConfig.dir_logLocal,self.ssConfig.dir_logAll,self.debug)    
        self.ssConfig.parse_Config()
        self.logs.EV("conf-file-read", self.dirConfig)
        self.logs.EV("log-file-create", self.ssConfig.dir_logLocal)
        self.ssCache = Cache()
        self.query = Query()
        self.refresh = 0;
        self.retry = 0;
        self.expire = 0;
        
        
    def getRefresh(self):
        for coluna in self.ssCache.mat:
            if coluna[1] == "SOAREFRESH":
                self.refresh = int(coluna[2])
                
    def getRetry(self):
        for coluna in self.ssCache.mat:
            if coluna[1] == "SOARETRY":
                self.retry = int(coluna[2])
                
    def getExpire(self):
        for coluna in self.ssCache.mat:
            if coluna[1] == "SOAEXPIRE":
                self.expire = int(coluna[2])
        
    def conecta_sp(self):
        while True:
            print("[SERVER TCP MODE] - STARTING...")
            ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ss.connect((self.ip , self.porta))
            print(f"[SS] - SERVER CONNECTED")
            #manda a mensagem do dominio
            msg = self.ssConfig.dominio
            print(f"[SS] - SENDING THIS MESSAGE:\n -> {msg}")
            ss.send(msg.encode('utf-8'))
            self.logs.QR_QE(False, str(self.ipPorta), self.ssConfig.dominio )
            
            #recebe a mensagem do sp (a dizer o numero de linhas)
            msg = ss.recv(1024).decode('utf-8')
            nLinhas = int(msg)
            print(f"[SS] - RECEIVED THIS MESSAGE:\n -> {msg}")
            self.logs.RP_RR(True,str(self.ipPorta), self.ssConfig.dominio)
            ficheiro = []
            start = time.time()
            bytesReceived = 0
            if nLinhas < 64000 :
            #envia mensagem ao sp a dizer que aceita
                msg = "ACCEPT"
                print(f"[SS] - SENDING THIS MESSAGE:\n -> {msg}")
                ss.send(msg.encode('utf-8'))
                
                flag = True
                while flag:
                    msg = ss.recv(1024).decode('utf-8')
                    lista_div = msg.split('\n')
                    for palavra in lista_div:
                        if palavra != "" and not("#" in palavra):
                            ficheiro.append(palavra)
                            bytesReceived+=len(palavra)
                            
                    if(len(ficheiro)==nLinhas):
                        flag= False
            self.ssCache.reg_cache3(ficheiro)
            end = time.time()
            self.logs.ZT(str(self.ipPorta),"SS", str(float(end-start)),str(bytesReceived))
            msg = "DISCONNECT"
            print(f"[SS] - SENDING THIS MESSAGE:\n -> {msg}")
            ss.send(msg.encode('utf-8'))
            self.getRetry()
            ss.close()
            self.logs.EV("end-of-connection")
            
            time.sleep(self.retry)
            
                
            #conecta = False
        
        
        
    def conecta_cliente(self):
        print("[SERVER UDP MODE] - STARTING...")
        serverUDP = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        serverUDP.bind((self.ip, self.porta))

        print("[SERVER UDP MODE] - LISTENING...")

        while True:
            (msg,add) = serverUDP.recvfrom(1024)
            self.query.parse_message_condense(msg.decode('utf-8'))
            self.logs.QR_QE(True, str(add), self.query.query_info_name + " " + self.query.query_info_type)

            clientMsg = "Message from Client:\n -> {}  ".format(msg.decode('utf-8'))

            bytesToSend = str.encode(self.query.origina_resposta(self.ssCache,self.query,clientMsg))

            clientIP  = "Client IP Address: {}".format(add)

            print(clientMsg)
            print(clientIP)

            # Sending a reply to client
            serverUDP.sendto(bytesToSend, add)
            self.logs.RP_RR(True,str(add),  self.query.query_info_name + " " + self.query.query_info_type)
            
if __name__ == "__main__":
    
    ss = SS()
    
    t1 = threading.Thread(target = ss.conecta_sp)
    t2 = threading.Thread(target = ss.conecta_cliente)
    t1.run()
    t2.start()

    #print(ss.ssCache)
