import threading
import time

class HiloCronometro(threading.Thread):

    def __init__(self, label_cronometro):
        threading.Thread.__init__(self, name = "Cronometro", target= HiloCronometro.run)
        self.label_cronometro = label_cronometro
        
    
    def run(self):
        self.startCronometro()
    
    
    def startCronometro(self, contador = 1):
        
        self.label_cronometro['text'] = contador
        self.label_cronometro['bg'] = '#00FF00'
        self.proceso=self.label_cronometro.after(1000, self.startCronometro, (contador+1))
        