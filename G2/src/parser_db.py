from cache import Cache
class Parser_BD:
    
    def __init__(self, diretoria):
        self.diretoria = diretoria
        self.linhas = []
        self.dominio = ""
        self.ttl = ""
  
        
    def parse_db(self, cache):
        with open(self.diretoria, "r") as f:     
            for line in f: 
                linha = line.split(" ")
                if(linha[0]!='#'):
                    self.linhas.append(line)
                    if(linha[0]=="@" and linha[1]=="DEFAULT"):
                        self.dominio = linha[2]
                    if(linha[0]=="TTL" and linha[1]=="DEFAULT"):
                        self.ttl = linha[2]
                    if((linha[0]=="@" or linha[0].__contains__("@")) and len(linha)<=4):
                        string = linha[0].replace("@", self.dominio)
                        cache.reg_atualiza_cache(string, linha[1], linha[2], self.ttl, " - ","FILE","VALID")
                    if((linha[0]=="@" or linha[0].__contains__("@")) and len(linha)>4):
                        string = linha[0].replace("@", self.dominio)
                        cache.reg_atualiza_cache(string, linha[1], linha[2], self.ttl, linha[4],"FILE","VALID")
                    if(not(linha[0].__contains__("@")) and len(linha)>4):
                        cache.reg_atualiza_cache(linha[0], linha[1], linha[2], self.ttl, linha[4],"FILE","VALID")
                    if(not(linha[0].__contains__("@")) and len(linha)<=4):
                        cache.reg_atualiza_cache(linha[0], linha[1], linha[2], self.ttl, " - ","FILE","VALID")
        
    def __str__ (self):
        return self.linhas 