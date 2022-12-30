class Parse_listaSt:
    def __init__(self,diretoria):
        self.diretoria = diretoria
        self.sts = []
        
    def parseST(self):
        with open(self.diretoria, "r") as f:    #config   
            for line in f: 
                linha = line.split(" ")
                if(linha[0]!='#'):
                    if(linha[0] == "ST"):
                        self.sts = linha[1]
