from cache import Cache
from parser_db import Parser_BD
from parser_config import Parser_Config
from query import Query
from parser_st import Parser_ST
from logs import Logs
import threading
import socket
import os
import sys
import time
from query import Query
import re
import pickle

class ST:
    
    def __init__(self):
        self.dirConfig = sys.argv[1]
        aux = sys.argv[2].split(":")
        self.ip = aux[0]
        self.porta = int(aux[1])
        if(len(sys.argv)==5):
            self.timeout = sys.argv[3]
            self.debug = sys.argv[4]
        if(len(sys.argv)==4):
            self.debug = sys.argv[3]
        self.srvConfig = Parser_Config(self.dirConfig)
        self.srvConfig.parse_Config()
        self.logs = Logs(self.srvConfig.dir_logLocal,self.srvConfig.dir_logAll, self.debug)
        self.logs.EV("conf-file-read", self.dirConfig)
        self.logs.EV("log-file-create", self.srvConfig.dir_logLocal)
        self.srvCache = Cache()
        self.srvBD = Parser_BD(self.srvConfig.dir_bd)
        self.srvBD.parse_db(self.srvCache)
        self.logs.EV("database-file-read", self.srvConfig.dir_bd)
        #self.srvST_list = Parser_ST(self.srvConfig.dir_ST)
        #self.query = Query()

    def con_servidor(self):
        print("[SERVER UDP MODE] - STARTING...")
        stUDP = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        stUDP.bind((self.ip, self.porta))
            
        print("[SERVER UDP MODE] - LISTENING...")
        
        
        while True:
            q = Query()
            bytesToSend = "".encode("utf-8")
            (msg,add) = stUDP.recvfrom(1024)
            print(msg.decode('utf-8'))
            q.parse_message_condense(msg.decode('utf-8'))
            self.logs.QR_QE(True, str(add), q.query_info_name + " " + q.query_info_type)
            
            clientIP  = "Client IP Address: {}".format(add)
            clientMsg = "Message from Client:\n -> {}  ".format(msg.decode('utf-8'))
            
            print(clientIP)
            print(clientMsg)
            
            res = q.origina_resposta(self.srvCache,q)
            print(res)
            if q.response_code==0 or q.response_code==1:
                bytesToSend = res.encode("utf-8")

            # Sending a reply to client
            stUDP.sendto(bytesToSend, add)
            
            self.logs.RP_RR(True,str(add),q.query_info_name + " " + q.query_info_type)
            
            
            
        
if __name__ == "__main__":
    srv = ST()
    print(srv.srvCache)
    t1 = threading.Thread(target = srv.con_servidor)
    
    t1.start()