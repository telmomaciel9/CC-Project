
class Parser_BD:
    linhas = []
    with open("modeloDB.txt", "r") as f:   
        for line in f: 
            linha = line.split(" ")
            if(linha[0]!='#'):
                linhas.append(linha)
            
        print(linhas)   