import logging
import re
class Logs:
    # O modo é se estamos a correr um servidor em modo debug ou shy
    # No modo debug, todos os logs também são mandados para o standard output
     def __init__(self, fileLogsLocal = '', fileLogsAll = '', modo = ""):
          primeiraLinha = "# Log File for DNS server/resolver\n"
          self.fileLogsLocal = fileLogsLocal
          self.fileLogsAll = fileLogsAll
          with open(self.fileLogsLocal, "a") as fLocal:
               fLocal.write(primeiraLinha)
          with open(self.fileLogsAll, "a") as fAll:
               fAll.write(primeiraLinha)
          self.modoDebug = modo
    
     def formatacao(self):
        logging.basicConfig(filename = self.fileLogsLocal, filemode="a", level=logging.INFO, format= "%(asctime)s.%(msecs)03d %(message)s", datefmt='%d:%m:%Y.%H:%M:%S')

     def impressora (self,string):
        logging.info(string)
        if self.modoDebug =="debug":
            print(string)
     
    # recebe == true recebeu query, false enviou que
     def QR_QE(self, recebe, endereco, infoQuery = ''):
        self.formatacao()
        
        if recebe:
            string = "QR " + str(endereco) + " " + infoQuery
        else:
            string = "QE " + str(endereco) + " " + infoQuery
        
        self.impressora(string)

     def RP_RR(self, recebe, endereco, infoQuery=''):
        self.formatacao()
        
        if recebe:
            string = "RR " + str(endereco) + " " + infoQuery
        else:
            string = "RP " + str(endereco) + " " + infoQuery

        self.impressora(string)

     def ZT(self, endereco, role = '', time = '', totalbytes = ''):
        self.formatacao()
        
        if time == '' and totalbytes == '':
            string = "ZT " + str(endereco) + " " + role
        else:
            string = "ZT " + str(endereco) + " " + role + " " + time + " " + totalbytes

        self.impressora(string)

     def EV(self, acontecimento, msg=''):
        self.formatacao()

        if msg:
            string = "EV 127.0.0.1 " + acontecimento + " " + msg 
        else:
            string = "EV 127.0.0.1 " + acontecimento

        self.impressora(string)

     def ER(self, endereco):
        self.formatacao()
        string = "ER " + str(endereco)   

        self.impressora(string)

     def EZ(self, ip, porta, role):
        self.formatacao()

        string = "EZ " + ip + ":" + porta + " " + role

        self.impressora(string)

     def FL(self, errorType):
        self.formatacao()
        string = "FL 127.0.0.1 " + errorType

        self.impressora(string)

     def TO(self, timeoutType):
        self.formatacao()
        string = "TO " + timeoutType

        self.impressora(string)

     def SP(self, reason):
        self.formatacao()
        string = "SP 127.0.0.1 " + reason

        self.impressora(string)

     def ST(self, port, timeout, mode):
        self.formatacao()
        string = "ST 127.0.0.1 " + port + " " + timeout + " " + mode
        
        self.impressora(string)