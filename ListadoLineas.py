from ListaLineaProduccion import ListaLineaProduccion, NodoLinea



class ListadoLineas:

    def __init__(self):
        
        self.lineas = ListaLineaProduccion()
        

    def insertar(self, num_linea, componentes, tiempo):
        
        #nodoNuevo = NodoComponente(num_componente)

        if self.lineas.buscar(num_linea) == None: 
            self.lineas.insertar(NodoLinea(num_linea, componentes, tiempo)) 

        
        #tempC = self.lineas.buscar(num_linea) # devuelve un NodoCabeceraLinea contiene(ListaLineaProduccion)
        #tempC.lista_componentes.insertar(nodoNuevo) 
        
        #print("se inserto numLineas:", num_linea," componentes:", componentes, " tiempo:", tiempo)

