from IPC2_Proyecto2_201313965.ListaComponenteProductos import NodoComponenteProductos
from ListaLineasProductos import ListaLineasProductos, NodoLineasProductos


class NodoProducto:
    def __init__(self, nombre_producto, elaboracion):   
        self.nombre_producto = nombre_producto
        self.elaboracion = elaboracion
    
        self.lista_lineas_productos = ListaLineasProductos() 
        self.next = None

    def setNombreProducto(self, nombre_producto):
      self.nombre_producto = nombre_producto

    def getNombreProducto(self):
      return self.nombre_producto

    
    def setElaboracion(self, elaboracion):
      lista_elaboracion = elaboracion.split()

      for i in range(len(lista_elaboracion)): # el for empieza desde 0
        instruccion = lista_elaboracion[i]
        #---------------PENDIENTE DE REVISAR SIGUIENTE LINEA(ABAJO) QUE NO INSERTE DOS VECES LA MISMA LINEA----
        self.lista_lineas_productos.insertar(NodoLineasProductos(int(instruccion[1:2])))  
        #------------------P E N D I E N T E      R E V I S A R   L I N E A   A R R I B A ------------------
        if int(instruccion[1:2]) == 1: 

          self.lista_lineas_productos.buscarLineaProducto(int(instruccion[1:2])).lista_componente_productos.insertar(NodoComponenteProductos(int(instruccion[3:4]))) 

        elif int(instruccion[1:2]) == 2: 
          self.lista_lineas_productos.buscarLineaProducto(int(instruccion[1:2])).lista_componente_productos.insertar(NodoComponenteProductos(int(instruccion[3:4]))) 

      print("Busqueda de COMPONENTE de Linea a Elaborar",
      self.lista_lineas_productos.buscarLineaProducto(1).lista_componente_productos.buscarComponente(2).getNumComponente())
      
      
    def getElaboracion(self):      
      return self.elaboracion # se utiliza en metodo de imprimir() en ListaProductos

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
      print("(NombreProducto:",node.getNombreProducto()," Elaboracion:", node.getElaboracion(),") ", end = " => ")
      node = node.next
    print()

  def buscarProducto(self, nombre_producto):

    if self.primero is not None: # si la cabecera no esta vacia
            
      temp = self.primero
      while (temp != None): # mientras que el NodoProducto no este vacio
        if temp.getNombreProducto() == nombre_producto:
          return temp #retorna el NodoProducto que contiene el nombre del producto
                
        temp = temp.getNext()  # pasa al siguiente nodo
    else:
      return None
    

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