from cache import Cache
from parser_db import Parser_BD
from parser_config import Parser_Config


class SP:
    def __init__(self):
        self.srvCache = Cache()
        self.srvBD = Parser_BD()
        self.srvConfig = Parser_Config()
        self.srvST_list = ""
        
    def regista_serverCache(self, nome,tipo,valor,ttl,order,origin,status):
        self.serverCache.reg_atualiza_cache(nome, tipo, valor, ttl, order,origin, status)
        
    def gera_resposta(self,mensagem):
        out = mensagem + '\n' 
        