#classe que da parse da mensgem

import re

class Query:

    def __init__(self):
        self.message_id = ""
        self.flags = ""
        self.response_code = 2
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
            self.flags = linha[1]
            self.query_info_name = linha[6]
            self.query_info_type = linha[7] 

    
    def gera_queryInterna(self):
        out = ""
        if self.flags =="":
            out = str(self.message_id) + ",Q,0,"+str(self.num_values)+","+str(self.num_authorities)+","+str(self.num_extra_value)+";"+str(self.query_info_name) + "," + str(self.query_info_type)
        if self.flags != "":
            out = str(self.message_id) + ",Q+"+str(self.flags)+ ",0,0,0,0," + str(self.query_info_name) + "," + str(self.query_info_type)
        return out
        
    def origina_resposta(self,cache, query):
        rval = ""
        aval = ""
        eval = ""
        rvalA = []
        avalA = []

        for list in cache.mat:
            if list[0] == query.query_info_name  or (str(list[0]) in str(query.query_info_name)) or (str(query.query_info_name) in str(list[0])):
                #response
                if (list[0] == query.query_info_name and list[1] == query.query_info_type):
                    self.response_code = 0
                    self.num_values=self.num_values+1
                    for i in range(5):            
                        rval = rval + str(list[i]) + " "
                    rvalA.append(rval)
                    rval = rval + "\n"
                elif (list[0] != query.query_info_name or (str(list[0]) in str(query.query_info_name)) or (str(query.query_info_name) in str(list[0]))) and (list[1] == query.query_info_type or list[1] == "NS"):
                    self.response_code = 1
                    
                #autoritativas
                if (list[0] == query.query_info_name or (str(list[0]) in (query.query_info_name)) or (str(query.query_info_name) in str(list[0]))) and list[1] == "NS":
                    self.num_authorities=self.num_authorities+1
                    for i in range(5):            
                        aval = aval + str(list[i]) + " "
                    avalA.append(aval)
                    aval = aval + "\n"

            #extra
            if (list[1]=="A"):
                domaux = query.query_info_name.split(".")
                dom = [x for x in domaux if len(x) > 0]

                if query.query_info_type.lower() in list[0] or (dom[len(dom)-1] in list[0]):
                    self.num_extra_value= self.num_extra_value+1
                    for i in range(5):            
                        eval = eval + str(list[i]) + " "
                    eval = eval + "\n"
            

        msg=self.message_id+","+self.flags+","+str(self.response_code)+","+str(self.num_values)+","+str(self.num_authorities)+","+str(self.num_extra_value)+";"+self.query_info_name+","+self.query_info_type+";"
        
        return (msg+"\n"+rval+aval+eval)    
    
    def le_linha (self, diretoria):
        with open(diretoria, "r") as f:                                    
            return f.readline()

    def __str__(self):
        out = ""
        out += "MESSAGE-ID  = " + self.message_id + "\nFLAGS = " + self.flags + "\nRESPONSE-CODE = " + self.response_code + "\nN-VALUES = " + self.num_values + "\nN-EXTRA-VALUES = " + self.num_extra_value + "\nQUERY-INFO_NAME = " + self.query_info_name+ "\nQUERY-INFO_TYPE = " + self.query_info_type
        return out
