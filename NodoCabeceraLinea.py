from ListaLineaProduccion import linked_list

class NodoCabeceraLinea:

    def __init__(self, numero_linea):
        
        self.numero_linea = numero_linea 
        self.next = None   
        self.lista_linea = linked_list()

    def getNumeroLinea(self):
        return self.numero_linea
    
    def setNumeroLinea(self, numero_linea):
        self.numero_linea = numero_linea

    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next = next

    
