import socket

class Server_UDP:
    bufferSize = 1024

    msgFromServer = "Hello UDP Client"
    bytesToSend = str.encode(msgFromServer)

    # Create a datagram socket
    UDPServer = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # Bind to address and ip
    UDPServer.bind(("127.0.0.1", 20001))

    print("UDP server up and listening")

    # Listen for incoming datagrams
    while(True):

        (msg,add) = UDPServer.recvfrom(bufferSize)

        clientMsg = "Message from Client-{}:  ".format(msg)
        clientIP  = "Client IP Address:{}".format(add)
        
        print(clientMsg)
        print(clientIP)

        # Sending a reply to client
        UDPServer.sendto(bytesToSend, add)