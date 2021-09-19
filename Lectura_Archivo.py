
import xml.etree.ElementTree as ET

from ListadoLineas import ListadoLineas
from ListaProductos import ListaProductos, NodoProducto
from ListaComponentes import NodoComponente, ListaComponentes

class Lectura_Archivo:
    def __init__(self):
        
        self.cant_componentes = 0
        self.tiempo_ensamblaje = 0
        self.numero_Linea = 0
        self.num_linea_ensamblaje = 0
        self.nombre_producto = ""
        self.elaboracion = ""
        self.producto_simulado = ""
        self.menuProductos = []
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

        self.listado_lineas = ListadoLineas()

        for elemento in root.findall('./ListadoLineasProduccion/LineaProduccion'): 
            
            #if int(elemento.find('./Numero').text) == self.numero_Linea: 
            self.num_linea_ensamblaje = int(elemento.find('./Numero').text)
            #print('\n El numero de linea ensamblaje es ', self.num_linea_ensamblaje)

            self.cant_componentes = int(elemento.find('./CantidadComponentes').text)
            #print('\n La cantidad de componentes es ', self.cant_componentes)

            self.tiempo_ensamblaje = int(elemento.find('./TiempoEnsamblaje').text) 
            #print('\n el tiempo de ensamblaje es ', self.tiempo_ensamblaje)

            
            
            self.listado_lineas.insertar(self.num_linea_ensamblaje, self.cant_componentes, self.tiempo_ensamblaje)
            
            for c in range(self.cant_componentes): # cantidad de componentes = 4 para cada linea
                self.listado_lineas.lineas.buscar(self.num_linea_ensamblaje).lista_linea_produccion.primero.lista_componentes.insertar(NodoComponente(c+1))
            
        
        print("El numero de componentes es: ", self.listado_lineas.lineas.buscar(2).lista_linea_produccion.primero.getComponentes()) # se obtiene el num componentes ingresados
        print("El tiempo de ensamblaje es: ", self.listado_lineas.lineas.buscar(2).lista_linea_produccion.primero.getTiempo()) # se obtiene el tiempo ingresado
        print("Numero Linea: ",self.listado_lineas.lineas.buscar(4).getNumeroLinea(),
        "El Componente BUSCADO es: ",self.listado_lineas.lineas.buscar(4).lista_linea_produccion.primero.lista_componentes.buscar(8).getNumComponente())


        self.lista_productos = ListaProductos()
        

        for elemento in root.findall('./ListadoProductos/Producto'):
                      
            #if elemento.find('./nombre').text == self.busca_producto:
            self.nombre_producto = elemento.find('./nombre').text
            print("el nombre del producto:", self.nombre_producto)
            self.elaboracion = elemento.find('./elaboracion').text
            print("La elaboracion:", self.elaboracion)
            
            self.lista_productos.insertar(NodoProducto(self.nombre_producto, self.elaboracion))
            self.lista_productos.buscarProducto(self.nombre_producto).setElaboracion(self.elaboracion)
                

            self.menuProductos.append(self.lista_productos.buscarProducto(self.nombre_producto).getNombreProducto())
            
        self.lista_productos.imprimir()

    def cargaSimulacion(self, archivo):
        
        xmlfile = archivo
        

        doc = ET.parse(xmlfile)
        root = doc.getroot()
                
        for elemento in root.findall('./ListadoProductos/Producto'): # terreno es el nombre de la etiqueta del archivo robot.xml
            
            self.producto_simulado = elemento.text #Se obtiene el nombre del producto
            print('\n El nombre del producto es ', self.producto_simulado)
                
                
    
        