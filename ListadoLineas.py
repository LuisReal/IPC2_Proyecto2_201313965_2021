from ListaCabeceraLinea import ListaCabeceraLinea
from NodoCabeceraLinea import NodoCabeceraLinea
from ListaLineaProduccion import NodoLinea
from ListaProductos import ListaProductos

class ListadoLineas:

    def __init__(self):
        self.lineas = ListaCabeceraLinea()
        self.lista_productos = ListaProductos()

    def insertar(self, num_linea, componentes, tiempo):
        
        nodoNuevo = NodoLinea(num_linea, componentes, tiempo)

        if self.lineas.buscar(num_linea) == None: 
            self.lineas.insertar(NodoCabeceraLinea(num_linea)) 

        tempC = self.lineas.buscar(num_linea) # devuelve un NodoCabeceraLinea contiene(ListaLineaProduccion)
        tempC.lista_linea_produccion.insertar(nodoNuevo) 
        
        #print("se inserto numLineas:", num_linea," componentes:", componentes, " tiempo:", tiempo)

