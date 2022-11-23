from cache import Cache
from parser_db import Parser_BD
from parser_config import Parser_Config
from query import Query
import threading
import socket


class ServerTeste:
    
    def __init__(self):
        self.srvCache = Cache()
        self.srvBD = Parser_BD("/home/rogan/Desktop/CC/trabalho/CC/G2/entrada/modeloDB.txt")
        self.srvConfig = Parser_Config("/home/rogan/Desktop/CC/trabalho/CC/G2/entrada/configDomA.txt")
        self.srvST_list = ""
        self.query = Query()
        self.srvBD.parse_db(self.srvCache)
        self.srvConfig.parse_Config()
        
    def origina_resposta(self, mensagem):
        rval = ""
        aval = ""
        eval = ""
        for list in self.srvCache.mat:
            if((str(list[1]) == str(self.query.query_info_type)) and (str(list[0]) == str(self.query.query_info_name))):
                for i in range(5):            
                    rval += str(list[i]) + " "
                rval = rval + "\n"
            #authoritiesvalues
            if(str(list[0]) == self.query.query_info_name and str(list[1]) == "NS"):
                for i in range(5):            
                    aval = aval + str(list[i]) + " "
                aval = aval + "\n"
            if((str(list[1]) == "A" and "NS".lower() in list) or (str(list[1]) == "A" and self.query.query_info_type.lower() in list)):
                for i in range(5):            
                    eval = eval + str(list[i]) + " "
                eval = eval + "\n"
            
        return mensagem+rval+aval+eval
     
    def cliente(self):
        print("[SERVER UDP MODE] - STARTING...")
        serverUDP = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        
        serverUDP.bind((socket.gethostbyname(socket.gethostname()),20001))
            
        print("[SERVER UDP MODE] - LISTENING...")
        
        while True:
            (msg,add) = serverUDP.recvfrom(1024)
            self.query.parse_message_condense(msg.decode('utf-8'))
            
            clientMsg = "Message from Client:\n -> {}  ".format(msg.decode('utf-8'))
            
            msgFromServer = (self.origina_resposta(msg.decode('utf-8')))
            bytesToSend = str.encode(msgFromServer)
            
            
            clientIP  = "Client IP Address: {}".format(add)
            
            
            print(clientMsg)
            print(clientIP)
    
            # Sending a reply to client
            serverUDP.sendto(bytesToSend, add)
             
     
    def ss(self):
        print("[SERVER TCP MODE] - STARTING...")
        serverTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        serverTCP.bind((socket.gethostbyname(socket.gethostname()),20001))
        
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
        #mandar linhas para o ss
        if msg == "ACCEPT":
            file  = open("/home/rogan/Desktop/CC/trabalho/CC/G2/entrada/ficheiroGrande", "r")
            data = file.read()
            conn.send(data.encode('utf-8'))
                
        msg = conn.recv(1024).decode('utf-8')
        print(f"[SP] - Message receive:\n -> {msg}")    
        conn.close()       

        
if __name__ == "__main__":
    srv = ServerTeste()
    print(srv.srvConfig.dominio)
    t1 = threading.Thread(target = srv.cliente)
    t2 = threading.Thread(target = srv.ss)
        
    t1.start()
    t2.run()


    