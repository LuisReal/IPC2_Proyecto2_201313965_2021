import sys
from tkinter import *
from tkinter import ttk 
from PyQt5.QtWidgets import *
from tkinter import messagebox, filedialog
from Lectura_Archivo import CargaArchivo

class Interfaz(QMainWindow):

    

    def __init__(self):
        
        raiz = Tk()
        raiz.title('Ventana')
        #raiz.resizable(100,500)
        #raiz.geometry("700x500")
        raiz.config(bg="blue")
        self.miMarco = Frame()
        self.miMarco.pack()
        self.miMarco.config(bg="red")
        self.miMarco.config(width="700", height="500")

        
        self.creacionWidgets()
        self.crearTabla()
        raiz.mainloop()
    
    def cargarArchivo(self):

        archivo = filedialog.askopenfile(title="Cargar Archivo")

        CargaArchivo().configurarMaquina(archivo, "1")

        messagebox.showinfo("Message", "SE CARGO EL ARCHIVO")

    def creacionWidgets(self):
        
        Boton_Archivo = Button(self.miMarco, text='Archivo', command = self.cargarArchivo, font=("Comic Sans MS", 14), width=10, height=1, bd=3)
        Boton_Archivo.grid(row=0, column=0, padx=10, pady=10)


        Boton_Reportes = Button(self.miMarco, text='Reportes', font=("Comic Sans MS", 14), width=10, height=1, bd=3)
        Boton_Reportes.grid(row=0, column=1, padx=10, pady=10)
        
        Boton_Ayuda = Button(self.miMarco, text='Ayuda', font=("Comic Sans MS", 14), width=10, height=1, bd=3)
        Boton_Ayuda.grid(row=0, column=2, padx=10, pady=10)

        Label_nombreProducto = Label(self.miMarco, text="Nombre Producto", font=("Comic Sans MS", 14), width= 15, height=1, bd=3)
        Label_nombreProducto.grid(row=1, column=1, padx=10, pady=10)

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
