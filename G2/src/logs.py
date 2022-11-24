import logging
import re
class Logs:
    # O modo é se estamos a correr um servidor em modo debug ou shy
    # No modo debug, todos os logs também são mandados para o standard output
     def __init__(self, fileLogs = '', fileLogsAll = '', modo = ''):
          primeiraLinha = "# Log File for DNS server/resolver\n"
          self.fileLogs = fileLogs
          self.fileLogsAll = fileLogsAll
          with open(self.fileLogs, "a") as fLocal:
               fLocal.write(primeiraLinha)
          with open(self.fileLogs, "a") as fAll:
               fAll.write(primeiraLinha)
          self.modo = modo

     
     
    # recebe == true recebeu, false enviou
     def QR_QE(self, recebe, endereco, infoQuery = ''):
        logging.basicConfig(filename = self.fileLogs, filemode="a", level=logging.INFO, format= "%(asctime)s.%(msecs)03d %(message)s", datefmt='%d:%m:%Y.%H:%M:%S')
        
        if recebe:
            string = "QR " + endereco + " " + infoQuery
        else:
            string = "QE " + endereco + " " + infoQuery
        
        logging.info(string)
        if self.modo == 'debug':
            print(string)


     def RP_RR(self, recebe, endereco, infoQuery=''):
        logging.basicConfig(filename = self.fileLogs, filemode="a", level=logging.INFO, format= "%(asctime)s.%(msecs)03d %(message)s", datefmt='%d:%m:%Y.%H:%M:%S')
        
        if recebe:
            string = "RR " + endereco + " " + infoQuery
        else:
            string = "RP " + endereco + " " + infoQuery

        logging.info(string)
        if self.modo == 'debug':
            print(string)

     def ZT(self, ip, porta, role = '', time = '', totalbytes = ''):
        logging.basicConfig(filename = self.fileLogs, filemode="a", level=logging.INFO, format= "%(asctime)s.%(msecs)03d %(message)s", datefmt='%d:%m:%Y.%H:%M:%S')
        
        if time == '' and totalbytes == '':
            string = "ZT " + ip + ":" + porta + " " + role
        else:
            string = "ZT " + ip + ":" + porta + " " + role + " " + time + " " + totalbytes

        logging.info(string)
        if self.modo == 'debug':
            print(string)

     def EV(self, eventType, msg=''):
        logging.basicConfig(filename = self.fileLogs, filemode="a", level=logging.INFO, format= "%(asctime)s.%(msecs)03d %(message)s", datefmt='%d:%m:%Y.%H:%M:%S')

        if msg:
            string = "EV 127.0.0.1 " + eventType + " " + msg 
        else:
            string = "EV 127.0.0.1 " + eventType

        logging.info(string)
        if self.modo == 'debug':
            print(string)

     def ER(self, endereco):
        logging.basicConfig(filename = self.fileLogs, filemode="a", level=logging.INFO, format= "%(asctime)s.%(msecs)03d %(message)s", datefmt='%d:%m:%Y.%H:%M:%S')
        string = "ER " + endereco   

        logging.info(string)
        if self.modo == 'debug':
            print(string)

     def EZ(self, ip, porta, role):
        logging.basicConfig(filename = self.fileLogs, filemode="a", level=logging.INFO, format= "%(asctime)s.%(msecs)03d %(message)s", datefmt='%d:%m:%Y.%H:%M:%S')

        string = "EZ " + ip + ":" + porta + " " + role

        logging.info(string)
        if self.modo == 'debug':
            print(string)

     def FL(self, errorType):
        logging.basicConfig(filename = self.fileLogs, filemode="a", level=logging.INFO, format= "%(asctime)s.%(msecs)03d %(message)s", datefmt='%d:%m:%Y.%H:%M:%S')
        string = "FL 127.0.0.1 " + errorType

        logging.info(string)
        if self.modo == 'debug':
            print(string)

     def TO(self, timeoutType):
        logging.basicConfig(filename = self.fileLogs, filemode="a", level=logging.INFO, format= "%(asctime)s.%(msecs)03d %(message)s", datefmt='%d:%m:%Y.%H:%M:%S')
        string = "TO " + timeoutType

        logging.info(string)
        if self.modo == 'debug':
            print(string)

     def SP(self, reason):
        logging.basicConfig(filename = self.fileLogs, filemode="a", level=logging.INFO, format= "%(asctime)s.%(msecs)03d %(message)s", datefmt='%d:%m:%Y.%H:%M:%S')
        string = "SP 127.0.0.1 " + reason

        logging.info(string)
        if self.modo == 'debug':
            print(string)

     def ST(self, port, timeout, mode):
        logging.basicConfig(filename = self.fileLogs, filemode="a", level=logging.INFO, format= "%(asctime)s.%(msecs)03d %(message)s", datefmt='%d:%m:%Y.%H:%M:%S')
        string = "ST 127.0.0.1 " + port + " " + timeout + " " + mode
        
        logging.info(string)
        if self.modo == 'debug':
            print(string)