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
import Clases.GramaticaLDC
import Interfaz.MenuPrincipal
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class GramaticaLibre(tk.Tk):
    def __init__(self):
        super().__init__()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width/2) - (1115/2)
        y = (screen_height/2) - (600/2)
        self.geometry("%dx%d+%d+%d" % (1115, 600, x, y))
        self.title("Gramatica Libre de Contexto")
        self.geometry("1115x600")
        self.configure(bg="#FFFFFF")
        def on_enter(event):
            event.widget.config(bg="#288AC0", fg="white")

        def cargarArchivo():
            
            archivo = filedialog.askopenfilename(filetypes=[("Text files","*.txt")])
            if archivo:
                cargar_archivo(archivo)

        def on_leave(event):
            event.widget.config(bg="#2CCCEF", fg="black")

        def abrir_menu_principal():
            Interfaz.MenuPrincipal.MenuPrincipal()
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
            text="Informacion General",
            font=("Helveltica", 16),
            command= lambda: (Interfaz.ListaGramatica.ListaGramatica(), self.destroy())
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
            text="Arbol de Derivacion",
            command= lambda: (Interfaz.ListaGramaticaArbol.ListaGramaticaArbol(), self.destroy())
            

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
        lines = archivo.readlines()

        i = 0
        while i < len(lines):
            line = lines[i].strip()

            if line == '%':
                i += 1
                continue

            name = line
            non_terminals = lines[i+1].strip().split(',')
            terminals = lines[i+2].strip().split(',')
            start_symbol = lines[i+3].strip()
            productions = []

            i += 4
            while i < len(lines) and lines[i].strip() != '%':
                productions.append(lines[i].strip())
                i += 1

            grammar = Clases.GramaticaLDC.Grammar(name, non_terminals, terminals, start_symbol, productions)
            
            # Verificar si la gramática cumple con las características de una gramática libre de contexto
            if grammar_is_context_free(grammar):
                Clases.GramaticaLDC.all_grammars.append(grammar)
            
            i += 1
    
    Clases.GramaticaLDC.get_all()  # Llamada correcta al método


def grammar_is_context_free(grammar):
    # Verificar si el no terminal tiene más de una derivación
    non_terminals_set = set(grammar.non_terminals)
    for non_terminal in non_terminals_set:
        count = 0
        for production in grammar.productions:
            if non_terminal in production:
                count += 1
                if count > 1:
                    break
        if count > 1:
            return True  # Cumple con la característica de una gramática libre de contexto

    # Verificar si la gramática posee una producción que la identifique como gramática independiente del contexto
    for production in grammar.productions:
        if production.startswith(grammar.start_symbol):
            return True  # Cumple con la característica de una gramática libre de contexto

    return False  # No cumple con las características de una gramática libre de contexto



              
            
