from cache import Cache
class Parser_BD:
    
    def __init__(self):
        self.linhas = []
        self.dominio = ""
        self.ttl = ""
  
        
    def parse_db(self, diretoria):
        with open(diretoria, "r") as f:   
            c = Cache()
            for line in f: 
                linha = line.split(" ")
                if(linha[0]!='#'):
                    if(linha[0]=="@" and linha[1]=="DEFAULT"):
                        self.dominio = linha[2]
                    if(linha[0]=="TTL" and linha[1]=="DEFAULT"):
                        self.ttl = linha[2]
                    if((linha[0]=="@" or linha[0].__contains__("@")) and len(linha)<=4):
                        string = linha[0].replace("@", self.dominio)
                        c.reg_atualiza_cache(string, linha[1], linha[2], self.ttl, " ","FILE","VALD")
                    if((linha[0]=="@" or linha[0].__contains__("@")) and len(linha)>4):
                        string = linha[0].replace("@", self.dominio)
                        c.reg_atualiza_cache(string, linha[1], linha[2], self.ttl, linha[4],"FILE","VALD")
                    if(not(linha[0].__contains__("@")) and len(linha)>4):
                        c.reg_atualiza_cache(linha[0], linha[1], linha[2], self.ttl, linha[4],"FILE","VALD")
                    if(not(linha[0].__contains__("@")) and len(linha)<=4):
                        c.reg_atualiza_cache(linha[0], linha[1], linha[2], self.ttl, "","FILE","VALD")
            print(c)
                        
                    