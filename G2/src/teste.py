#ficheiro que faço testes ao codigo

from cliente_UDP import Cliente_UDP
from message import Message
from server_UDP import Server_UDP

m = Message()
m.parse_message_condense("/home/rogan/Desktop/CC/trabalho/CC/G2/entrada/query.txt")

serv = Server_UDP()
cliente = Cliente_UDP ()
serv.conectar()
cliente.enviar_mensagem(m)