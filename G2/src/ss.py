import socket
from cache import Cache
from parser_config import Parser_Config
from logs import Logs
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
        self.ssConfig = Parser_Config(self.dirConfig)    
        self.ssConfig.parse_Config()
        self.logs = Logs(self.ssConfig.dir_logLocal,self.ssConfig.dir_logAll,self.debug)    
        self.ssConfig.parse_Config()
        self.logs.EV("conf-file-read", self.dirConfig)
        self.logs.EV("log-file-create", self.ssConfig.dir_logLocal)
        self.ssCache = Cache()
        
    def conecta(self):
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ss.connect((self.ip, self.porta))
        print(f"[SS] - SERVER CONNECTED")
        
        conecta = True
        while conecta:
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
            if nLinhas < 65535 :
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
            ss.close()
            conecta = False
        self.logs.EV("end-of-connection")
            
if __name__ == "__main__":
    ss = SS()
    ss.conecta()
    #print(ss.ssCache)