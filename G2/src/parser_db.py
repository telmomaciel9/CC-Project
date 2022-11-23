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
        cache.reg_cache3(self.linhas)
        
    def __str__ (self):
        return str(self.linhas)     
"""
if __name__ == "__main__":
    c = Cache()
    b = Parser_BD()
    b.parse_db(c)
    print(b)
"""