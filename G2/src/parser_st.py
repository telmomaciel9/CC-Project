class Parser_ST:
    
    def __init__(self, diretoria):
        self.diretoria = diretoria
        self.linhas = []
        

    def parse_db(self):
        with open(self.diretoria, "r") as f:     
            for line in f: 
                linha = line.split(" ")
                if(linha[0]!='#' and linha[0]!='\n'):
                    self.linhas.append(line)