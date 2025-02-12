#Ficheiro que se destina a implementar a cache

import datetime
#from tabulate import tabulate

class Cache:
    def __init__(self): #n é o num de linhas max
        n = 10
        self.mat = [[0 for _ in range(9)] for _ in range(n)]
        """
        cada lista pequena correstponde a uma coluna   
        #[    0,    1,     2,   3,     4,      5,         6,     7,      8]    
        # [Name, Type, Value, TTL, Order, Origin, TimeStamp, Index, Status]
        #                            (FILE, SP, OTHERS)     (1...N) (FREE, VALID)
        """
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
                
      
    #função pedida no enunciado      
    def reg_atualiza_cache(self, name, tipo, value, ttl, order,origin): 
        current_time = datetime.datetime.now()
        time_stamp = current_time.timestamp()
        
        if(origin == "SP" or origin == "FILE"):
            flag=1
            for list in self.mat:
                if(list[8]=="FREE"):
                    list[0]=name
                    list[1]=tipo
                    list[2]=value
                    list[3]=ttl
                    list[4]=order
                    list[5]=origin
                    list[6]=time_stamp
                    list[8]="VALID"
                    flag=0
                    break
            if flag:
                self.mat.append([name, tipo, value, ttl, order, origin, time_stamp, len(self.mat)+1, "VALID"])
             
        
        if(origin == "OTHERS"):
            flag1 = 1
            flag2 = 1
            flag3 = 1
            
            for list in self.mat:
                if(list[0]== name and list[1]==type and list[2]== value and list[4]== order and (list[5]=="SP" or list[5]=="FILE")):
                    flag1 = 0
                    flag2 = 0
                    flag3 = 0
            
            if(flag1):
                for list in self.mat:
                    if(list[0]== name and list[1]==type and list[2]== value and list[4]== order and list[5]==origin ):
                        list[6]=time_stamp
                        list[8] = "VALID"
                        flag2=0
                        flag3 =0
                        break            
            if(flag2):
                for list in self.mat:
                    if list[8] == "FREE":
                        list[0]=name
                        list[1]=tipo
                        list[2]=value
                        list[3]=ttl
                        list[4]=order
                        list[5]=origin
                        list[6]=time_stamp
                        list[8]="VALID"
                        break     
                flag3=0
                
            if flag3:
                self.mat.append([name, type, value, ttl, order, origin,time_stamp, len(self.mat)+1, "VALID"])

    #função que regista na cache quando recebe uma linha (era para usar quando o ss recebe uma linha so, mas nao vai ser usada)
    """
    def reg_cache(self, mensagem):
        dominio= ""
        ttl = ""
        linha = mensagem.split(" ")
        if(linha[0]!='#'):
            if(linha[0]=="@" and linha[1]=="DEFAULT"):
                dominio = linha[2].replace("\n", "")
            if(linha[0]=="TTL" and linha[1]=="DEFAULT"):
                ttl = linha[2].replace("\n","")
            if((linha[0]=="@" or linha[0].__contains__("@")) and len(linha)<=4):
                string = linha[0].replace("@", dominio)
                self.reg_atualiza_cache(string, linha[1], linha[2], ttl, "","SP","VALID")
            if((linha[0]=="@" or linha[0].__contains__("@")) and len(linha)>4):
                string = linha[0].replace("@", dominio)
                self.reg_atualiza_cache(string, linha[1], linha[2], ttl, linha[4].replace("\n",""),"SP","VALID")
            if(not(linha[0].__contains__("@")) and len(linha)>4):
                self.reg_atualiza_cache(linha[0], linha[1], linha[2], ttl, linha[4].replace("\n",""),"SP","VALID")
            #if(not(linha[0].__contains__("@")) and len(linha)<=4):
            #    self.reg_atualiza_cache(linha[0], linha[1], linha[2], ttl, " - ","SP","VALID") 
    """
    
    #recebe uma lista de strings e regista para a cache
    def reg_cache3(self,lista):
        dominio = ""
        ttl = ""
        #print(lista)
        for frase in lista:
            palavra=frase.split(" ")   
            if(palavra[0]=="@" and palavra[1]=="DEFAULT"):
                dominio = palavra[2].replace("\n","")
            if(palavra[0]=="TTL" and palavra[1]=="DEFAULT"):
                ttl = palavra[2].replace("\n","")
            if((palavra[0]=="@" or palavra[0].__contains__("@")) and len(palavra)<=4):
                string = palavra[0].replace("@", dominio)
                self.reg_atualiza_cache(string, palavra[1].replace("\n",""), palavra[2].replace("\n",""), ttl, "","FILE")
            if((palavra[0]=="@" or palavra[0].__contains__("@")) and len(palavra)>4):
                string = palavra[0].replace("@", dominio)
                self.reg_atualiza_cache(string, palavra[1].replace("\n",""), palavra[2].replace("\n",""), ttl, palavra[4].replace("\n",""),"FILE")
            if(not(palavra[0].__contains__("@")) and len(palavra)>4):
                if(palavra[1] == "A"):
                    if(dominio != "."):
                        palavra[0]=palavra[0]+"."+dominio
                    elif dominio == ".":
                        palavra[0]=palavra[0]+dominio
                self.reg_atualiza_cache(palavra[0], palavra[1].replace("\n",""), palavra[2].replace("\n",""), ttl, palavra[4].replace("\n",""),"FILE")
            if(not(palavra[0].__contains__("@")) and len(palavra)<=4):
                if(palavra[1] == "A"):
                    if(dominio != "."):
                        palavra[0]=palavra[0]+"."+dominio
                    elif dominio == ".":
                        palavra[0]=palavra[0]+dominio
                self.reg_atualiza_cache(palavra[0].replace("\n",""), palavra[1].replace("\n",""), palavra[2].replace("\n",""), ttl, "","FILE")

    #def __str__(self):
    #    header = ["Name", "Type", "Value", "TTL", "Order", "Origin", "TimeStamp", "Index", "Status"]
    #    return (tabulate(self.mat, headers = header, tablefmt = "grid"))
    
    def __str__(self):
        out = ""
        for list in self.mat:
            #for i in range(len(list)):
            #    out+=str(list[i]) + " "
            out+=str(list)+"\n"
        return out
    