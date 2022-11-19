import socket

class SP_TCP:

    
    
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