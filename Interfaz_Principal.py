from tkinter import * 

class Interfaz:

    def __init__(self):
        
        raiz = Tk()
        raiz.title('Ventana')
        #raiz.resizable(100,500)
        #raiz.geometry("700x500")
        raiz.config(bg="blue")
        miMarco = Frame()
        miMarco.pack(fill="both", expand="True")
        miMarco.config(bg="red")
        miMarco.config(width="700", height="500")

        Boton_Archivo = Button(miMarco, text='Archivo', font=("Comic Sans MS", 14), width=10, height=1, bd=3)
        Boton_Archivo.grid(row=0, column=0, padx=10, pady=10)


        Boton_Reportes = Button(miMarco, text='Reportes', font=("Comic Sans MS", 14), width=10, height=1, bd=3)
        Boton_Reportes.grid(row=0, column=1, padx=10, pady=10)
        
        Boton_Ayuda = Button(miMarco, text='Ayuda', font=("Comic Sans MS", 14), width=10, height=1, bd=3)
        Boton_Ayuda.grid(row=0, column=2, padx=10, pady=10)
        
        
        raiz.mainloop()


obj = Interfaz()
