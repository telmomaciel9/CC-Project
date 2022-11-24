#Ficheiro que 
import sys
import socket
from query import Query
import random 

class Cliente_UDP:
    def __init__(self):
        self.query = Query()
        self.query.message_id = random.randint(1,65535)
        aux = sys.argv[1].split(":")
        self.ip = aux[0]
        self.porta = int(aux[1])
        self.query.query_info_name = sys.argv[2]
        self.query.query_info_type = sys.argv[3]
        if len(sys.argv) == 5:
            self.query.flags=sys.argv[4]
        

    def iniciaCom(self):
    #serverAddressPort = ((socket.gethostbyname(socket.gethostname()), 20001))
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client.connect((self.ip, self.porta))
        print(f"[CONNECTED] Cliente connected")
        
        
        msg = self.query.gera_queryInterna()
            
        client.send(msg.encode('utf-8'))
        msg = client.recv(1024).decode('utf-8')
        print(f"[MESSAGE RECEIVED FROM SERVER]\n{msg}")

if __name__ == "__main__":
    c = Cliente_UDP()
    c.iniciaCom()
    
    

    