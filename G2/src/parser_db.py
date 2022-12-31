class Parser_BD:
    
    def __init__(self, diretoria):
        self.diretoria = diretoria
        self.linhas = []
        self.dominio = ""
        self.ttl = ""
        self.soasp = ""
        self.soaadmin = ""
        self.soaserial = 0
        self.soarefresh = 0
        self.soaretry = 0
        self.soaexpire = 0
        self.ns = []
        self.a = []
  
        
    def parse_db(self, cache):
        with open(self.diretoria, "r") as f:     
            for line in f: 
                linha = line.split(" ")
                if(linha[0]!='#' and linha[0]!='\n'):
                    self.linhas.append(line)
                    if(linha[0] == "@" and linha[1]=="DEFAULT"):
                        self.dominio = linha[2]
                    if(linha[0] == "TTL" and linha[1]=="DEFAULT"):
                        self.ttl = linha[2]
                    if(linha[0] == "@" and linha[1]=="SOASP"):
                        self.soasp = linha[2]
                    if(linha[0] == "@" and linha[1]=="SOAADMIN"):
                        self.soaadmin = linha[2]
                    if(linha[0] == "@" and linha[1]=="SOASERIAL"):
                        self.soaserial = linha[2]
                    if(linha[0] == "@" and linha[1]=="SOAREFRESH"):
                        self.soarefresh = linha[2]
                    if(linha[0] == "@" and linha[1]=="SOARETRY"):
                        self.soaretry = linha[2]
                    if(linha[0] == "@" and linha[1]=="SOAEXPIRE"):
                        self.soaretry = linha[2]
                    if(linha[1] == "A"):
                        if(self.dominio == "."):
                            linha[0]=linha[0]+self.dominio
                        elif(self.dominio != "."):
                            linha[0]=linha[0]+"."+self.dominio
                        
        cache.reg_cache3(self.linhas)
        
        f.close()
        
    def __str__ (self):
        return str(self.linhas)     
"""
if __name__ == "__main__":
    c = Cache()
    b = Parser_BD()
    b.parse_db(c)
    print(b)
"""