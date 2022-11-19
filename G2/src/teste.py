#ficheiro que faço testes ao codigo

"""
from cliente_UDP import Cliente_UDP
from trabalho.CC.G2.src.query import Message
from server_UDP import Server_UDP

m = Message()
m.parse_message_condense("/home/rogan/Desktop/CC/trabalho/CC/G2/entrada/query.txt")

serv = Server_UDP()
cliente = Cliente_UDP ()
serv.conectar()
cliente.enviar_mensagem(m)

from cache import Cache

c = Cache(3)

print(c)

c.reg_atualiza_cache("t1","1","1",1,"1", "FILE","VALID")
c.reg_atualiza_cache("t2","2","2",2,"2", "SP","VALID")
c.reg_atualiza_cache("t3","3","3",3,"3", "OTHERS","VALID")


print(c)

print(c.verifica_valid(1,"t1","1"))
print(c.verifica_valid(1,"t2","1"))

from myapp import MYAPP

app = MYAPP()
app.parseCommandLine()
print(app)


import datetime

date = datetime.datetime.now()
data_formatada = str(date.day) + ":" + str(date.month) + ":" + str(date.year) + "." + str(date.hour) + ":" + str(date.minute) + ":" + str(date.second) + ":" + str(round(date.microsecond,2))
print(data_formatada)


from parser_db import Parser_BD
from cache import Cache

class Teste:
    bd = Parser_BD()
    bd.parse_db("/home/rogan/Desktop/CC/trabalho/CC/G2/entrada/modeloDB.txt")
 
 """
 
import socket
import threading

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
            
def handle_cliente(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg = conn.recv(1024).decode('utf-8')
        if msg == "!DISCONNECT":
            connected = False
            
        print(f"[{addr}] {msg}")
        msg = f"Msg received: {msg}"
        conn.send(msg.encode('utf-8'))
        
    conn.close()
    
def cliente():
    print("[SERVER STARTING]")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 20001))
    server.listen()
    print(f"[SERVER LISTENING] ")
    
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_cliente, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
        
def ss():
    sp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sp.bind(("127.0.0.1",9999))
    sp.listen()
    
    while True:
        ss, add = sp.accept()
        print(f"Connected to {add}")
        print(ss.recv(1024).decode('utf-8'))
        ss.send("connected".encode('utf-8'))
        print(ss.recv(1024).decode('utf-8'))
        ss.send("end of connection".encode('utf-8'))
        ss.close()
    
def main():   
    t1 = threading.Thread(target = cliente)
    t2 = threading.Thread(target= ss)
    t1.start()
    t2.start()
    
if __name__ == "__main__":
    main()