import datetime

class Writer:
     def escreve_log(self,diretoria):
          with open(diretoria, "a") as f:
               date = datetime.datetime.now()
               data_formatada = str(date.day) + ":" + str(date.month) + ":" + str(date.year) + "." + str(date.hour) + ":" + str(date.minute) + ":" + str(date.second) + ":" + str(round(date.microsecond,3))
               
               
