class ListaCabeceraLinea:
    
    def __init__(self):
        self.head = None
        
    def vacia(self):
        return self.head == None # retorno True o False

    def insertar(self, nodoNuevo): # se recive un NodoCabeceraLinea
        
        if self.vacia():
            self.head = nodoNuevo # se ingresa un NodoCabeceraLinea

        else: 
            if nodoNuevo.getX() < self.primero.getX():
                self.agregar_inicio(nodoNuevo)
            

            elif nodoNuevo.getX() > self.ultimo.getX():
                self.agregar_final(nodoNuevo)
            
            else:
                self.insertar_medio(nodoNuevo)
    
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
       

    def recorrer_inicio(self):
        
        if self.vacia() is not None:
            
            tmp = self.primero

            while tmp != None: # mientras que aux != None (mientras que el nodo no este vacio)
                print("x: ", tmp.getX())
                tmp = tmp.getSiguiente()

    def buscar(self, x):
        if self.vacia() is not None:
            
            temp = self.primero
            while (temp != None):
                if temp.getX() == x:
                    return temp
                
                temp = temp.getSiguiente()
        else:
            return None