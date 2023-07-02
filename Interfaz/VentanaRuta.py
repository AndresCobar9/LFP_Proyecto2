



from tkinter import Toplevel, Label
from tkinter import Tk, Text, END
import tkinter as tk

class VistaRuta(tk.Tk):
    def __init__(self, Cadena, Ruta, nombre):
        super().__init__()
        print('Prueba1: ',Cadena, Ruta, nombre)
        self.title("Ventana de Ruta")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width/2) - (600/2)
        y = (screen_height/2) - (350/2)
        self.geometry("%dx%d+%d+%d" % (600, 350, x, y))
        self.title("Ruta seguida")
        self.geometry("600x350")

        self.text_area = Text(self)
        self.text_area.pack()

        self.display_grammar(Cadena, Ruta, nombre)

    def display_grammar(self, Cadena, Ruta, nombre):
        print('Prueba2: ',Cadena, Ruta, nombre)
        self.text_area.insert(END, f"Nombre: {nombre}\n")
        self.text_area.insert(END, f"Cadena utilizada: {Cadena}\n\n")
        self.text_area.insert(END, f"--------------------\n")
       

        for ruta in Ruta:
            self.text_area.insert(END, f"|    {ruta}    |\n")
            
        self.text_area.insert(END, f"--------------------\n")
        self.text_area.config(state="disabled")

   