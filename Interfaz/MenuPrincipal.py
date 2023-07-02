from re import X
import time
import tkinter as tk
from pathlib import Path
from tkinter import BOTH, RIGHT, Frame, Label, Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter.ttk import Progressbar
from PIL import Image
import Interfaz.ModuloAP
import Interfaz.GramaticaLibre

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class MenuEmergente(tk.Tk):
    def __init__(self):
        super().__init__()

        def actualizar_progreso():
            if barra["value"] < 100:
                barra["value"] += 20
                self.after(1000, actualizar_progreso)

        self.resizable(False, False)
        self.overrideredirect(True)  # Turns off title bar and geometry
        self.wm_attributes("-topmost", 1)  # Forces tkinter window to be on top of all other windows

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (1115 / 2)
        y = (screen_height / 2) - (630 / 2)
        self.geometry("%dx%d+%d+%d" % (1115, 630, x, y))

        self.configure(bg="#FFFFFF")
        self.title("Menú Principal")

        label1 = Label(
            self,
            text="Lenguajes Formales y de Programacion",
            font=("Happy Monkey", 28),
            bg="#FFFFFF",
        )
        label1.place(x=0.0, y=0.0, width=1115.0, height=100.0)

        label2 = Label(
            self,
            text="Bienvenido a Spark Stack",
            font=("Happy Monkey", 54),
            fg="#000000",
            bg="#FFFFFF"
        )
        label2.place(x=110.0, y=220.0, anchor="nw")

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
            text="Cargando...",
            font=("Happy Monkey", 20),
            fg="#000000",
            bg="#FFFFFF"
        )
        label4.place(x=0, y=340.0, width=1115.0, height=100.0,  anchor="nw")

        barra = Progressbar(self, length=600, style='black.Horizontal.TProgressbar')
        barra.place(x=157, y=440.0,  width=800.0, height=40.0, anchor="nw")
        actualizar_progreso()
            
        
        # Programa la destrucción de la ventana después de 5 segundos
        self.after(5100, self.cerrar_ventana)
        
    

    def cerrar_ventana(self):
        self.destroy()
        MenuPrincipal()
       

            
class MenuPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        
        def on_enter(event):
            event.widget.config(bg="gray", fg="white")

        def on_leave(event):
            event.widget.config(bg="lightgray", fg="black")

        # Configuración de la ventana principal
        self.geometry("1115x600")
        self.configure(bg="#FFFFFF")
        self.title("Menú Principal")
        self.resizable(False, False)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (1115 / 2)
        y = (screen_height / 2) - (600 / 2)
        self.geometry("%dx%d+%d+%d" % (1115, 600, x, y))
        def ModuloGL():
            Interfaz.GramaticaLibre.GramaticaLibre()
            self.destroy()

        button_1 = Button(
            self,
            bg="lightgray",
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            font=("Helvetica", 16),
            text="Gramatica Libre de Contexto",
            command= lambda: ModuloGL()
        )
        button_1.bind("<Enter>", on_enter)
        button_1.bind("<Leave>", on_leave)
        button_1.place(x=0.0, y=0.0, width=327.0, height=120.0)

        button_2 = Button(
            self,
            bg="lightgray",
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            text="Modulo Automatas de Pila",
            font=("Helveltica", 16),
            command= lambda: (Interfaz.ModuloAP.ModuloAP(), self.destroy())
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
            bg="lightgray",
            borderwidth=0,
            highlightthickness=0,
            command=self.quit,
            relief="flat",
            font=("Helveltica", 16),
            text="Salir"
        )
        button_4.place(
            x=0.0,
            y=480.0,
            width=327.0,
            height=120.0
        )
        button_4.bind("<Enter>", on_enter)
        button_4.bind("<Leave>", on_leave)

        

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
            text="Spark Stack",
            font=("Happy Monkey", 48),
            fg="#000000",
            bg="#FFFFFF"
        )
        label4.place(x=543.0, y=280.0, anchor="nw")

        self.resizable(False, False)
        
        


   