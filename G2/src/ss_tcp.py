import socket

class SS_TCP:
     
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ss.connect((socket.gethostbyname(socket.gethostname()), 20001))
    print(f"[CONNECTED] Cliente connected")
    
    connected = True
    while connected:
        msg = input("> ")
        
        ss.send(msg.encode('utf-8'))
        if msg == "!DISCONNECT":
            connected = False
        else:
            msg = ss.recv(1024).decode('utf-8')
            print(f"[SERVER] {msg}")