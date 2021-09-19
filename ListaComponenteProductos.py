class NodoComponenteProductos:
    def __init__(self, num_componente):   
        
        self.num_componente = num_componente    
        self.next = None

    def setNumComponente(self, num_componente):
      self.num_componente = num_componente

    def getNumComponente(self):
      return self.num_componente

    def setNext(self, next):
      self.next = next
    
    def getNext(self):
      return self.next

class ListaComponenteProductos:
    def __init__(self):
        self.primero = None

    def vacia(self):
        return self.primero == None # retorno True o False
  
    def insertar(self, nodo_nuevo): # recibe un NodoComponenteProductos 
        if not self.primero:  # si no existe cabecera
            self.primero = nodo_nuevo # contiene num_componente
      
        else:
            current = self.primero 
            while current.next != None: #la primera vez que se llama a insertar() no pasa por este while solo por el if not self.head
                current = current.next
            current.next = nodo_nuevo 
  
    def imprimir(self):
        node = self.primero

        while node != None:
            print("(NumComponente:",node.getNumComponente(), ")", end = " => ")
            node = node.next
        print()

  
    def buscarComponente(self, num_componente):
        
        if self.primero is not None:        
            temp = self.primero
            while (temp != None):
                if temp.getNumComponente() == num_componente:
                    return temp
                temp = temp.getNext()
        else:
            return None


    def eliminar(self, num_componente):
        current = self.primero
        previous = None

        while current and current.getNumComponente() != num_componente:
            previous = current
            current = current.next

        if previous is None:
            self.primero = current.next
        elif current:
            previous.next = current.next
            current.next = None