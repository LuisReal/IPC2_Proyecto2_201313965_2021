
from ListadoProductos import ListadoProductos


class EnsamblarProducto:

    def __init__(self):
        
        self.listado_productos = ListadoProductos()
    
    def buscarProductoElaborar(self, nombre_producto, elaboracion):
      lista_elaboracion = elaboracion.split()

      for i in range(len(lista_elaboracion)): # el for empieza desde 0
        instruccion = lista_elaboracion[i]
       
        print("El producto: ",self.lectura_archivo.listado_productos.lista_productos.buscarProducto("Smartwatch").getNombreProducto(),
        " De la linea L: ",self.lectura_archivo.listado_productos.lista_productos.buscarProducto("Smartwatch").lista_linea_produccion.buscar(int(instruccion[1:2])).getNumeroLinea(),
        " El componente es C: ",self.lectura_archivo.listado_productos.lista_productos.buscarProducto("Smartwatch").lista_linea_produccion.buscar(int(instruccion[1:2])).lista_componentes.buscar(int(instruccion[3:4])).getNumComponente())

        
