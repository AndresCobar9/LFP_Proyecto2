import tkinter as tk
from tkinter import Toplevel, Label
from tkinter import Tk, Text, END

class VistaGramatica:
    def __init__(self, grammar):
        super().__init__()
        
        self.window = Tk()
        self.window.title("Ventana de Gramática")
        
        self.text_area = Text(self.window)
        self.text_area.pack()

        self.display_grammar(grammar)

    def display_grammar(self, grammar):
        self.text_area.insert(END, f"Nombre: {grammar.name}\n")
        self.text_area.insert(END, f"No Terminales: {', '.join(grammar.non_terminals)}\n")
        self.text_area.insert(END, f"Terminales: {', '.join(grammar.terminals)}\n")
        self.text_area.insert(END, f"No Terminal Inicial: {grammar.start_symbol}\n")
        self.text_area.insert(END, "Producciones:\n")

        productions_dict = self.convert_productions(grammar.productions)

        for non_terminal, expressions in productions_dict.items():
            expressions_str = " | ".join(expressions)
            production_str = f"{non_terminal} -> {expressions_str}\n"
            self.text_area.insert(END, production_str)

        self.text_area.config(state="disabled")

    def convert_productions(self, productions):
        productions_dict = {}

        for production in productions:
            parts = production.split("::=")
            non_terminal = parts[0].strip()
            expression = parts[1].strip()

            if non_terminal in productions_dict:
                productions_dict[non_terminal].append(expression)
            else:
                productions_dict[non_terminal] = [expression]

        return productions_dict