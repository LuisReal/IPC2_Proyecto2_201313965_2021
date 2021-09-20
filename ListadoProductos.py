

from ListaLineaProduccion import ListaLineaProduccion, NodoLinea
from ListaProductos import ListaProductos, NodoProducto

class ListadoProductos:

    def __init__(self):
        
        self.lista_productos = ListaProductos()

    def insertar(self, nombre_producto, elaboracion):

        if self.lista_productos.buscarProducto(nombre_producto) == None: 
            self.lista_productos.insertar(NodoProducto(nombre_producto, elaboracion))

