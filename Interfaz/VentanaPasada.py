from tkinter import Tk, Text, Frame, Label, font
import tkinter as tk

class VistaRuta(tk.Tk):
    def __init__(self, info):
        super().__init__()
        self.title("Ventana de Ruta")
        self.geometry("600x350")

        self.frame = Frame(self)
        self.frame.pack()

        header_font = font.Font(size=42, family="Helvetica", weight="bold")
        normal_font = font.Font(size=18, family="Helvetica")

        iteracion_label = Label(self.frame, text="Iteracion", font=header_font)
        pila_label = Label(self.frame, text="Pila", font=header_font)
        entrada_label = Label(self.frame, text="Entrada", font=header_font)
        transicion_label = Label(self.frame, text="Transicion", font=header_font)


        # Ubicar etiquetas de encabezado de columna en la grilla
        iteracion_label.grid(row=0, column=0, padx=5, pady=5)
        pila_label.grid(row=0, column=1, padx=5, pady=5)
        entrada_label.grid(row=0, column=2, padx=5, pady=5)
        transicion_label.grid(row=0, column=3, padx=5, pady=5)

        # Llenar la tabla con la información proporcionada
        for i, item in enumerate(info):
            iteracion = Label(self.frame, text=str(i+1), font=normal_font)
            pila = Label(self.frame, text=item[2], font=normal_font)
            entrada = Label(self.frame, text=item[3], font=normal_font)
            transicion = Label(self.frame, text=item[1], font=normal_font)

            # Ubicar los elementos en la grilla
            iteracion.grid(row=i+1, column=0, padx=5, pady=5)
            pila.grid(row=i+1, column=1, padx=5, pady=5)
            entrada.grid(row=i+1, column=2, padx=5, pady=5)
            transicion.grid(row=i+1, column=3, padx=5, pady=5)