#Ficheiro que 

import socket
from query import Query

class Cliente_UDP:

    m = Query()
        
    bytesToSend = str.encode(m.le_linha("/home/rogan/Desktop/CC/trabalho/CC/G2/entrada/query.txt"))

    serverAddressPort = ("127.0.0.1", 20001)
    bufferSize = 1024

    # Create a UDP socket at client side
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # Send to server using created UDP socket
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)

    msgFromServer = UDPClientSocket.recvfrom(bufferSize)

    print(msgFromServer[0])
    
    UDPClientSocket.close()