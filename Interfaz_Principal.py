
from tkinter import *
from tkinter import ttk
from PyQt5.QtCore import center 
from PyQt5.QtWidgets import *
from tkinter import messagebox, filedialog
from Lectura_Archivo import Lectura_Archivo
from Cronometro import Cronometro
import os
import time
from Hilos import Hilos
import xml.etree.ElementTree as ET

class Interfaz(QMainWindow):

    def __init__(self):
        
        raiz = Tk()
        raiz.title('Ventana')
        #raiz.resizable(100,500)
        #raiz.geometry("700x500")
        raiz.config(bg="#5F9EA0")
        self.miMarco = Frame()
        self.miMarco.pack()
        self.miMarco.config(bg="#F5F5F5")
        self.miMarco.config(width="700", height="500")
        self.opciones = ['Archivo Maquina', 'Archivo Simulacion']
        self.carga = Lectura_Archivo()
        
        self.text = ""
        self.creacionWidgets()
        
        self.crearTabla()
        self.proceso = 0
        
        raiz.mainloop()
        
        self.archivo_simulacion= ""
        self.archivo_maquina = ""
        self.root_simulacion = ""
        self.tabla = ""
        self.tiempo_ensamblaje = ""
        self.hilos = ""
        self.Label_cronometro = ""

    def opcionSeleccionada(self, *args):
        
        if self.opcion_seleccionada.get() == "Archivo Maquina":
            
            self.archivo_maquina = filedialog.askopenfile(title="Cargar Archivo Maquina") # se obtiene la ruta   
            
            self.carga.configurarMaquina(self.archivo_maquina, "2", "Smartwatch")

            messagebox.showinfo("Message", "SE CARGO EL ARCHIVO MAQUINA")

            
            Productos = self.carga.menuProductos # revisar------------------:) (RECIVE UNA LISTA DE PRODUCTOS [])

            self.producto_seleccionado = StringVar()
            self.producto_seleccionado.set('Nombre Producto')
            
            menuProducto = OptionMenu(self.miMarco, self.producto_seleccionado, *Productos, command=self.productoSeleccionado  )
            menuProducto.grid(row=1, column=1, padx=10, pady=10)
            menuProducto.config(width =15,  font=("Comic Sans MS", 12), bg="#7FFFD4", bd=3)  
            
        elif self.opcion_seleccionada.get() == "Archivo Simulacion":
            
            self.archivo_simulacion = filedialog.askopenfile(title="Cargar Archivo Simulacion") 

            doc = ET.parse(self.archivo_simulacion)
            self.root_simulacion = doc.getroot() 
            
            #self.carga.cargaSimulacion(self.root_simulacion)

            messagebox.showinfo("Message", "SE CARGO EL ARCHIVO SIMULACION")

    def productoSeleccionado(self, *args):
        print("Producto seleccionado: ", self.producto_seleccionado.get())


    def creacionWidgets(self):
        

        self.opcion_seleccionada = StringVar()
        self.opcion_seleccionada.set('Archivo')

        menu = OptionMenu(self.miMarco, self.opcion_seleccionada, *self.opciones, command=self.opcionSeleccionada  )
        menu.grid(row=0, column=0, padx=2, pady=2, sticky=W)
        menu.config(width =15,  font=("Comic Sans MS", 14), bg="#7FFFD4", bd=3, fg='#34495E')      

        Boton_Reportes = Button(self.miMarco, text='Reportes', font=("Comic Sans MS", 14), width=10, height=1, bd=3)
        Boton_Reportes.grid(row=0, column=1, padx=10, pady=10)
        
        Boton_Ayuda = Button(self.miMarco, text='Ayuda', font=("Comic Sans MS", 14), width=10, height=1, bd=3)
        Boton_Ayuda.grid(row=0, column=2, padx=10, pady=10)

        Label_nombreProducto = Label(self.miMarco, text="Nombre Producto", fg='#FDFEFE',  font=("Comic Sans MS", 14), 
        width= 15, height=1, bg='#34495E', borderwidth=3, relief="sunken" )
        Label_nombreProducto.grid(row=1, column=0, padx=1, pady=10, sticky=E)
 

        Boton_Start = Button(self.miMarco, text='Start', font=("Comic Sans MS", 14), command=self.ensamblar, width=5, height=1, bd=1)
        Boton_Start.grid(row=3, column=2, padx=1, pady=10, sticky=W)

        self.Label_cronometro = Label(self.miMarco, fg='#FDFEFE',  font=("Comic Sans MS", 14), 
        width= 10, height=1, bg='#34495E', borderwidth=1, relief="sunken" )
        self.Label_cronometro.grid(row=2, column=2, padx=1, pady=10)

        Boton_Stop = Button(self.miMarco, text='Stop', font=("Comic Sans MS", 14), command=self.stopCronometro, width=5, height=1, bd=1)
        Boton_Stop.grid(row=3, column=2, padx=1, pady=1, sticky=E)
        
        #self.cronometro()
        
    def ensamblar(self):

        
        
        for elemento in self.root_simulacion.findall('./ListadoProductos/Producto'): # archivo simulacion_1
            
            producto_simular = elemento.text
            
            for producto in self.carga.root_machine.findall('./ListadoProductos/Producto'):

                nombre_producto = producto.find('./nombre').text    # archivo maquina

                elaboracion = producto.find('./elaboracion').text

                if producto_simular == nombre_producto:

                    lista_elaboracion = elaboracion.split()  
                    
                    for i in range(len(lista_elaboracion)):
                        instruccion = lista_elaboracion[i]

                        for linea in self.carga.root_machine.findall('./ListadoLineasProduccion/LineaProduccion'): 
            
                            if instruccion[1:2] == linea.find('./Numero').text:
                                
                                linea_simular = int(linea.find('./Numero').text)
        
                                self.tiempo_ensamblaje = int(linea.find('./TiempoEnsamblaje').text)

                            
                                componente_ensamblar = int(instruccion[3:4])       
             
                                self.hilos = Hilos(producto_simular, linea_simular, self.tiempo_ensamblaje, componente_ensamblar, self.carga.root_machine, self.tabla, self.carga, self.Label_cronometro )

                                #self.startCronometro()
        
    '''
    def startCronometro(self, contador = 1):
        
        self.Label_cronometro['text'] = contador
        self.Label_cronometro['bg'] = '#00FF00'
        self.proceso=self.Label_cronometro.after(1000, self.startCronometro, (contador+1))
    '''
                     

    def stopCronometro(self):
        self.Label_cronometro['bg'] = '#FF0000'
        self.Label_cronometro.after_cancel(self.proceso)
        

    def crearTabla(self):
    
        self.tabla = ttk.Treeview(self.miMarco, columns= [f"#{n}" for n in range(1, 5)])
        self.tabla.grid(row=1, column=3, rowspan=3  )

        self.tabla.heading("#0", text="Tiempo", anchor=CENTER)
        self.tabla.heading("#1", text="Producto1", anchor=CENTER)
        self.tabla.heading("#2", text="Linea1", anchor=CENTER)
        self.tabla.heading("#3", text="Producto2", anchor=CENTER)
        self.tabla.heading("#4", text="Linea2", anchor=CENTER)
    
        self.tabla.column("#0", width=80, anchor=CENTER)
        self.tabla.column("#1", width=80, anchor=CENTER)
        self.tabla.column("#2", width=80, anchor=CENTER )
        self.tabla.column("#3", width=80, anchor=CENTER )
        self.tabla.column("#4", width=80, anchor=CENTER )


obj = Interfaz()
