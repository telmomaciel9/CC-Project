from cache import Cache
class Parser_BD:
    
    def __init__(self, diretoria="/home/rogan/Desktop/CC/trabalho/CC/G2/entrada/modeloDB.txt"):
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
                        self.dominio = linha[2].replace("\n","")
                    if(linha[0]=="TTL" and linha[1]=="DEFAULT"):
                        self.ttl = linha[2].replace("\n","")
                    if((linha[0]=="@" or linha[0].__contains__("@")) and len(linha)<=4):
                        string = linha[0].replace("@", self.dominio)
                        cache.reg_atualiza_cache(string, linha[1].replace("\n",""), linha[2].replace("\n",""), self.ttl, "","FILE","VALID")
                    if((linha[0]=="@" or linha[0].__contains__("@")) and len(linha)>4):
                        string = linha[0].replace("@", self.dominio)
                        cache.reg_atualiza_cache(string, linha[1].replace("\n",""), linha[2].replace("\n",""), self.ttl, linha[4].replace("\n",""),"FILE","VALID")
                    if(not(linha[0].__contains__("@")) and len(linha)>4):
                        cache.reg_atualiza_cache(linha[0], linha[1].replace("\n",""), linha[2].replace("\n",""), self.ttl, linha[4].replace("\n",""),"FILE","VALID")
                    if(not(linha[0].__contains__("@")) and len(linha)<=4):
                        cache.reg_atualiza_cache(linha[0].replace("\n",""), linha[1].replace("\n",""), linha[2].replace("\n",""), self.ttl, "","FILE","VALID")
        
    def __str__ (self):
        return str(self.linhas) 