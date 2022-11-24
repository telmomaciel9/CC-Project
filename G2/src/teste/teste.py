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
 
import socket
import threading
 
def handle_client(conn,addr):
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
 
def cliente():
    print("[SERVER UDP MODE] - STARTING...")
    serverTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    serverTCP.bind((socket.gethostbyname(socket.gethostname()),20001))
    
    serverTCP.listen()
    print("[SERVER UDP MODE] - LISTENING...")
    
    while True:
        conn, addr = serverTCP.accept()
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}")
        
def handle_ss(conn,addr):
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
 
def ss():
    print("[SERVER TCP MODE] - STARTING...")
    serverUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    serverUDP.bind((socket.gethostbyname(socket.gethostname()),20001))
    
    serverUDP.listen()
    print("[SERVER TCP MODE] - LISTENING...")
    
    while True:
        conn, addr = serverUDP.accept()
        thread = threading.Thread(target=handle_ss, args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}")        

def main():
    t1 = threading.Thread(target = cliente)
    t2 = threading.Thread(target = ss)
    
    t1.run()
    t2.run()
    
if __name__ == "__main__":
    main()

with open("ficheiroGrande", "a") as f:
    for i in range(1400):
        f.write("ola\n")
               

               
import datetime
date = datetime.datetime.now()
data_formatada = str(date.day) + ":" + str(date.month) + ":" + str(date.year) + "." + str(date.hour) + ":" + str(date.minute) + ":" + str(date.second) + ":" + str(date.microsecond)[:-3]
print(data_formatada)               

from query import Query
import random
import sys

class Teste:

    def __init__(self):
        self.ip = ""
        self.query = Query()
        self.query.message_id = random.randint(1,65535)
        self.ip = sys.argv[1]
        self.query.query_info_name = sys.argv[2]
        self.query.query_info_type = sys.argv[3]
        if len(sys.argv) == 5:
            self.query.flags=sys.argv[4]
        
        
if __name__ == "__main__":
    t= Teste()

    print(t.query.gera_queryInterna())
"""

from sp import SP


s = SP()
print (s.srvCache)