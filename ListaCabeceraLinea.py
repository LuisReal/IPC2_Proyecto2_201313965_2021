class ListaCabeceraLinea:
    
    def __init__(self):
        self.primero = None
        
    def vacia(self):
        return self.primero == None # retorno True o False

    def insertar(self, nodoNuevo): # se recive un NodoCabeceraLinea
        
        if self.vacia():
            self.primero = nodoNuevo # se ingresa un NodoCabeceraLinea

        else:
            if nodoNuevo.getNumeroLinea() > self.primero.getNumeroLinea():
                
                current = self.primero # la cabecera es mi nodo actual
                while current.next != None:
                    current = current.next
                current.next = nodoNuevo
                #self.agregar_final(nodoNuevo)
    '''
    def insertar_medio(self, nodoNuevo):
        tmp1 = self.primero
        while tmp1.getX() < nodoNuevo.getX():
            tmp1 = tmp1.getSiguiente()

        tmp2 = tmp1.getAnterior()
        tmp2.setSiguiente(nodoNuevo)
        nodoNuevo.setSiguiente(tmp1)
        nodoNuevo.setAnterior(tmp2)
        tmp1.setAnterior(nodoNuevo)

    def agregar_inicio(self, nodoNuevo ):
        
        self.primero.setAnterior(nodoNuevo)
        nodoNuevo.setSiguiente(self.primero)
        self.primero = nodoNuevo
        

    def agregar_final(self, nodoNuevo):
        
        self.ultimo.setSiguiente(nodoNuevo)
        nodoNuevo.setAnterior(self.ultimo)
        self.ultimo = nodoNuevo
       
    '''
    def recorrer(self):
        
        if self.vacia() is not None:
            
            tmp = self.primero

            while tmp != None: # mientras que aux != None (mientras que el nodo no este vacio)
                print("Num Linea: ", tmp.getNumeroLinea())
                tmp = tmp.getNext()

    def buscar(self, num_linea):
        if self.vacia() is not None:
            
            temp = self.primero
            while (temp != None):
                if temp.getNumeroLinea() == num_linea:
                    return temp
                
                temp = temp.getNext()
        else:
            return None