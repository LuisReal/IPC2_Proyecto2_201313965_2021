from ListaLineaProduccion import linked_list
from ListadoProductos import ListaProductos, NodoProducto
from ListadoLineas import ListadoLineas

class Ensamblado:
    def __init__(self):
        self.linea_produccion = linked_list()
        self.lista_productos = ListaProductos()
        self.lista_lineas = ListadoLineas()

    def setLineaProduccion(self, nombre_producto, elaboracion):
        self.lista_productos.buscarProducto(nombre_producto).setElaboracion(elaboracion)
        self.lista_productos.insertar(NodoProducto(self.nombre_producto, self.elaboracion))