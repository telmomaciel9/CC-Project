import re

class Message:
    def __init__(self):
        message_id = ""
        flags = ""
        response_code = ""
        num_values = ""
        num_authorities = ""
        num_extra_value = ""
        query_info = ""
        responde_value = []
        authoriries_vales = []
        extra_values = []
        
    def parse_message_extended (self, diretoria):
        with open("/home/rogan/Desktop/CC/trabalho/CC/G2/entrada/query.txt", "r") as f:
            for line in f: 
                linha = re.split("; |, | |\*|\n",line)
                if(linha[0]!='#'):
                    if(linha[0] == "MESSAGE-ID"):
                        self.message_id = linha[2]
                    elif(linha[3] == "FLAGS"):
                        self.flags = linha[5]
                    elif(linha[6] == "RESPONSE-CODE"):
                        self.response_code = linha[8]
                    elif(linha[0] == "N-VALUES"):
                        self.num_values=linha[2]
                    elif(linha[3] == "N'AUTHORITIES"):
                        self.num_authorities = linha[5]
                    elif(linha[5] == "N-EXTRA-VALUES"):
                        self.num_extra_value = linha[7]
                                                     
        f.close() 
        