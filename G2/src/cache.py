#Ficheiro que se destina a implementar a cache

import datetime
from tabulate import tabulate
from entrada import Entrada

class Cache:
    def __init__(self): #n é o num de linhas max
        n = 40
        self.mat = [[0 for _ in range(9)] for _ in range(n)]
        #cada lista pequena correstponde a uma coluna   
        #[    0,    1,     2,   3,     4,      5,         6,     7,      8]    
        # [Name, Type, Value, TTL, Order, Origin, TimeStamp, Index, Status]
        #                            (FILE, SP, OTHERS)     (1...N) (FREE, VALID)
        i=0
        while i<n:
            self.mat [i][7] = i+1
            self.mat [i][8] = "FREE"
            i=i+1
        

    def verifica_valid (self, index, name, type):
        i=index-1
        r=index-1
        for list in self.mat:
            if(list[7]>=i):
                if(list[0]==name and list[1]==type and list[8]=="VALID"):
                    return r
            if(list[5]=="OTHERS" and (list[6]>list[3])):
                list[8]= "FREE"
                
      
                
    def reg_atualiza_cache(self, name, tipo, value, ttl, order,origin, status):
        
        current_time = datetime.datetime.now()
        time_stamp = current_time.timestamp()
        
        if(origin == "SP" or origin == "FILE"):
            for list in self.mat:
                if(list[8]=="FREE"):
                    novaPos = list[7]-1
                    self.mat[novaPos][0]=name
                    self.mat[novaPos][1]=tipo
                    self.mat[novaPos][2]=value
                    self.mat[novaPos][3]=ttl
                    self.mat[novaPos][4]=order
                    self.mat[novaPos][5]=origin
                    self.mat[novaPos][6]=time_stamp
                    self.mat[novaPos][8]=status
                    break           
        flag1 = 1
        flag2 = 1      
        if(origin == "OTHERS"):
            for list in self.mat:
                if(list[0]== name and list[1]==type and list[2]== value and list[4]== order and (list[5]=="SP" or list[5]=="FILE")):
                    flag1 = 0
            if(flag1):
                for list in self.mat:
                    if(list[0]== name and list[1]==type and list[2]== value and list[4]== order and list[5]=="OTHERS" ):
                        list[6]=time_stamp
                        list[8] = "VALID"
                        flag2=0
                        break            
            if(flag2):
                self.mat.append([name, type, value, ttl, order, origin,time_stamp, len(self.mat)+1, "FREE"])

    def reg_cache(self, mensagem):
        dominio= ""
        ttl = ""
        linha = mensagem.split(" ")
        if(linha[0]!='#'):
            if(linha[0]=="@" and linha[1]=="DEFAULT"):
                dominio = linha[2]
            if(linha[0]=="TTL" and linha[1]=="DEFAULT"):
                ttl = linha[2]
            if((linha[0]=="@" or linha[0].__contains__("@")) and len(linha)<=4):
                string = linha[0].replace("@", dominio)
                self.reg_atualiza_cache(string, linha[1], linha[2], ttl, " - ","SP","VALID")
            if((linha[0]=="@" or linha[0].__contains__("@")) and len(linha)>4):
                string = linha[0].replace("@", dominio)
                self.reg_atualiza_cache(string, linha[1], linha[2], ttl, linha[4],"SP","VALID")
            if(not(linha[0].__contains__("@")) and len(linha)>4):
                self.reg_atualiza_cache(linha[0], linha[1], linha[2], ttl, linha[4],"SP","VALID")
            #if(not(linha[0].__contains__("@")) and len(linha)<=4):
            #    self.reg_atualiza_cache(linha[0], linha[1], linha[2], ttl, " - ","SP","VALID") 
                

    
    def __str__(self):
        header = ["Name", "Type", "Value", "TTL", "Order", "Origin", "TimeStamp", "Index", "Status"]
        return (tabulate(self.mat, headers = header, tablefmt = "grid"))