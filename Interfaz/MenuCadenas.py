from pathlib import Path
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import Interfaz.MenuPrincipal
from PIL import Image
import Clases.AutomataPila
import Interfaz.ModuloAP
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../assets/frame0")
afn_registrados=[]
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class MenuCadenas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.resizable(False, False)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width/2) - (1115/2)
        y = (screen_height/2) - (600/2)
        self.geometry("%dx%d+%d+%d" % (1115, 600, x, y))
        self.title("Validar Cadena")
        self.geometry("1115x600")   
        self.configure(bg="#FFFFFF")
        def on_enter(event):
            event.widget.config(bg="#288AC0", fg="white")

        def on_leave(event):
            event.widget.config(bg="#2CCCEF", fg="black")

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
        cargarAFN(self)
        

        entry_1 = Entry(
            self,
            bg="#D9D9D9",
            fg="#000716",
            font=("HappyMonkey Regular", 14),
            highlightthickness=0,
            bd=0,
            justify="center",
            
            
        )
        entry_1.place(
            x=660.0, y=34.0,
            width=327.0,
            height=30.0
        )


        button_1 = Button(
            self,
            bg="#2CCCEF",
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            font=("Helvetica", 16),
            text="Validar Cadena",
            command=lambda: ComprobarCadena(self, getEntry()),
        )
        button_1.bind("<Enter>", on_enter)
        button_1.bind("<Leave>", on_leave)
        button_1.place(x=0.0, y=0.0, width=327.0, height=120.0)
        def getEntry():
            if not entry_1.get():
                return None
            else:
                return entry_1.get()
        
        button_2 = Button(
            self,
            bg="#2CCCEF",
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            text="Ruta de Validacion",
            command= lambda: RutaValidacion(self, getEntry()),
            font=("Helveltica", 16),
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
            text="Recorrido Paso a Paso",
            command= lambda: PasoPaso(self, getEntry()),
            font=("Helveltica", 16),
        )
        button_4.place(
            x=0.0,
            y=240.0,
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
            text="Una Pasada",
            command= lambda: UnaPasada(self, getEntry()),
            font=("Helveltica", 16),
        )
        button_5.place(
            x=0.0,
            y=360.0,
            width=327.0,
            height=120.0
        )
        button_5.bind("<Enter>", on_enter)
        button_5.bind("<Leave>", on_leave)
            
        button_3 = Button(
            self,
            bg="#2CCCEF",
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
        text="Ruta a evaluar:",
        font=("Happy Monkey", 20),
        bg="#FFFFFF",
        )
        label1.place(x=410.0, y=30.0, anchor="nw")

       
def cargarAFN(self):
    AP = Clases.AutomataPila.listaAutomataPila()
    print(AP)
    for Gramatica in AP:
        self.listbox.insert(END, "Nombre: "+  Gramatica.nombre + " - Alfabeto: " + str(Gramatica.alfabeto) + " - Restados: " + str(Gramatica.estados))
        


def ComprobarCadena(self, cadena):
    selected_index = self.listbox.curselection()
    afn_registrados = Clases.AutomataPila.listaAutomataPila()              
     
    if selected_index:
        afn = afn_registrados[selected_index[0]]
        resultados = Clases.AutomataPila.comprobar_cadena_ap(afn, cadena)
        messagebox.showinfo("Resultados", resultados)

def RutaValidacion(self, cadena):
    selected_index = self.listbox.curselection()
    ap_registrados = Clases.AutomataPila.listaAutomataPila()              
    if selected_index:
        ap = ap_registrados[selected_index[0]]
        resultados = Clases.AutomataPila.comprobar_cadena_ap_ruta(ap, cadena)
        
def PasoPaso(self,cadena):
    selected_index = self.listbox.curselection()
    ap_registrados = Clases.AutomataPila.listaAutomataPila()              
    if selected_index:
        ap = ap_registrados[selected_index[0]]
        resultados = Clases.AutomataPila.comprobar_cadena_ap_Paso(ap, cadena)

def UnaPasada(self,cadena):
    selected_index = self.listbox.curselection()
    ap_registrados = Clases.AutomataPila.listaAutomataPila()              
    if selected_index:
        ap = ap_registrados[selected_index[0]]
        resultados = Clases.AutomataPila.SoloPaso(ap, cadena)