from ListaLineaProduccion import ListaLineaProduccion

class NodoCabeceraLinea:

    def __init__(self, numero_linea):
        
        self.numero_linea = numero_linea 
        self.next = None   
        self.lista_linea_produccion = ListaLineaProduccion()

    def getNumeroLinea(self):
        return self.numero_linea
    
    def setNumeroLinea(self, numero_linea):
        self.numero_linea = numero_linea

    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next = next

    
