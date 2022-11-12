#classe que da parse da mensgem

import re

class Message:
    def __init__(self):
        message_id = ""
        flags = ""
        response_code = ""
        num_values = ""
        num_authorities = ""
        num_extra_value = ""
        query_info_name = ""
        query_info_type = ""
        responde_value = []
        authoriries_vales = []
        extra_values = []
        
    def parse_message_condense (self, diretoria):
        with open(diretoria, "r") as f:
            for line in f: 
                linha = re.split(";|,| ",line)
                if(linha[0]!='#'):
                    self.message_id = linha[0]
                    self.flags = linha[1]
                    self.response_code = linha[2]
                    self.num_values = linha[3]
                    self.num_authorities = linha[4]
                    self.num_extra_value = linha[5]
                    self.query_info_name = linha[6]
                    self.query_info_type = linha[7]                       
        f.close() 
    
    def __str__(self):
        out = ""
        out += "MESSAGE-ID  = " + self.message_id + "\nFLAGS = " + self.flags + "\nRESPONSE-CODE = " + self.response_code + "\nN-VALUES = " + self.num_values + "\nN-EXTRA-VALUES = " + self.num_extra_value + "\nQUERY-INFO_NAME = " + self.query_info_name+ "\nQUERY-INFO_TYPE = " + self.query_info_type
        return out
        