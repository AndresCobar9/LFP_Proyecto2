from pathlib import Path
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import Interfaz.MenuPrincipal
from PIL import Image
import Clases.GramaticaLDC
import Interfaz.ListaGramatica
import Interfaz.VentanaDescripcion
import Clases.CrearArbol
import Clases.GrafoAP
import Interfaz.ModuloAP
import Clases.AutomataPila
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../assets/frame0")
afd_registrados=[]
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class InformacionAutomata(tk.Tk):
    def __init__(self):
        super().__init__()
        self.resizable(False, False)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width/2) - (1115/2)
        y = (screen_height/2) - (600/2)
        self.geometry("%dx%d+%d+%d" % (1115, 600, x, y))
 
        self.title("Informacion Automata")
        self.geometry("1115x600")
        self.configure(bg="#FFFFFF")
        def on_enter(event):
            event.widget.config(bg="#a63232", fg="white")

        def on_leave(event):
            event.widget.config(bg="#e15a5a", fg="black")

        def abrir_menu_principal():
            Interfaz.ModuloAP.ModuloAP()
            self.destroy()

        self.listbox = Listbox(
            self,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            selectbackground="#7C7C7C",
            selectforeground="#FFFFFF",
            font=("HappyMonkey Regular", 14),
            activestyle=DOTBOX
        )
        self.listbox.place(x=380.0, y=100.0, width=650.0, height=450.0)

        self.scrollbar = Scrollbar(
            self,
            command=self.listbox.yview
        )
        self.scrollbar.place(x=1030.0, y=100.0, width=17.0, height=450)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        cargarAFD(self)

    

        button_1 = Button(
            self,
            bg="#e15a5a",
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            font=("Helvetica", 16),
            text="Cargar Reporte",
            command=lambda: CargarInformacion(self)
            
        )
        button_1.bind("<Enter>", on_enter)
        button_1.bind("<Leave>", on_leave)
        button_1.place(x=0.0, y=0.0, width=327.0, height=120.0)
        
        
        
        
        
            
        button_3 = Button(
            self,
            bg="#e15a5a",
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            text="Regresar",
            font=("Helveltica", 16),
            command=lambda: abrir_menu_principal()
        )
        button_3.place(
            x=0.0,
            y=480.0,
            width=327.0,
            height=120.0
        )
        button_3.bind("<Enter>", on_enter)
        button_3.bind("<Leave>", on_leave)


        label1 = Label(
        self,
        text="Automatas Cargados",
        font=("Happy Monkey", 28),
        bg="#FFFFFF",
        )
        label1.place(x=580.0, y=30.0, anchor="nw")

       
def cargarAFD(self):
    AP = Clases.AutomataPila.listaAutomataPila()
    print(AP)
    for Gramatica in AP:
        self.listbox.insert(END, "Nombre: "+  Gramatica.nombre + " - Alfabeto: " + str(Gramatica.alfabeto) + " - Restados: " + str(Gramatica.estados))
        

def CargarInformacion(self):
    selected_index = self.listbox.curselection()
    AP = Clases.AutomataPila.listaAutomataPila()         
     
    if selected_index:
        # Obtener el AFD correspondiente al índice seleccionado
        Grm = AP[selected_index[0]]   
        print(Grm.estados, Grm.estados_aceptacion, Grm.transiciones, Grm.transicionesN,Grm.estado_inicial, Grm.nombre,Grm.alfabeto)
        Clases.GrafoAP.generarReporteAutomataPila( Grm.estados, Grm.estados_aceptacion, Grm.transiciones, Grm.transicionesN,Grm.estado_inicial, Grm.nombre,Grm.alfabeto,Grm.alfabeto,Grm.SimboloPila)
    
                                                                                
        
