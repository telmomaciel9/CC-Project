from cache import Cache
from parser_db import Parser_BD
from parser_config import Parser_Config
from server_UDP import Server_UDP
import threading
import socket


class SP:
    #Variaveis uteis para os socket
    mode = 'utf-8'
    porta = 20001
    ip = "127.0.0.1"
    address = (ip, porta)
    
    def __init__(self):
        self.srvCache = Cache()
        self.srvBD = Parser_BD("/home/rogan/Desktop/CC/trabalho/CC/G2/entrada/modeloDB.txt")
        self.srvConfig = Parser_Config()
        self.srvST_list = ""
        
    #Faz parse da base de dados para a cache do sp    
    def regista_svrCache(self):
        self.srvBD.parse_db(self.srvCache)
        
    #Função auxiliar da função cliente    
    def handle_cliente(self,conn, addr):
        print(f"[NEW CONNECTION] {addr} connected.")
    
        connected = True
        while connected:
            msg = conn.recv(1024).decode(mode)
            
            if msg == "!DISCONNECT":
                connected = False
                
            print(f"[{addr}] {msg}")
            msg = f"Msg received: {msg}"
            conn.send(msg.encode(mode))
            
        conn.close()
    
    #Função que permite a multithreading dos clientes - UDP
    def cliente(self):
        print("[SERVER UDP MODE] - STARTING...")
        serverUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        serverUDP.bind(address)
        
        serverUDP.listen()
        print(f"[SERVER UDP MODE] - LISTENING...")
        
        while True:
            conn, addr = serverUDP.accept()
            thread = threading.Thread(target = handle_cliente, args=(conn, addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
    
    
     #Função auxiliar da função cliente    
    def handle_ss(self,conn, addr):
        print(f"[NEW CONNECTION] {addr} connected.")
    
        connected = True
        while connected:
            msg = conn.recv(1024).decode(mode)
            
            if msg == "!DISCONNECT":
                connected = False
                
            print(f"[{addr}] {msg}")
            msg = f"Msg received: {msg}"
            conn.send(msg.encode(mode))
            
        conn.close()
    
    #Função para a transferencia de zona - TCP
    def ss(self):
    
        print("[SERVER TCP MODE] - STARTING...")
        serverTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        serverTCP.bind(address)
        
        serverTCP.listen()
        print(f"[SERVER TCP MODE] - LISTENING...")
        
        while True:
            conn, addr = serverUDP.accept()
            thread = threading.Thread(target = handle_ss, args=(conn, addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
        
    def main(): 
        s = SP()
        t2 = threading.Thread(target = s.cliente)
        t3 = threading.Thread(target= s.ss)
        
        t2.start()
        t3.start()
        
    if __name__ == "__main__":
        main()


    