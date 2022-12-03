import socket
serverTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverTCP.bind(('',2001))
serverTCP.listen()
while 1:
    conn, addr = serverTCP.accept()
    print(f"[NEW CONNETION] {addr} CONNECTED.")
    msg = conn.recv(1024).decode('utf-8')
    print(f"[SP] - Message receive:\n -> {msg}")