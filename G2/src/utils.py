#utilizo este ficheiro mais para guardar potencial codigo, 

from writer import Writer

w = Writer()
w.escreve_log("/home/rogan/Desktop/CC/trabalho/CC/G2/entrada/log.txt")

from message import Message

m = Message()
m.parse_message_condense("/home/rogan/Desktop/CC/trabalho/CC/G2/entrada/query.txt")
print(m)