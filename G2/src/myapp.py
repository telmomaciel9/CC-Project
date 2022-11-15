import sys

class MYAPP:
    def __init__(self):
        self.dnsDestinoIP = ""
        self.queryName = ""
        self.queryType = ""
        self.modo = ""
    
    def parseCommandLine(self):
        self.dnsDestinoIP = sys.argv[1]
        self.queryName = sys.argv[2]
        self.queryType = sys.argv[3]
        self.modo = sys.argv[4]
        
    def __str__(self):
        out = ""
        out = out +  self.dnsDestinoIP + " - " + self.queryName + " - " + self.queryType + " - " + self.modo
        return out 
        