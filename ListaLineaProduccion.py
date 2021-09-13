'''
class LineaEnsamblaje:
    def __init__(self, numero, componentes, tiempo):
        self.numero = numero
        self.componentes = componentes
        self.tiempo = tiempo
'''
class NodoLinea:
    def __init__(self, numero_linea, componentes, tiempo):   
        self.numero_linea = numero_linea
        self.componentes = componentes
        self.tiempo = tiempo
        self.next = None

    def setNumeroLinea(self, numero_linea):
      self.numero_linea = numero_linea

    def getNumeroLinea(self):
      return self.numero_linea

    def setComponentes(self, componentes):
      self.componentes = componentes

    def getComponentes(self):
      return self.componentes

    def setTiempo(self, tiempo):
      self.tiempo = tiempo

    def getTiempo(self):
      return self.tiempo

    def setNext(self, next):
      self.next = next
    
    def getNext(self):
      return self.next


class linked_list:
  def __init__(self):
    self.head = None
  
  def insertar(self, nodo_nuevo): # recibe un NodoLinea con los valoes = numero, componentes, tiempo
    if not self.head:  # si no existe cabecera
      self.head = nodo_nuevo # contiene numero de linea, componentes, tiempo
      
    else:
      current = self.head 
      while current.next != None: #la primera vez que se llama a insertar() no pasa por este while solo por el if not self.head
        current = current.next
      current.next = nodo_nuevo 
  
  def imprimir(self):
    node = self.head

    while node != None:
      print("(Num:",node.getNumeroLinea()," Comp:", node.getComponentes(),
      " Tiem:", node.getTiempo(),")", end = " => ")
      node = node.next
    print()
  
  '''
    node = self.head

    while node != None:
      print(node.LineaEnsamblaje.componentes, end = "=>")
      node = node.next
    
    node = self.head
    while node != None:
      print(node.LineaEnsamblaje.tiempo, end = "=>")
      node = node.next
  '''

  def eliminar(self, numero_linea): # elimina el numero de linea de ensamblaje
    current = self.head
    previous = None

    while current and current.getNumeroLinea() != numero_linea:
      previous = current
      current = current.next

    if previous is None:
      self.head = current.next
    elif current:
      previous.next = current.next
      current.next = None