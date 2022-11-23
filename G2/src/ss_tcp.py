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
        ss.connect((socket.gethostbyname(socket.gethostname()), 20001))
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
            if nLinhas < 65535 :
            #envia mensagem ao sp a dizer que aceita
                msg = "ACCEPT"
                print(f"[SS] - SENDING THIS MESSAGE:\n -> {msg}")
                ss.send(msg.encode('utf-8'))
                #recebe as linhas da bd
                fullMsg = ""
                flag = True
                for i in range(nLinhas):
                    msg = ss.recv(1024).decode('utf-8')
                    print(i)
                    print(f"[SS] - RECEIVED THIS MESSAGE:\n -> {msg}")
                    #if not (msg.encode('utf-8')) :
                    #    flag = False
                    
                        
                
                    
                #print(msg)

                #print(fullMsg)    
                #self.ssCache.reg_cache(msg)
                #print(f"[SS] - RECIVED THIS MESSAGE:\n -> {msg}")
            print("ola")
            
            msg = "DISCONNECT"
            print(f"[SS] - SENDING THIS MESSAGE:\n -> {msg}")
            ss.send(msg.encode('utf-8'))
            ss.close()
            conecta = False
            
if __name__ == "__main__":
    ss = SS_TCP()
    ss.conecta()
    #print(ss.ssCache)