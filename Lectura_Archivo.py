import xml.etree.ElementTree as ET

class CargaArchivo:
    def __init__(self):
        self.doc = ""
        
        self.cant_componentes = 0
        self.tiempo_ensamblaje = 0
        self.numero_Linea = 0
        self.nombre_producto = ""
        self.elaboracion = ""
        self.producto_simulado = ""
        
   
    def configurarMaquina(self, archivo, numeroLinea, nombreproducto):
    
        xmlfile = archivo
        self.numero_Linea = int(numeroLinea)
        self.nombre_producto = nombreproducto

        doc = ET.parse(xmlfile)
        root = doc.getroot()

        print("Lograste acceder")


        for elemento in root.findall('./ListadoLineasProduccion/LineaProduccion'): # terreno es el nombre de la etiqueta del archivo robot.xml
            
            if int(elemento.find('./Numero').text) == self.numero_Linea: # se compara el nombre del terreno que se ingresa con el del archivo xml
                self.cant_componentes = int(elemento.find('./CantidadComponentes').text)
                print('\n La cantidad de componentes es ', self.cant_componentes)

                self.tiempo_ensamblaje = int(elemento.find('./TiempoEnsamblaje').text) #se busca el valor de dimension m solamente para el terreno ingresado
                print('\n el tiempo de ensamblaje es ', self.tiempo_ensamblaje)
            
        for elemento in root.findall('./ListadoProductos/Producto'): # terreno es el nombre de la etiqueta del archivo robot.xml
            
            if elemento.find('./nombre').text == self.nombre_producto: # se compara el nombre del terreno que se ingresa con el del archivo xml
                nombre_producto = elemento.find('./nombre').text
                print('\n El nombre del producto es ', nombre_producto)
                self.elaboracion = elemento.find('./elaboracion').text
                print('\n La elaboracion es ', self.elaboracion)

    def cargaSimulacion(self, archivo):
        
        xmlfile = archivo
        

        doc = ET.parse(xmlfile)
        root = doc.getroot()
                
        for elemento in root.findall('./ListadoProductos/Producto'): # terreno es el nombre de la etiqueta del archivo robot.xml
            
            self.producto_simulado = elemento.text #Se obtiene el nombre del producto
            print('\n El nombre del producto es ', self.producto_simulado)
                
                
    
        