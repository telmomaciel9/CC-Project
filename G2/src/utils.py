#utilizo este ficheiro mais para guardar potencial codigo, 
'''
from trabalho.CC.G2.src.logs import Writer

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
            
            
#codigo base de dados
def __init__(self):
        self.linhas = []
        self.dominio = ""
        self.ttl = 0
        self.prefixo = ""    #o parâmetro @ é reservado para identificar um prefixo por defeito que é acrescentado sempre 
                        #que um nome não apareça na forma completa (i.e., terminado com ‘.’); o valor de TTL deve ser zero;
        self.soasp = ""      #indica o nome completo do SP do domínio
        self.soaadmin = ""   #indica o endereço de e-mail completo do administrador do domínio
        self.soaserial = ""  #valor indica o número de série da base de dados do SP do domínio
        self.soarefresh = "" #indica o intervalo temporal em segundos para um SS perguntar ao SP do domínio
        self.soaretry = ""   #indica o intervalo temporal para um SS voltar a perguntar ao SP do domínio, apos um timeout
        self.soaexpire = ""  #indica o intervalo temporal para um SS deixar de considerar a sua réplica válida
        self.ns = []         #indica o nome dum servidor que é autoritativo para o domínio indicado no parâmetro (chave) 
                             #este tipo de parâmetro suporta prioridades (value)
        
if(linha[0]!='#' or linha[0]!="\n"):
                    if(linha[0]=="@" and linha[1]=="DEFAULT"):
                        self.dominio = linha[2]
                        dom = linha[2]
                    if(linha[0]=="TTL" and linha[1] == "DEFAULT"):
                        self.ttl=linha[3]
                        ttl = linha [3]
                    if(linha[0]=="@" and linha[1]=="SOASP"):
                        self.soasp = linha[2]
                        linha[0] = self.dominio
                        linha[3] = self.ttl
                    if(linha[0]=="@" and linha[1]=="SOAADMIN"):
                        self.soaadmin = linha[2]
                        linha[0] = self.dominio
                        linha[3] = self.ttl
                    if(linha[0]=="@" and linha[1]=="SOASERIAL"):
                        self.soaserial = linha[2]
                        linha[0] = self.dominio
                        linha[3] = self.ttl
                    if(linha[0]=="@" and linha[1]=="SOAREFRESH"):
                        self.soarefresh = linha[2]
                        linha[0] = self.dominio
                        linha[3] = self.ttl
                    if(linha[0]=="@" and linha[1]=="SOARETRY"):
                        self.soaretry = linha[2]
                        linha[0] = self.dominio
                        linha[3] = self.ttl
                    if(linha[0]=="@" and linha[1]=="SOAEXPIRE"):
                        self.soaexpire = linha[2]
                        linha[0] = self.dominio
                        linha[3] = self.ttl
                    if(linha[0]=="@" and linha[1]=="NS"):
                        self.ns.append(linha[2])
                        linha[0] = self.dominio
                        linha[3] = self.ttl
                    
                    
                    
                    if(linha[0]=="@" and linha[1]=="DEFAULT"):
                        self.nome = linha[2]
                    if(linha[0]=="TTL" and linha[1]=="DEFAULT"):
                        self.ttl = linha[2]
                    if(linha[1]=="SOASP"):
                        self.tipo = linha[1]
                        self.valor = linha[2]                
                    if(linha[1]=="SOAADMIN"):
                        self.tipo = linha[1]
                        self.valor = linha[2] 
                    if(linha[1]=="SOASERIAL"):
                        self.tipo = linha[1]
                        self.valor = linha[2] 
                    if(linha[1]=="SOAREFRESH"):
                        self.tipo = linha[1]
                        self.valor = linha[2] 
                    if(linha[1]=="SOARETRY"):
                        self.tipo = linha[1]
                        self.valor = linha[2] 
                    if(linha[1]=="SOAEXPIRE"):
                        self.tipo = linha[1]
                        self.valor = linha[2] 
                    if(linha[1]=="NS"):
                        self.tipo = linha[1]
                        self.valor = linha[2] 
                    if(linha[0].__contains__(".")):
                        self.nome = linha[0]
                        self.tipo = linha[1]
                        self.valor = linha[2]
                    if(linha[1] == "MX"):
                        self.tipo = linha[1]
                        self.valor = linha[2]
                        self.ordem = linha[4]
                    if(linha[0].__contains__("ns")):
                        self.nome = linha[0]
                        self.tipo = linha[1]
                        self.valor = linha[2]
                    if(linha[0].__contains__("mx")):
                        self.nome = linha[0]
                        self.tipo = linha[1]
                        self.valor = linha[2]
                    if(linha[0]=="www"):
                        self.nome = linha[0]
                        self.tipo = linha[1]
                        self.valor = linha[2]
                        self.ordem = linha[4]
                    if(linha[0]=="ftp"):
                        self.nome = linha[0]
                        self.tipo = linha[1]
                        self.valor = linha[2]
                    if(linha[0]=="sp"):
                        self.nome = linha[0]
                        self.tipo = linha[1]
                        self.valor = linha[2]
                    if(linha[0].__contains__("ss")):
                        self.nome = linha[0]
                        self.tipo = linha[1]
                        self.valor = linha[2]
                    if(linha[0].__contains__("mail")):
                        self.nome = linha[0]
                        self.tipo = linha[1]
                        self.valor = linha[2]
                        
                        
                            def fixed(text, length):
        if len(text) > length:
            text = text[:length]
        elif len(text) < length:
            text = (text + " "*length)[:length]
'''

import socket
import threading

    
def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
            print(f"[SERVER] {msg}")
        
        
if __name__ == "__main__":
    main()