# Nesta classe está a função em que le o ficheiro, e ao mesmo tempo que le, guarda os parametros nas vars
class Parser_Config:
    
    def __init__(self,diretoria):
        self.diretoria = diretoria
        self.dominio = ""
        self.linhas = []
        self.dir_logLocal = ""
        self.dir_logAll = ""
        self.dir_bd = ""
        self.ip_SS = []
        self.ip_SP = ""
        self.ip_DD = []
        self.dir_ST = ""
        
    def parse_Config(self):
        with open(self.diretoria, "r") as f:    #config   
            for line in f: 
                linha = line.split(" ")
                if(linha[0]!='#'):
                    self.linhas.append(linha)
                    if(linha[1] == "DB"):
                        self.dominio = linha[0]
                        self.dir_bd = linha[2]
                    if(linha[1] == "SP"):
                        self.dominio = linha[0]
                        self.ip_SP = linha[2]
                    if(linha[1] == "SS"):
                        self.dominio = linha[0]
                        self.ip_SS.append(linha[2])
                    if(linha[1] == "DD"):
                        self.dominio = linha[0]
                        self.ip_DD.append(linha[2])
                    if(linha[1] == "ST" and linha[0] == "root"):
                        self.dir_ST = linha[2]
                    if(linha[1] == "SP"):
                        self.ip_SP = linha[2]
                    if(linha[1] == "LG" and linha[0]=="all"):
                        self.dir_logAll = linha[2]
                    if(linha[1] == "LG" and linha[0]!="all"):
                        self.dir_logLocal = linha[2]
        f.close()
                        
    def __str__(self):
        #print(self.linhas)
        return self.dominio