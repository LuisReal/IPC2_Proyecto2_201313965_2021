class NodoProducto:
    def __init__(self, nombre_producto, elaboracion):   
        self.nombre_producto = nombre_producto
        self.elaboracion = elaboracion
        
        self.next = None

    def setNombreProducto(self, nombre_producto):
      self.nombre_producto = nombre_producto

    def getNombreProducto(self):
      return self.nombre_producto


    def setElaboracion(self, elaboracion):
      self.elaboracion = elaboracion

    def getElaboracion(self):
      return self.elaboracion

    def setNext(self, next):
      self.next = next
    
    def getNext(self):
      return self.next


class ListaProductos:
  def __init__(self):
    self.primero = None
  
  def insertar(self, nodo_nuevo): # recibe un NodoProducto con los valoes = nombre_producto, elaboracion
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
      print("(NombreProducto:",node.getNombreProducto()," Elaboracion:", node.getElaboracion(), end = " => ")
      node = node.next
    print()

  def eliminar(self, nombre_producto): 
    current = self.primero
    previous = None

    while current and current.getNombreProducto() != nombre_producto:
      previous = current
      current = current.next

    if previous is None:
      self.primero = current.next
    elif current:
      previous.next = current.next
      current.next = None