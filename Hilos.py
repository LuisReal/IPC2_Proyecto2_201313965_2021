from IPC2_Proyecto2_201313965.HiloCronometro import HiloCronometro
import threading
import time
import datetime

from Hilo1 import Hilo1
from Hilo2 import Hilo2


class Hilos:

    def __init__(self, producto_simular, linea_simular, tiempo_ensamblaje, componente_ensamblar, root_machine, tabla, carga, label_cronometro):

        tiempo_ini = datetime.datetime.now()

        #t1 = threading.Thread(name="hilo_1", target= consultar, args= (1, ))
        #t2 = threading.Thread(name="hilo_2", target= guardar, args= (1, "probando hilos"))

        self.h1 = Hilo1(producto_simular,linea_simular, tiempo_ensamblaje, componente_ensamblar, root_machine, tabla, carga)
        self.h2 = Hilo2(producto_simular, linea_simular, tiempo_ensamblaje, componente_ensamblar, root_machine, tabla, carga)
        self.h3 = HiloCronometro(label_cronometro)
        self.h1.start()
        self.h2.start()
        self.h3.start()
        
        self.h1.join()  
        self.h2.join()
        self.h3.join()

        tiempo_fin = datetime.datetime.now()

        print("Tiempo Transcurrido " + str(tiempo_fin.second - tiempo_ini.second))