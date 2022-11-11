import re
linhas = []
with open("/home/rogan/Desktop/CC/trabalho/CC/G2/entrada/query.txt", "r") as f:
            for line in f: 
                linha = re.split("; |, | |,; |,\n |,;\n |\*|\n",line)
                if(linha[0]!='#'):
                    linhas.append(linha)
                                                     
f.close() 
print(linhas)