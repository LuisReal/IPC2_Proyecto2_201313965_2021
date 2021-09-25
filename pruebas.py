from tkinter import *
from tkinter import ttk
from datetime import datetime
import tkinter as tk
from PyQt5.QtCore import center 
from PyQt5.QtWidgets import *
import time
import threading
import queue


def busqueda1(num,cola):
    for i in range(5000):
        if(num == i):
            cola.put("Busqueda1 confirmó el número")
def busqueda2(num,cola):
    for i in range(5000,10000):
        if(num == i):
            cola.put("Busqueda2 confirmó el número")

numero = 4232
cola = queue.Queue()

thread1 = threading.Thread(target=busqueda1,args=(numero,cola))
thread2 = threading.Thread(target=busqueda2,args=(numero,cola))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(cola.get())




