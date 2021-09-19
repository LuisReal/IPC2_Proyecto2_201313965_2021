from ListaComponenteProductos import ListaComponenteProductos

class NodoLineasProductos:
    def __init__(self, linea_producto):   
        self.linea_producto = linea_producto
    
        self.lista_componente_productos = ListaComponenteProductos() # cada producto va a tener su lista de elaboracion
        self.next = None

    def setLineaProducto(self, linea_producto):
      self.linea_producto = linea_producto

    def getLineaProducto(self):
      return self.linea_producto


    def setNext(self, next):
      self.next = next
    
    def getNext(self):
      return self.next


class ListaLineasProductos:
  def __init__(self):
    self.primero = None
  
  def insertar(self, nodo_nuevo): # recibe un NodoLineasProductos 
    if not self.primero:  # si no existe cabecera
      self.primero = nodo_nuevo 
      
    else:
      current = self.primero 
      while current.next != None: #la primera vez que se llama a insertar() no pasa por este while solo por el if not self.head
        current = current.next
      current.next = nodo_nuevo 
  
  def imprimir(self):
    node = self.primero

    while node != None:
      print("(NumeroLinea:",node.getLineaProducto(),") ", end = " => ")
      node = node.next
    print()

  def buscarLineaProducto(self, num_linea):

    if self.primero is not None: # si la cabecera no esta vacia
            
      temp = self.primero
      while (temp != None): # mientras que el NodoLineasProductos no este vacio
        if temp.getLineaProducto() == num_linea:
          return temp #retorna el NodoLineasProductos
                
        temp = temp.getNext()  # pasa al siguiente nodo
    else:
      return None
    

  def eliminar(self, num_linea): 
    current = self.primero
    previous = None

    while current and current.getLineaProducto() != num_linea:
      previous = current
      current = current.next

    if previous is None:
      self.primero = current.next
    elif current:
      previous.next = current.next
      current.next = None