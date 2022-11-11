import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket criado")

port =  123
s.connect(('',port))

message = "ola"
s.sendall(message.encode())
s.close()