#Ficheiro que 

import socket
from query import Query


class Cliente_UDP:

    #m = Query()
    #bytesToSend = str.encode(m.le_linha("/home/rogan/Desktop/CC/trabalho/CC/G2/entrada/query.txt"))

    #serverAddressPort = ((socket.gethostbyname(socket.gethostname()), 20001))
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.connect((socket.gethostbyname(socket.gethostname()), 20001))
    print(f"[CONNECTED] Cliente connected")
    
    connected = True
    while connected:
        msg = input("> ")
        
        client.send(msg.encode('utf-8'))
        if msg == "!DISCONNECT":
            connected = False
        else:
            msg = client.recv(1024).decode('utf-8')
            print(f"[MESSAGE RECEIVED FROM SERVER]\n{msg}")

    
    
    

    