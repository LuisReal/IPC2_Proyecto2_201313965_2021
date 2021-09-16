import xml.etree.ElementTree as ET
from ListaLineaProduccion import linked_list, NodoLinea
from ListadoLineas import Matriz
from ListadoProductos import ListaProductos, NodoProducto


class Lectura_Archivo:
    def __init__(self):
        
        self.cant_componentes = 0
        self.tiempo_ensamblaje = 0
        self.numero_Linea = 0
        self.num_linea_ensamblaje = 0
        self.nombre_producto = ""
        self.elaboracion = ""
        self.producto_simulado = ""
        #self.menuProductos = []
        self.busca_producto = ""
        self.lista_ensamblaje = ""
        self.lista_productos = ""

        self.lista = ""
        
   
    def configurarMaquina(self, archivo, numeroLinea, buscaproducto):
    
        xmlfile = archivo
        self.numero_Linea = int(numeroLinea)
        self.busca_producto = buscaproducto

        doc = ET.parse(xmlfile)
        root = doc.getroot()

        print("Lograste acceder")

        self.lista = Matriz()

        for elemento in root.findall('./ListadoLineasProduccion/LineaProduccion'): # terreno es el nombre de la etiqueta del archivo robot.xml
            
            #if int(elemento.find('./Numero').text) == self.numero_Linea: # se compara el nombre del terreno que se ingresa con el del archivo xml
            self.num_linea_ensamblaje = int(elemento.find('./Numero').text)
            #print('\n El numero de linea ensamblaje es ', self.num_linea_ensamblaje)

            self.cant_componentes = int(elemento.find('./CantidadComponentes').text)
            #print('\n La cantidad de componentes es ', self.cant_componentes)

            self.tiempo_ensamblaje = int(elemento.find('./TiempoEnsamblaje').text) #se busca el valor de dimension m solamente para el terreno ingresado
            #print('\n el tiempo de ensamblaje es ', self.tiempo_ensamblaje)

            
            
            self.lista.insertar(self.num_linea_ensamblaje, self.cant_componentes, self.tiempo_ensamblaje)

        print("El numero de componentes es: ", self.lista.lineas.buscar(1).lista_linea.primero.getComponentes())
        print("El tiempo de ensamblaje es: ", self.lista.lineas.buscar(1).lista_linea.primero.getTiempo())

        
        #lista.eliminar(2)
        #print()
        
        #lista.imprimir()

        self.lista_productos = ListaProductos()

        for elemento in root.findall('./ListadoProductos/Producto'): # terreno es el nombre de la etiqueta del archivo robot.xml
            
            
            if elemento.find('./nombre').text == self.busca_producto: # se compara el nombre del terreno que se ingresa con el del archivo xml
                self.nombre_producto = elemento.find('./nombre').text
                #print('\n El nombre del producto es ', self.nombre_producto)
                self.elaboracion = elemento.find('./elaboracion').text
                #print('\n La elaboracion es ', self.elaboracion)
        
                self.lista_productos.insertar(NodoProducto(self.nombre_producto, self.elaboracion))
        self.lista_productos.imprimir()

    def cargaSimulacion(self, archivo):
        
        xmlfile = archivo
        

        doc = ET.parse(xmlfile)
        root = doc.getroot()
                
        for elemento in root.findall('./ListadoProductos/Producto'): # terreno es el nombre de la etiqueta del archivo robot.xml
            
            self.producto_simulado = elemento.text #Se obtiene el nombre del producto
            print('\n El nombre del producto es ', self.producto_simulado)
                
                
    
        