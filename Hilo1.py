
import threading
import time



class Hilo1(threading.Thread):

    def __init__(self, producto_simular, linea_simular, tiempo_ensamblaje, componente_ensamblar, root_machine, tabla, carga):
        
        threading.Thread.__init__(self, name = producto_simular, target= Hilo1.run)
        self.producto_simular = producto_simular
        self.linea_simular = linea_simular
        self.tiempo_ensamblaje = tiempo_ensamblaje
        self.tabla = tabla
        self.componente_ensamblar = componente_ensamblar
        self.root_machine = root_machine
        self.carga = carga
        self.tiempo = 0
    
    def run(self):
        self.consultar(self.producto_simular, self.linea_simular, self.tiempo_ensamblaje, self.componente_ensamblar, self.root_machine, self.tabla, self.carga)
    
    def setTiempo(self, tiempo):
        self.tiempo = tiempo
    
    def getTiempo(self):
        return self.tiempo
    
    def consultar(self, producto_simular, linea_simular, tiempo_ensamblaje, componente_ensamblar, root_machine, tabla, carga):

        componente = 1
        
        if componente <= componente_ensamblar: # smartwatch simulacion = smartwatch maquina.xml
                    
            producto1 = carga.listado_productos.lista_productos.buscarProducto(producto_simular).getNombreProducto()
            #linea = self.carga.listado_productos.lista_productos.buscarProducto("Smartwatch").lista_linea_produccion.buscar(1).getNumeroLinea()
            componenteL1 = carga.listado_productos.lista_productos.buscarProducto(producto_simular).lista_linea_produccion.buscar(linea_simular).lista_componentes.buscar(componente).getNumComponente()

            producto2 = carga.listado_productos.lista_productos.buscarProducto("Camara").getNombreProducto()
            #linea = self.carga.listado_productos.lista_productos.buscarProducto("Camara").lista_linea_produccion.buscar(1).getNumeroLinea()
            componenteL2 = carga.listado_productos.lista_productos.buscarProducto("Camara").lista_linea_produccion.buscar(linea_simular).lista_componentes.buscar(componente).getNumComponente()
        
            tabla.insert("", END, text=self.getTiempo() ,values=(producto1, "C"+str(componenteL1), producto2,"C"+str(componenteL2)))

            componente += 1

            
            time.sleep(2)
            return

    