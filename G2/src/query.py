#classe que da parse da mensgem
from cache import Cache
import re

class Query:
    def __init__(self):
        self.message_id = ""
        self.flags = ""
        self.response_code = ""
        self.num_values = ""
        self.num_authorities = ""
        self.num_extra_value = ""
        self.query_info_name = ""
        self.query_info_type = ""
        self.responde_value = []
        self.authoriries_vales = []
        self.extra_values = []
        
        
    def parse_message_condense (self, query_str):
        linha = re.split(";|,| ",query_str)
        if(linha[0]!='#'):
            self.message_id = linha[0]
            self.flags = linha[1]
            self.response_code = linha[2]
            self.num_values = linha[3]
            self.num_authorities = linha[4]
            self.num_extra_value = linha[5]
            self.query_info_name = linha[6]
            self.query_info_type = linha[7] 
            
         
    
    def le_linha (self, diretoria):
        with open(diretoria, "r") as f:                                    
            return f.readline()
            
    

    def __str__(self):
        out = ""
        out += "MESSAGE-ID  = " + self.message_id + "\nFLAGS = " + self.flags + "\nRESPONSE-CODE = " + self.response_code + "\nN-VALUES = " + self.num_values + "\nN-EXTRA-VALUES = " + self.num_extra_value + "\nQUERY-INFO_NAME = " + self.query_info_name+ "\nQUERY-INFO_TYPE = " + self.query_info_type
        return out
        