import socket

class SS_TCP:
     
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ss.connect(("127.0.0.1",9999))
    
    ss.send("estou a conectar".encode('utf-8'))
    print(ss.recv(1024).decode('utf-8'))
    ss.send("bye".encode('utf-8'))
    print(ss.recv(1024).decode('utf-8'))