import tkinter as tk
from graphviz import Digraph
import webbrowser
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from PIL import Image

contador = 0
Pila = []
Imagenes =[]
def obtener_cadena(AP, origen, entrada, destino):
    
    for transicion in AP:
        Origen, Entrada, sacarPila, Destino, EntraPila = transicion.split(',')
        
        if Origen == origen and entrada == Entrada and destino == Destino:
            cadena = f"{entrada},{sacarPila},{EntraPila}"
            cadena = cadena.replace("$", "λ")
            return cadena


def GenerarDOT(ap, cadena, posicion_actual, Transicion, trans, Final):
    global contador
    global Imagenes
    global Pila
    cadena = cadena.replace("$", "")
    dot = Digraph(ap.nombre, filename=(ap.nombre + '_' +str(contador)), format='png',directory='./ImagenesPasoaPaso')
    dot.attr(rankdir='LR', size='8,5')

    Origen, Entrada, sacarPila, Destino, EntraPila = trans.split(',')
    
    try:    
        if EntraPila != '$':
                Pila.append(EntraPila)
        if sacarPila != '$':
                if len(Pila) > 0:
                    Pila.remove(sacarPila)
    except:
        pass
    
    dot.node('Cadena: ' + cadena, shape= 'rectangle')
    dot.node('Cadena: ' + str(Pila), shape= 'rectangle')
    
    

    estados1 = set(ap.estados).symmetric_difference(set(ap.estados_aceptacion))
    estados2 = estados1.difference({ap.estado_inicial})

    
    dot.node(ap.estado_inicial, shape='circle', color='red')

    for estado in estados2:
        if estado == posicion_actual:
            dot.node(estado, shape='circle', color='green')
        else:
            dot.node(estado, shape='circle')

    for estado_aceptacion in ap.estados_aceptacion:
        if estado_aceptacion == posicion_actual:
            dot.node(estado_aceptacion, shape='doublecircle', color='green')
        else:
            dot.node(estado_aceptacion, shape='doublecircle')

    for origen, transicion in ap.transiciones.items():
        for etiqueta, destino in transicion.items():
            etiqueta = obtener_cadena(ap.transicionesN ,origen, etiqueta, destino)
            if Transicion == etiqueta:
                dot.edge(origen, destino, label=etiqueta, color='green')
            else:
                dot.edge(origen, destino, label=etiqueta)
                
    Imagenes.append(str(ap.nombre + '_'+ str(contador)))
    contador = contador + 1
    
    dot.render(view=False)
    if Final == True:
        
        GenerarPDF(ap.nombre, cadena)
        contador = 0
        Pila = []
        Imagenes = []


def get_scaled_dimensions(image_width, image_height, page_width, margin):
    max_width = page_width - (2 * margin)
    scale_factor = max_width / image_width
    scaled_width = max_width
    scaled_height = image_height * scale_factor
    return scaled_width, scaled_height

def GenerarPDF(nombre, cadena):
    w, h = (21.6 * cm, 35.0 * cm)

    global Pila
    Imagenes.remove(Imagenes[0])
    Imagenes.remove(Imagenes[-1])
    c = canvas.Canvas("Reporte_Paso_a_Paso_" + nombre + ".pdf", pagesize=(w, h))
    c.setLineWidth(.3)
    c.setFont('Helvetica', 22)

    # Calcular posición x para centrar el texto
    reporte_afd_text = "- Reporte Paso a Paso de: '" + nombre + "' -"
    reporte_afd_text_width = c.stringWidth(reporte_afd_text, "Helvetica", 22)
    reporte_afd_text_x = (w - reporte_afd_text_width) / 2

    c.drawString(reporte_afd_text_x, h - 30, reporte_afd_text)
    c.setFont('Helvetica', 12)

    margin = 30  # Márgenes izquierdo y derecho
    page_width = w - (2 * margin)
    image_y = h - 70 - 180  # Posición inicial en el pie de la página

    for imagen in Imagenes:
        image_path = imagen + ".png"
        image = Image.open('./ImagenesPasoaPaso/' + image_path)
        image_width, image_height = image.size

        # Calcular las dimensiones escaladas de la imagen
        scale_factor = page_width / image_width
        scaled_width = page_width
        scaled_height = image_height * scale_factor

        # Verificar si la imagen cabe en la página actual
        if image_y < margin + scaled_height:
            c.showPage()  # Comenzar una nueva página
            image_y = h - margin - scaled_height  # Posición inicial en la nueva página

        image_x = (w - scaled_width) / 2

        # Dibujar la imagen escalada en el pie de la página
        c.drawInlineImage('./ImagenesPasoaPaso/' + image_path, image_x, image_y, width=scaled_width, height=scaled_height)

        # Agregar separador
        separator_y = image_y - 10
        c.setStrokeColorRGB(0, 0, 0)  # Color del separador (negro)
        c.setLineWidth(1)  # Grosor del separador
        c.line(margin, separator_y, w - margin, separator_y)

        image_y -= scaled_height + 50  # Espacio entre las imágenes

    c.save()