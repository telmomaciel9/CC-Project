import socket
from cache import Cache
from parser_config import Parser_Config

class SS_TCP:
    
    def __init__(self):
        self.ssCache = Cache()
        self.ssConfig = Parser_Config("/home/rogan/Desktop/CC/trabalho/CC/G2/entrada/configDomB.txt")
        self.ssConfig.parse_Config()
        
        
    def conecta(self):
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ss.connect(("127.0.0.1", 20001))
        print(f"[SS] - SERVER CONNECTED")
        
        conecta = True
        while conecta:
            #manda a mensagem do dominio
            msg = self.ssConfig.dominio
            print(f"[SS] - SENDING THIS MESSAGE:\n -> {msg}")
            ss.send(msg.encode('utf-8'))
            
            #recebe a mensagem do sp (a dizer o numero de linhas)
            msg = ss.recv(1024).decode('utf-8')
            nLinhas = int(msg)
            print(f"[SS] - RECEIVED THIS MESSAGE:\n -> {msg}")
            ficheiro = []
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
                    
                    if(len(ficheiro)==nLinhas):
                        flag= False
            self.ssCache.reg_cache3(ficheiro)
            
            msg = "DISCONNECT"
            print(f"[SS] - SENDING THIS MESSAGE:\n -> {msg}")
            ss.send(msg.encode('utf-8'))
            ss.close()
            conecta = False
            
if __name__ == "__main__":
    ss = SS_TCP()
    ss.conecta()
    #print(ss.ssCache)