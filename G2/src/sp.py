from cache import Cache
from parser_db import Parser_BD
from parser_config import Parser_Config
from server_UDP import Server_UDP
import threading
import socket


class SP:
    
    def __init__(self):
        self.srvCache = Cache()
        self.srvBD = Parser_BD("/home/rogan/Desktop/CC/trabalho/CC/G2/entrada/modeloDB.txt")
        self.srvConfig = Parser_Config()
        self.srvST_list = ""
        
    #Faz parse da base de dados para a cache do sp    
    def regista_srvCache(self):
        self.srvBD.parse_db(self.srvCache)
        
    #Função auxiliar da função cliente    
    def handle_client(self,conn,addr):
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
     
    def cliente(self):
        print("[SERVER UDP MODE] - STARTING...")
        serverTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        serverTCP.bind((socket.gethostbyname(socket.gethostname()),20001))
        
        serverTCP.listen()
        print("[SERVER UDP MODE] - LISTENING...")
        
        while True:
            conn, addr = serverTCP.accept()
            thread = threading.Thread(target=self.handle_client, args=(conn,addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}")
            
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
        serverUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        serverUDP.bind((socket.gethostbyname(socket.gethostname()),20001))
        
        serverUDP.listen()
        print("[SERVER TCP MODE] - LISTENING...")
        
        while True:
            conn, addr = serverUDP.accept()
            thread = threading.Thread(target=self.handle_ss, args=(conn,addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}")        


        
if __name__ == "__main__":
    srv = SP()
    srv.regista_srvCache()
    t1 = threading.Thread(target = srv.cliente)
    t2 = threading.Thread(target = srv.ss)
        
    t1.run()
    t2.run()


    