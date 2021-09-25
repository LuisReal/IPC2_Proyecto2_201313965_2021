
import xml.etree.ElementTree as ET
from ListadoProductos import ListadoProductos
from ListadoLineas import ListadoLineas
from ListaComponentes import NodoComponente, ListaComponentes
from ListaLineaProduccion import NodoLinea


class Lectura_Archivo:
    def __init__(self):
        
        self.cant_componentes = 0
        self.tiempo_ensamblaje = 0
        self.numero_Linea = 0
        self.num_linea_ensamblaje = 0
        self.nombre_producto = ""
        self.elaboracion = ""
        self.producto_simulado = ""
        self.menuProductos = []  # se utiliza para el OptionMenu
        self.busca_producto = ""
        self.lista_ensamblaje = ""
        self.listado_productos = ""
        
        self.obj_ensamblar = ""
        self.tiempo_simular = ""

        self.lista = ""
        
        self.archivo_maquina = ""
        self.root_machine = ""
        self.doc = ""

        self.archivo_simulacion = ""
        self.root_simulacion = ""

        self.roots = ""

    def configurarMaquina(self, archivo, numeroLinea, buscaproducto):
    
        archivo_maquina = archivo
        self.numero_Linea = int(numeroLinea)
        self.busca_producto = buscaproducto

        
        doc = ET.parse(archivo_maquina)
        self.root_machine = doc.getroot()


        self.listado_lineas = ListadoLineas()
        self.listado_productos = ListadoProductos()
        
        for elemento in self.root_machine.findall('./ListadoProductos/Producto'):
            
            self.nombre_producto = elemento.find('./nombre').text
            
            self.elaboracion = elemento.find('./elaboracion').text

            self.listado_productos.insertar(self.nombre_producto, self.elaboracion)
            
            for elemento in self.root_machine.findall('./ListadoLineasProduccion/LineaProduccion'): 
            
            
                self.num_linea_ensamblaje = int(elemento.find('./Numero').text)
            

                self.cant_componentes = int(elemento.find('./CantidadComponentes').text)
            

                self.tiempo_ensamblaje = int(elemento.find('./TiempoEnsamblaje').text)    
            
            
                self.listado_productos.lista_productos.buscarProducto(self.nombre_producto).lista_linea_produccion.insertar(NodoLinea(self.num_linea_ensamblaje, self.cant_componentes, self.tiempo_ensamblaje))
            
                for c in range(self.cant_componentes): # cantidad de componentes = 4 para cada linea
                    #self.listado_lineas.lineas.buscar(self.num_linea_ensamblaje).lista_linea_produccion.primero.lista_componentes.insertar(NodoComponente(c+1))
                    self.listado_productos.lista_productos.buscarProducto(self.nombre_producto).lista_linea_produccion.buscar(self.num_linea_ensamblaje).lista_componentes.insertar(NodoComponente(c+1))
            
            self.menuProductos.append(self.listado_productos.lista_productos.buscarProducto(self.nombre_producto).getNombreProducto())

        

        '''
        print("El producto: ",self.listado_productos.lista_productos.buscarProducto("USBStick").getNombreProducto(),
        " De la linea L: ",self.listado_productos.lista_productos.buscarProducto("USBStick").lista_linea_produccion.buscar(4).getNumeroLinea(),
        " El componente es C: ",self.listado_productos.lista_productos.buscarProducto("USBStick").lista_linea_produccion.buscar(4).lista_componentes.buscar(9).getNumComponente())
        
        '''
        
    
    def cargaSimulacion(self, root_simulacion):
            
        

        #print("self.root_simulacion ", self.root_simulacion)
        #print("self.root_machine ", self.root_machine)

        for elemento in root_simulacion.findall('./ListadoProductos/Producto'): # archivo simulacion_1
            
            producto_simular = elemento.text
            
            for producto in self.root_machine.findall('./ListadoProductos/Producto'):

                nombre_producto = producto.find('./nombre').text    # archivo maquina

                elaboracion = producto.find('./elaboracion').text

                if producto_simular == nombre_producto:

                    lista_elaboracion = elaboracion.split()  
                    
                    for i in range(len(lista_elaboracion)):
                        instruccion = lista_elaboracion[i]

                        for linea in self.root_machine.findall('./ListadoLineasProduccion/LineaProduccion'): 
            
                            if instruccion[1:2] == linea.find('./Numero').text:
                                
                                linea_simular = int(linea.find('./Numero').text)
        
                                self.tiempo_simular = int(linea.find('./TiempoEnsamblaje').text)
                                print("tiempo_simular", self.tiempo_simular)
        '''
        
        for elemento in root_simulacion.findall('./ListadoProductos/Producto'):
            
            producto_simular = elemento.text
          
            for producto in self.root_machine.findall('./ListadoProductos/Producto'):

                nombre_producto = producto.find('./nombre').text

                if producto_simular == nombre_producto:

                    elaboracion = producto.find('./elaboracion').text
            
                    lista_elaboracion = elaboracion.split()            

                    for i in range(len(lista_elaboracion)): # el for empieza desde 0
                        instruccion = lista_elaboracion[i]
       
                        print("El producto: ",self.listado_productos.lista_productos.buscarProducto(nombre_producto).getNombreProducto(),
                        " De la linea L: ",self.listado_productos.lista_productos.buscarProducto(nombre_producto).lista_linea_produccion.buscar(int(instruccion[1:2])).getNumeroLinea(),
                        " El componente es C: ",self.listado_productos.lista_productos.buscarProducto(nombre_producto).lista_linea_produccion.buscar(int(instruccion[1:2])).lista_componentes.buscar(int(instruccion[3:4])).getNumComponente())
        '''
                
    
        