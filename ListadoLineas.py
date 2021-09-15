from ListaCabeceraLinea import ListaCabeceraLinea
from NodoCabeceraLinea import NodoCabeceraLinea
from ListaLineaProduccion import NodoLinea


class Matriz:

    def __init__(self):
        self.lineas = ListaCabeceraLinea()
        

    def insertar(self, num_linea, componentes, tiempo):
        
        nodoNuevo = NodoLinea(num_linea, componentes, tiempo)

        if self.lineas.buscar(num_linea) == None: 
            self.lineas.insertar(NodoCabeceraLinea(num_linea)) 

        tempC = self.lineas.buscar(num_linea)
        tempC.lista_linea.insertar(nodoNuevo) 
        
        print("se inserto numLineas:", num_linea," componentes:", componentes, " tiempo:", tiempo)