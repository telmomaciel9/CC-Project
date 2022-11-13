
class Parser_BD:
    
    def __init__(self):
        self.linhas = []
        self.dominio = ""
        self.ttl = 0
        self.prefixo = ""    #o parâmetro @ é reservado para identificar um prefixo por defeito que é acrescentado sempre 
                        #que um nome não apareça na forma completa (i.e., terminado com ‘.’); o valor de TTL deve ser zero;
        self.soasp = ""      #indica o nome completo do SP do domínio
        self.soaadmin = ""   #indica o endereço de e-mail completo do administrador do domínio
        self.soaserial = ""  #valor indica o número de série da base de dados do SP do domínio
        self.soarefresh = "" #indica o intervalo temporal em segundos para um SS perguntar ao SP do domínio
        self.soaretry = ""   #indica o intervalo temporal para um SS voltar a perguntar ao SP do domínio, apos um timeout
        self.soaexpire = ""  #indica o intervalo temporal para um SS deixar de considerar a sua réplica válida
        self.ns = []         #indica o nome dum servidor que é autoritativo para o domínio indicado no parâmetro (chave) 
                             #este tipo de parâmetro suporta prioridades (value)
        
    def parse_db(self, diretoria):
        with open(diretoria, "r") as f:   
            for line in f: 
                linha = line.split(" ")
                if(linha[0]!='#' or linha[0]!="\n"):
                    if(linha[0]=="@" and linha[1]=="DEFAULT"):
                        self.dominio = linha[2]
                    if(linha[0]=="TTL" and linha[1] == "DEFAULT"):
                        self.ttl=linha[3]
                    if(linha[0]=="@" and linha[1]=="SOASP"):
                        self.soasp = linha[2]
                        linha[0] = self.dominio
                        linha[3] = self.ttl
                    if(linha[0]=="@" and linha[1]=="SOAADMIN"):
                        self.soaadmin = linha[2]
                        linha[0] = self.dominio
                        linha[3] = self.ttl
                    if(linha[0]=="@" and linha[1]=="SOASERIAL"):
                        self.soaserial = linha[2]
                        linha[0] = self.dominio
                        linha[3] = self.ttl
                    if(linha[0]=="@" and linha[1]=="SOAREFRESH"):
                        self.soarefresh = linha[2]
                        linha[0] = self.dominio
                        linha[3] = self.ttl
                    if(linha[0]=="@" and linha[1]=="SOARETRY"):
                        self.soaretry = linha[2]
                        linha[0] = self.dominio
                        linha[3] = self.ttl
                    if(linha[0]=="@" and linha[1]=="SOAEXPIRE"):
                        self.soaexpire = linha[2]
                        linha[0] = self.dominio
                        linha[3] = self.ttl
                    if(linha[0]=="@" and linha[1]=="NS"):
                        self.ns.append(linha[2])
                        linha[0] = self.dominio
                        linha[3] = self.ttl
                    
                    
                
               