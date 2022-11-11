
class Parser_BD:
    
    def __init__(self):
        ttl = 0
        prefixo = ""    #o parâmetro @ é reservado para identificar um prefixo por defeito que é acrescentado sempre 
                        #que um nome não apareça na forma completa (i.e., terminado com ‘.’); o valor de TTL deve ser zero;
        soasp = ""      #indica o nome completo do SP do domínio
        soaadmin = ""   #indica o endereço de e-mail completo do administrador do domínio
        soaserial = ""  #valor indica o número de série da base de dados do SP do domínio
        soarefresh = "" #indica o intervalo temporal em segundos para um SS perguntar ao SP do domínio
        soaretry = ""   #indica o intervalo temporal para um SS voltar a perguntar ao SP do domínio, apos um timeout
        soaexpire = ""  #indica o intervalo temporal para um SS deixar de considerar a sua réplica válida
        ns = tuple()     #indica o nome dum servidor que é autoritativo para o domínio indicado no parâmetro (chave) 
                        #este tipo de parâmetro suporta prioridades (value)
        
    
    with open("modeloDB.txt", "r") as f:   
        for line in f: 
            linha = line.split(" ")
            if(linha[0]!='#'):
                linhas.append(linha)
            
        print(linhas)   