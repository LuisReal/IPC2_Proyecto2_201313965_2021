

from ListaComponentes import NodoComponente, ListaComponentes


class NodoLinea:
    def __init__(self, numero_linea, componentes, tiempo):   
        self.numero_linea = numero_linea
        self.componentes = componentes
        self.tiempo = tiempo
        self.lista_componentes = ListaComponentes()
        self.nada = "No hace nada"
        self.ensamblar_componente = None    # recibe un nodo
        self.next = None

    def setNumeroLinea(self, numero_linea):
      self.numero_linea = numero_linea

    def getNumeroLinea(self):
      return self.numero_linea

    '''
    def setComponentes(self):
      
      for c in range(self.componentes):
        self.lista_componentes.insertar(NodoComponente(c+1))    # se crea la lista de componentes
      print(self.lista_componentes.imprimir())
    '''

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

    def setNada(self, nada):
      self.nada = nada

    def getNada(self):
      return self.nada # devuelve un String "No hace nada"

    def setEnsamblarComponente(self, componente): # recibe el componente a ensamblar
      self.ensamblar_componente = componente

    def getEnsamblarComponente(self):
      return print("Ensamblar ",self.ensamblar_componente)

class ListaLineaProduccion:
  def __init__(self):
    self.primero = None

  def vacia(self):
        return self.primero == None # retorno True o False
  
  def insertar(self, nodo_nuevo): # recibe un NodoLinea con los valoes = numero, componentes, tiempo
    if not self.primero:  # si no existe cabecera
      self.primero = nodo_nuevo # contiene numero de linea, componentes, tiempo
      
    else:
      current = self.primero 
      while current.next != None: #la primera vez que se llama a insertar() no pasa por este while solo por el if not self.head
        current = current.next
      current.next = nodo_nuevo 
  
  def imprimir(self):
    node = self.primero

    while node != None:
      print("(Num:",node.getNumeroLinea()," Comp:", node.getComponentes(),
      " Tiem:", node.getTiempo(),")", end = " => ")
      node = node.next
    print()

  def buscar(self, num_linea):
    if self.vacia() is not None:
            
      temp = self.primero
      while (temp != None):
        if temp.getNumeroLinea() == num_linea:
          return temp
                
        temp = temp.getNext()
    else:
      return None

  def eliminar(self, numero_linea): # elimina el numero de linea de ensamblaje
    current = self.primero
    previous = None

    while current and current.getNumeroLinea() != numero_linea:
      previous = current
      current = current.next

    if previous is None:
      self.primero = current.next
    elif current:
      previous.next = current.next
      current.next = None