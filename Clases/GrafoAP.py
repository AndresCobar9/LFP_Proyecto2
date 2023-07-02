import tkinter as tk
from graphviz import Digraph
import webbrowser
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from PIL import Image

from Clases.AutomataPila import AutomataPila

def obtener_cadena(AP, origen, entrada, destino):
    
    for transicion in AP:
        Origen, Entrada, sacarPila, Destino, EntraPila = transicion.split(',')
        if Origen == origen and entrada == Entrada and destino == Destino:
            cadena = f"{entrada},{sacarPila},{EntraPila}"
            cadena = cadena.replace("$", "λ")
            return cadena


      #  if transicion == origen:
       #     for entrada_transicion, destino_transicion in trans_dict.items():
        #        if entrada_transicion == entrada and destino_transicion == destino:
         #           cadena = f"{origen},{entrada},{AP.SimboloPila},{destino},{AP.SimboloPila}"
          #          return cadena


   

def generarDOT(estados, estados_aceptacion, transiciones, estado_inicial, nombre, AP):
    dot = Digraph(nombre, filename=nombre, format='png')
    dot.attr(rankdir='LR', size='8,5')

    estados1 = set(estados).symmetric_difference(set(estados_aceptacion))
    estados2 = estados1.difference({estado_inicial})

    # Agregar estado inicial con triángulo
    dot.node(estado_inicial, shape='circle', color='red')

    for estado in estados2:
        dot.node(estado, shape='circle')

    for estado_aceptacion in estados_aceptacion:
        dot.node(estado_aceptacion, shape='doublecircle')

    for origen, transicion in transiciones.items():
        for etiqueta, destino in transicion.items():
            etiqueta = obtener_cadena(AP,origen, etiqueta, destino)
            dot.edge(origen, destino, label=etiqueta)

    dot.render(view=False)


def generarPDF(estados, estados_aceptacion, transiciones, estado_inicial, nombre,AP,alfabeto,pila):
    w, h = A4
    c = canvas.Canvas("ReporteAutomataPila_" + nombre + ".pdf", pagesize=A4)
    c.setLineWidth(.3)
    c.setFont('Helvetica', 22)

    # Calcular posición x para centrar el texto
    reporte_afd_text = "- Reporte Generado Sobre Automata de Pila '" + nombre + "' -"
    reporte_afd_text_width = c.stringWidth(reporte_afd_text, "Helvetica", 22)
    reporte_afd_text_x = (w - reporte_afd_text_width) / 2

    c.drawString(reporte_afd_text_x, h - 30, reporte_afd_text)
    c.setFont('Helvetica', 12)
    c.drawString(30, h - 70, "Nombre del AutomataPila:  " + nombre)
    c.drawString(30, h - 90, "Estados:  " + str(estados))
    c.drawString(30, h - 110, "Estado inicial:  " + estado_inicial)
    c.drawString(30, h - 130, "Estados de aceptacion:  " + str(estados_aceptacion))
    c.drawString(30, h - 150, "Alfabeto:  " + str(alfabeto))
    c.drawString(30, h - 170, "Simbolos de Pila:  " + str(pila))
    # Generar una linea por cada elemento en el array de transiciones
    c.drawString(30, h - 190, "Listado de Transiciones:")
    x = 250  # Posición vertical inicial
    for transicion in transiciones:
        c.drawString(30, h - x + 20, "     - "+ transicion)
        x += 20  # Incrementar la posición vertical
        c.setFont('Helvetica', 12)

    image_path = nombre + ".png"
    image = Image.open(image_path)
    image_width, image_height = image.size
    image_x = (w - image_width) / 2
    image_y = 30  # Posición en el pie de la página

    
   

    c.setFont('Helvetica', 12)

    # Ajustar las coordenadas para que las líneas de texto estén encima de la imagen
    c.drawString(30, image_y + image_height + 20, "------------------------------------------------------- Gráfica del AutomataPila -------------------------------------------------------")
   

    # Dibujar la imagen en el pie de la página
    c.drawInlineImage(image_path, image_x, image_y, width=image_width, height=image_height)
    c.save()


def generarReporteAutomataPila(estados, estados_aceptacion, transiciones, transicionesN,estado_inicial, nombre,AP,alfabeto,simboloPila):
 
    
    generarDOT(estados, estados_aceptacion, transiciones, estado_inicial,nombre,transicionesN)
    
    generarPDF(estados, estados_aceptacion, transicionesN, estado_inicial, nombre,AP,alfabeto,simboloPila)
    return True