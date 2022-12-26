#classe que da parse da mensgem

import re

class Query:

    def __init__(self):
        self.message_id = ""
        self.flags = ""
        self.response_code = 0
        self.num_values = 0
        self.num_authorities = 0
        self.num_extra_value = 0
        self.query_info_name = ""
        self.query_info_type = ""
       


    def parse_message_condense (self, query_str):
        linha = re.split(";|,| ",query_str)
        if(linha[0]!='#'):
            self.message_id = linha[0]
            l = linha[1].split("+")
            #if(l[0]=="Q"):
            #    self.flags=l[1]
            #else:
            self.flags = linha[1]
            self.query_info_name = linha[6]
            self.query_info_type = linha[7] 

    
    def gera_queryInterna(self):
        out = ""
        if self.flags =="":
            out = str(self.message_id) + ",Q,"+str(self.response_code) +","+str(self.num_values)+","+str(self.num_authorities)+","+str(self.num_extra_value)+";"+str(self.query_info_name) + "," + str(self.query_info_type)
        if self.flags != "":
            out = str(self.message_id) + ",Q+"+str(self.flags)+ ",0,0,0,0," + str(self.query_info_name) + "," + str(self.query_info_type)
        return out
        
    def origina_resposta(self,cache, query):
        rval = ""
        aval = ""
        eval = ""
        for list in cache.mat:
            #response
            if((str(list[1]) == str(query.query_info_type)) and (str(list[0]) == str(query.query_info_name))):
                self.num_values=self.num_values+1
                for i in range(5):            
                    rval = rval + str(list[i]) + " "
                rval = rval + "\n"
            
            #autoritativas
            if(str(list[0]) == query.query_info_name and str(list[1]) == "NS"):
                self.num_authorities=self.num_authorities+1
                for i in range(5):            
                    aval = aval + str(list[i]) + " "
                aval = aval + "\n"
            
            #extra
            if((str(list[1]) == "A" and "NS".lower() in list[0]) or (str(list[1]) == "A" and query.query_info_type.lower() in list[0])):
                self.num_extra_value= self.num_extra_value+1
                for i in range(5):            
                    eval = eval + str(list[i]) + " "
                eval = eval + "\n"         
                
        msg="\n"+self.message_id+","+self.flags+","+str(self.response_code)+","+str(self.num_values)+","+str(self.num_authorities)+","+str(self.num_extra_value)+";"+self.query_info_name+","+self.query_info_type+";"
        
        return (msg+"\n"+rval+aval+eval)    
    
    def le_linha (self, diretoria):
        with open(diretoria, "r") as f:                                    
            return f.readline()

    def __str__(self):
        out = ""
        out += "MESSAGE-ID  = " + self.message_id + "\nFLAGS = " + self.flags + "\nRESPONSE-CODE = " + self.response_code + "\nN-VALUES = " + self.num_values + "\nN-EXTRA-VALUES = " + self.num_extra_value + "\nQUERY-INFO_NAME = " + self.query_info_name+ "\nQUERY-INFO_TYPE = " + self.query_info_type
        return out
