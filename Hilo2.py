import threading
import time

class Hilo2(threading.Thread):

    def __init__(self, nombre_hilo, nombre_producto, tiempo, tabla):
        threading.Thread.__init__(self, name = nombre_hilo, target= Hilo2.run)
        self.nombre_hilo = nombre_hilo
        self.nombre_producto = nombre_producto
        self.tiempo = tiempo
        self.tabla = tabla
    
    def run(self):
        self.guardar(self.nombre_producto, self.tiempo, self.tabla)
    
    def guardar(self, nombre_producto, tiempo, tabla):
        print("El nombre del producto es ", nombre_producto, " El tiempo es ", tiempo)
        time.sleep(1)
        return