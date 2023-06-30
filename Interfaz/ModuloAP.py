from pathlib import Path
from tkinter import *
import tkinter as tk
from pathlib import Path
from tkinter import *
import tkinter as tk
import Interfaz.ListaGramatica
from tkinter import messagebox
from tkinter import filedialog
import Interfaz.MenuPrincipal
from PIL import Image
import Interfaz.ListaGramaticaArbol
import Interfaz.InformacionAutomata
import Clases.GramaticaLDC
import Clases.AutomataPila
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class ModuloAP(tk.Toplevel):
    def __init__(self):
        super().__init__()
       
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width/2) - (1115/2)
        y = (screen_height/2) - (600/2)
        self.geometry("%dx%d+%d+%d" % (1115, 600, x, y))

        self.geometry("1115x600")
        self.configure(bg="#FFFFFF")
        def on_enter(event):
            event.widget.config(bg="#288AC0", fg="white")

        def cargarArchivo():
            self.destroy()
            archivo = filedialog.askopenfilename(filetypes=[("Text files","*.txt")])
            if archivo:
                cargar_archivo(archivo)

        def on_leave(event):
            event.widget.config(bg="#2CCCEF", fg="black")

        def abrir_menu_principal():
            self.destroy()

        button_1 = Button(
            self,
            bg="#2CCCEF",
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            font=("Helvetica", 16),
            text="Cargar Archivo",
            command= cargarArchivo
            
        )
        button_1.bind("<Enter>", on_enter)
        button_1.bind("<Leave>", on_leave)
        button_1.place(x=0.0, y=0.0, width=327.0, height=120.0)

        button_2 = Button(
            self,
            bg="#2CCCEF",
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            text="Informacion del Automata de Pila",
            font=("Helveltica", 16),
            command= lambda: Interfaz.InformacionAutomata.InformacionAutomata()
        )
        button_2.place(
            x=0.0,
            y=120.0,
            width=327.0,
            height=120.0
        )
        button_2.bind("<Enter>", on_enter)
        button_2.bind("<Leave>", on_leave)

       
        button_4 = Button(
            self,
            bg="#2CCCEF",
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            font=("Helveltica", 16),
            command=abrir_menu_principal,
            text="Regresar"
        )
        button_4.place(
            x=0.0,
            y=480.0,
            width=327.0,
            height=120.0
        )
        button_4.bind("<Enter>", on_enter)
        button_4.bind("<Leave>", on_leave)
        button_5 = Button(
            self,
            bg="#2CCCEF",
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            font=("Helveltica", 16),
            text="Cadenas",
            command= lambda: Interfaz.ListaGramaticaArbol.ListaGramaticaArbol()

        )
        button_5.place(
            x=0.0,
            y=240.0,
            width=327.0,
            height=120.0
        )
        button_5.bind("<Enter>", on_enter)
        button_5.bind("<Leave>", on_leave)

        label1 = Label(
        self,
        text="Lenguajes Formales y de Programacion",
        font=("Happy Monkey", 28),
        bg="#FFFFFF",
        )
        label1.place(x=350.0, y=45.0, anchor="nw")

        label2 = Label(
            self,
            text="Proyecto 2",
            font=("Happy Monkey", 12),
            fg="#000000",
            bg="#FFFFFF"
        )
        label2.place(x=983.0, y=98.0, anchor="nw")

        label3 = Label(
            self,
            text="Luis Andres Cobar Sandoval 202010097",
            font=("Happy Monkey", 9),
            fg="#8B8B8B",
            bg="#FFFFFF"
        )
        label3.place(x=865.0, y=575.0, anchor="nw")

        label4 = Label(
            self,
            text="GRAMATICA LIBRE",
            font=("Happy Monkey", 48),
            fg="#000000",
            bg="#FFFFFF"
        )
        label4.place(x=473.0, y=280.0, anchor="nw")
        
        self.resizable(False, False)

        

def cargar_archivo(archivo):
    with open(archivo, 'r') as archivo:
        lineas = archivo.readlines()
        i = 0
        while i < len(lineas):

            nombre = ""
            estados = []
            alfabeto = []
            estado_inicial = ""
            estados_aceptacion = []
            transiciones = []
            SimbolodePila = []

            nombre= lineas[i] = lineas[i].strip()
            alfabeto = lineas[i+1] = lineas[i+1].strip().split(',')
            SimbolodePila = lineas[i+2] = lineas[i+2].strip().split(',') 
            estados = lineas[i+3] = lineas[i+3].strip().split(',')  
            estado_inicial = lineas[i+4] = lineas[i+4].strip()
            estados_aceptacion = lineas[i+5] = lineas[i+5].strip().split(',')
            transiciones = []
            while True:
               
                if lineas[i+6].strip() == '%':
                    i+= 1
                    break
                else:
                    transiciones.append(lineas[i+6].strip().replace(';', ','))
                    i += 1
                
            i += 6
            print(nombre, estados, alfabeto, estado_inicial, estados_aceptacion, transiciones)
            transiciones.append('')
            Clases.AutomataPila.AddPila(nombre, alfabeto, SimbolodePila, estados, estado_inicial, estados_aceptacion, transiciones)



              
            
