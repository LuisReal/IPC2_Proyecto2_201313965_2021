import sys
from tkinter import *
from tkinter import ttk
from PyQt5.QtCore import center 
from PyQt5.QtWidgets import *
from tkinter import messagebox, filedialog
from Lectura_Archivo import CargaArchivo

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
        
        self.creacionWidgets()
        self.crearTabla()
        raiz.mainloop()

    def opcionSeleccionada(self, *args):
        

        if self.opcion_seleccionada.get() == "Archivo Maquina":
            
            archivo_maquina = filedialog.askopenfile(title="Cargar Archivo Maquina") # se obtiene la ruta
    
            carga1 = CargaArchivo()
            carga1.configurarMaquina(archivo_maquina, "2", "Producto2")

            messagebox.showinfo("Message", "SE CARGO EL ARCHIVO MAQUINA")

            
            Productos = carga1.menuProductos

            self.producto_seleccionado = StringVar()
            self.producto_seleccionado.set('Nombre Producto')
            menuProducto = OptionMenu(self.miMarco, self.producto_seleccionado, *Productos, command=self.productoSeleccionado  )
            menuProducto.grid(row=1, column=1, padx=10, pady=10)
            menuProducto.config(width =15,  font=("Comic Sans MS", 12), bg="#7FFFD4", bd=3)  
            
        elif self.opcion_seleccionada.get() == "Archivo Simulacion":
            
            archivo_simulacion = filedialog.askopenfile(title="Cargar Archivo Simulacion")
        
            carga2 = CargaArchivo()
            carga2.cargaSimulacion(archivo_simulacion)

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

         

    def crearTabla(self):
    
        tabla = ttk.Treeview(self.miMarco, columns= [f"#{n}" for n in range(1, 4)])
        tabla.grid(row=1, column=3, rowspan=3  )

        tabla.heading("#0", text="Tiempo", anchor=CENTER)
        tabla.heading("#1", text="Linea1", anchor=CENTER)
        tabla.heading("#2", text="Linea2", anchor=CENTER)
        tabla.heading("#3", text="Linea3", anchor=CENTER)
    
        tabla.column("#0", width=80, anchor=CENTER)
        tabla.column("#1", width=80, anchor=CENTER)
        tabla.column("#2", width=80, anchor=CENTER )
        tabla.column("#3", width=80, anchor=CENTER )

        

        tabla.insert("", END, text="3 seg", values=("2.50", "5", "7"))
                        
    

    
obj = Interfaz()
