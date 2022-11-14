#utilizo este ficheiro mais para guardar potencial codigo, 

from writer import Writer

w = Writer()
w.escreve_log("/home/rogan/Desktop/CC/trabalho/CC/G2/entrada/log.txt")

from trabalho.CC.G2.src.query import Message

m = Message()
m.parse_message_condense("/home/rogan/Desktop/CC/trabalho/CC/G2/entrada/query.txt")
print(m)

class Cliente_UDP:
    def __init__(self):
        self.ip="127.0.0.1"
        self.porta = 20001
        
    def enviar_mensagem(self, mensagem):
            
        bytesToSend = str.encode(mensagem)

        serverAddressPort = (self.ip, self.porta)
        bufferSize = 1024

        # Create a UDP socket at client side
        UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

        # Send to server using created UDP socket
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)

        msgFromServer = UDPClientSocket.recvfrom(bufferSize)

        msg = "Message from Server {}".format(msgFromServer[0])

        print(msg)
        
        
import socket

class Server_UDP:
    def __init__(self):
        self.ip = "127.0.0.1"
        self.porta = 20001
        
    def conectar(self):
        bufferSize = 1024

        msgFromServer = "Hello UDP Client"
        bytesToSend = str.encode(msgFromServer)

        # Create a datagram socket
        UDPServer = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

        # Bind to address and ip
        UDPServer.bind((self.ip, self.porta))

        print("UDP server up and listening")

        # Listen for incoming datagrams
        while(True):

            (msg,add) = UDPServer.recvfrom(bufferSize)

            clientMsg = "Message from Client:{}".format(msg)
            clientIP  = "Client IP Address:{}".format(add)
            
            print(clientMsg)
            print(clientIP)

            # Sending a reply to client
            UDPServer.sendto(bytesToSend, add)