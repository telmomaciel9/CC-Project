from writer import Writer

w = Writer()
w.escreve_log("/home/rogan/Desktop/CC/trabalho/CC/G2/entrada/log.txt")





[
    ['MESSAGE-ID', '=', '3874', 'FLAGS', '=', 'Q+R', 'RESPONSE-CODE', '=', '0,', ''], 
    ['N-VALUES', '=', '0', 'N-AUTHORITIES', '=', '0', 'N-EXTRA-VALUES', '=', '0,;', ''], 
    ['QUERY-INFO.NAME', '=', 'example.com.', 'QUERY-INFO.TYPE', '=', 'MX,;', ''], 
    ['RESPONSE-VALUES', '=', '(Null)', ''], 
    ['AUTHORITIES-VALUES', '=', '(Null)', ''], 
    ['EXTRA-VALUES', '=', '(Null)']]


if(linha[0] == "MESSAGE-ID"):
                        self.message_id = linha[2]
                    elif(linha[3] == "FLAGS"):
                        self.flags = linha[4]
                    elif(linha[5] == "RESPONSE-CODE"):
                        self.response_code = linha[7]
                    elif(linha[0] == "N-VALUES"):
                        self.num_values=linha[2]
                    elif(linha[3] == "DD"):
                        self.ip_DD.append(linha[2])
                    elif(linha[1] == "ST"):
                        self.ip_ST = linha[2]
                    elif(linha[1] == "SP"):
                        self.ip_SP = linha[2]
                    elif(linha[1] == "LG"):
                        self.dir_log = linha[2]    
                        
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