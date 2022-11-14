#ficheiro que faço testes ao codigo

"""
from cliente_UDP import Cliente_UDP
from trabalho.CC.G2.src.query import Message
from server_UDP import Server_UDP

m = Message()
m.parse_message_condense("/home/rogan/Desktop/CC/trabalho/CC/G2/entrada/query.txt")

serv = Server_UDP()
cliente = Cliente_UDP ()
serv.conectar()
cliente.enviar_mensagem(m)
"""

from cache import Cache

c = Cache(3)

print(c)

c.reg_atualiza_cache("t1","1","1",1,"1", "FILE","VALID")
c.reg_atualiza_cache("t2","2","2",2,"2", "SP","VALID")
c.reg_atualiza_cache("t3","3","3",3,"3", "OTHERS","VALID")


print(c)

print(c.verifica_valid(1,"t1","1"))
print(c.verifica_valid(1,"t2","1"))