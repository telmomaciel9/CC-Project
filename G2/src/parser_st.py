class Parser_ST:
    
    def __init__(self,diretoria):
        self.linhas = []
        self.diretoria = diretoria
        self.sts = []
        with open(self.diretoria, "r") as f:    #config   
            for line in f: 
                linha = line.split(" ")
                if(linha[0]!='#'):
                    self.linhas.append(linha)
                    if(linha[0] == "ST"):
                        self.sts.append(linha[1].replace("\n",""))