import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket criado")

s.bind(("127.0.0.1", 8000))
print("socket binded")

s.listen()
print("socket is listening")

mensagem = " ola"

while(True):
    (msg, add) = s.recv(len(mensagem))
    print ('Got connection from', add)
    msg.send(mensagem.decode('utf-8'))
    msg.close()