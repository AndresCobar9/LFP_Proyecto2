import random
from tkinter import messagebox
import Interfaz.VentanaRuta
import Interfaz.VentanaPasada
ap_registrados = []
import Clases.RecorridoPasoaPaso
class AutomataPila:
    def __init__(self, nombre, alfabeto, SimboloPila, estados, estado_inicial, estados_aceptacion, transiciones):
        self.nombre = nombre
        self.alfabeto = alfabeto
        self.SimboloPila= SimboloPila
        self.Pila = []
        self.estados = estados
        self.estado_inicial = estado_inicial
        self.estados_aceptacion = estados_aceptacion
        self.transiciones = {}
        self.transicionesN = transiciones
        for transicion in transiciones:
            
            origen, entrada, sacarPila, destino, entraPila = transicion.split(',')
            
            self.transiciones.setdefault(origen, {})[entrada] = destino



    def __str__(self):
        estados_str = ", ".join(self.estados)
        alfabeto_str = ", ".join(self.alfabeto)
        estados_aceptacion_str = ", ".join(self.estados_aceptacion)
        transiciones_str = "\n".join([f"{origen},{entrada},{destino}" for origen, transiciones in self.transiciones.items() for entrada, destino in transiciones.items()])

        return f"Nombre: {self.nombre}\nEstados: {estados_str}\nAlfabeto: {alfabeto_str}\nEstado Inicial: {self.estado_inicial}\nEstados de Aceptación: {estados_aceptacion_str}\nTransiciones:\n{transiciones_str}"
    
   

    
def generar_cadena_ejemplo(ap):
    estado_actual = ap.estado_inicial
    cadena = ""

    while True:
        transiciones = ap.transiciones.get(estado_actual)
        if not transiciones:
            messagebox.showerror(title="Error", message="No hay transiciones disponibles desde el estado actual")
            break
        
        transicion = random.choice(list(transiciones.items()))
        entrada, destino = transicion
        cadena += entrada
        estado_actual = destino

        if estado_actual in ap.estados_aceptacion:
            return cadena
    messagebox.showerror(title="Error", message="No se pudo generar una cadena de ejemplo")
    return None

def verificar_alfabeto(alfabeto):
    if len(set(alfabeto)) != len(alfabeto):
        messagebox.showerror(title="Error", message="El alfabeto no puede tener símbolos repetidos")
        return False
    else:
        return True


def verificar_estado_inicial(estado_inicial, estados):
    if estado_inicial not in estados:
        messagebox.showerror(title="Error", message="El estado inicial no está en la lista de estados")
        return False
    else:
        return True


def Estados_aceptacion(estados_aceptacion, estados):
    for estado in estados_aceptacion:
        if estado not in estados:
            messagebox.showerror(title="Error", message="Los estados de aceptación no están en la lista de estados")
            return False
    return True



def verificar_transiciones(transiciones, estados, alfabeto, SimboloPila):
    for transicion in transiciones:
        
        
        origen, entrada, sacarPila, destino, entraPila = transicion.split(',')


        if origen not in estados or destino not in estados:
            messagebox.showerror(title="Error", message="Los estados de origen y destino deben estar en la lista de estados")
            return False
        if entrada not in alfabeto:
            messagebox.showerror(title="Error", message="El símbolo de entrada no está en el alfabeto")
            return False
        if sacarPila not in SimboloPila:
            messagebox.showerror(title="Error", message="El símbolo de Pila no está en los Simbolos de Pila registrados")
            return False
        if entraPila not in SimboloPila:
            messagebox.showerror(title="Error", message="El símbolo de Pila no está en los Simbolos de Pila registrados")
            return False
        

    return True


def Crear_AutomataPila(nombre, alfabeto,SimboloPila, estados, estado_inicial, estados_aceptacion, transiciones):
    ap = AutomataPila(nombre, alfabeto,SimboloPila, estados, estado_inicial, estados_aceptacion, transiciones)
    ap_registrados.append(ap)


def listaAutomataPila():
    return ap_registrados


def comprobar_cadena_ap(ap, cadena):
    cadena = "$"+cadena+"$"
    estado_actual = ap.estado_inicial
    
    for caracter in cadena:
        
        if caracter not in ap.alfabeto:
            messagebox.showerror(title="Error", message=f"El caracter '{caracter}' no está en el alfabeto del AutomataPila '{ap.nombre}'")
            return False
        
        if estado_actual not in ap.transiciones or caracter not in ap.transiciones[estado_actual]:
            messagebox.showerror(title="Error", message=f"No hay una transición definida para el estado '{estado_actual}' y el caracter '{caracter}' en el AutomataPila '{ap.nombre}'")
            return False
        
        estado_actual = ap.transiciones[estado_actual][caracter]

        
    
    if estado_actual in ap.estados_aceptacion:
       
        return f"La cadena: | {cadena.replace('$','')}  | es válida en el AutomataPila '{ap.nombre}'"
    else:
        return f"La cadena: | {cadena.replace('$','')}  | no es válida en el AutomataPila '{ap.nombre}'"
    

def comprobarCadenaRapido(ap, cadena):
    cadena = "$"+cadena+"$"
    estado_actual = ap.estado_inicial
    
    for caracter in cadena:
        
        if caracter not in ap.alfabeto:
            messagebox.showerror(title="Error", message=f"El caracter '{caracter}' no está en el alfabeto del AutomataPila '{ap.nombre}'")
            return False
        
        if estado_actual not in ap.transiciones or caracter not in ap.transiciones[estado_actual]:
            messagebox.showerror(title="Error", message=f"No hay una transición definida para el estado '{estado_actual}' y el caracter '{caracter}' en el AutomataPila '{ap.nombre}'")
            return False
        
        estado_actual = ap.transiciones[estado_actual][caracter]

        
    
    if estado_actual in ap.estados_aceptacion:
       
        return True
    else:
        return False
    
def comprobar_cadena_ap_ruta(ap, cadena):
    cadena = "$"+cadena+"$"
    estado_actual = ap.estado_inicial
    transicion = []
    for caracter in cadena:
        
        if caracter not in ap.alfabeto:
            messagebox.showerror(title="Error", message=f"El caracter '{caracter}' no está en el alfabeto del AutomataPila '{ap.nombre}'")
            return False
        
        if estado_actual not in ap.transiciones or caracter not in ap.transiciones[estado_actual]:
            messagebox.showerror(title="Error", message=f"No hay una transición definida para el estado '{estado_actual}' y el caracter '{caracter}' en el AutomataPila '{ap.nombre}'")
            return False
        
        estado_anterior = estado_actual
        estado_actual = ap.transiciones[estado_actual][caracter]
        for Transicion in ap.transicionesN:
            Origen, Entrada, sacarPila, Destino, EntraPila = Transicion.split(',')
            
            if Origen == estado_anterior and caracter == Entrada and estado_actual == Destino:
                ruta = f"{Origen},{Entrada},{sacarPila},{Destino},{EntraPila}"
                ruta = ruta.replace("$", "λ")
                transicion.append(ruta)
        
    
    if estado_actual in ap.estados_aceptacion:
       
        Interfaz.VentanaRuta.VistaRuta(cadena.replace('$',''),transicion,ap.nombre)
    else:
        return f"La cadena '{cadena.replace('$','')}' no es válida en el AutomataPila '{ap.nombre}'"    
    

def comprobar_cadena_ap_Paso(ap, cadena):
    if comprobarCadenaRapido(ap,cadena):
        cadena = "$"+cadena+"$"
        estado_actual = ap.estado_inicial
        transicion = []

        caracteres=""
        for caracter in cadena:
            caracteres = caracteres + caracter
            if caracter not in ap.alfabeto:
                messagebox.showerror(title="Error", message=f"El caracter '{caracter}' no está en el alfabeto del AutomataPila '{ap.nombre}'")
                return False
            
            if estado_actual not in ap.transiciones or caracter not in ap.transiciones[estado_actual]:
                messagebox.showerror(title="Error", message=f"No hay una transición definida para el estado '{estado_actual}' y el caracter '{caracter}' en el AutomataPila '{ap.nombre}'")
                return False
            
            estado_anterior = estado_actual
            estado_actual = ap.transiciones[estado_actual][caracter]
            for Transicion in ap.transicionesN:
                Origen, Entrada, sacarPila, Destino, EntraPila = Transicion.split(',')
                
                if Origen == estado_anterior and caracter == Entrada and estado_actual == Destino:
                    ruta = f"{Entrada},{sacarPila},{EntraPila}"
                    ruta = ruta.replace("$", "λ")
                    
                    Clases.RecorridoPasoaPaso.GenerarDOT(ap, caracteres, estado_actual, ruta, Transicion,False)
                    
    else:
        messagebox.showerror(title="Error", message=f"La cadena '{cadena}' no es válida en el AutomataPila '{ap.nombre}'")
        
    
    if estado_actual in ap.estados_aceptacion:
       
        Clases.RecorridoPasoaPaso.GenerarDOT(ap, cadena, estado_actual, ruta, Transicion,True)
    else:
        return f"La cadena '{cadena.replace('$','')}' no es válida en el AutomataPila '{ap.nombre}'"        
    



def SoloPaso(ap, cadena):
    if comprobarCadenaRapido(ap,cadena):
        cadena = "$"+cadena+"$"
        estado_actual = ap.estado_inicial
        info = []
        pila = []
        caracteres=""
        for caracter in cadena:
            caracteres = caracteres + caracter
            if caracter not in ap.alfabeto:
                messagebox.showerror(title="Error", message=f"El caracter '{caracter}' no está en el alfabeto del AutomataPila '{ap.nombre}'")
                return False
            
            if estado_actual not in ap.transiciones or caracter not in ap.transiciones[estado_actual]:
                messagebox.showerror(title="Error", message=f"No hay una transición definida para el estado '{estado_actual}' y el caracter '{caracter}' en el AutomataPila '{ap.nombre}'")
                return False
            
            estado_anterior = estado_actual
            estado_actual = ap.transiciones[estado_actual][caracter]
            for Transicion in ap.transicionesN:
                Origen, Entrada, sacarPila, Destino, EntraPila = Transicion.split(',')
                
                if Origen == estado_anterior and caracter == Entrada and estado_actual == Destino:
                    ruta = f"{Origen},{Entrada},{sacarPila},{Destino},{EntraPila}"
                    try:    
                        if EntraPila != '$':
                                pila.append(EntraPila)
                        if sacarPila != '$':
                                if len(pila) > 0:
                                    pila.remove(sacarPila)
                    except:
                        pass
                    ruta = ruta.replace("$", "λ")
                    info.append([ruta , Transicion, str(pila), caracteres])
        Interfaz.VentanaPasada.VistaRuta(info)
                    
                    
                    
    else:
        messagebox.showerror(title="Error", message=f"La cadena '{cadena}' no es válida en el AutomataPila '{ap.nombre}'")
        
    



def addPila(nombre, alfabeto, SimboloPila, estados, estado_inicial, estados_aceptacion, transiciones):
    del transiciones[-1]
    if nombre == "" or estados == "" or alfabeto == "" or estado_inicial == "" or estados_aceptacion == "" or SimboloPila == "" or transiciones == "": 
        messagebox.showerror(title="Error", message="Alguno de los campos esta Vacio")
        return
    
    else:
        if verificar_estado_inicial(estado_inicial, estados) == True:
            if Estados_aceptacion(estados_aceptacion, estados) == True:
                if verificar_transiciones(transiciones, estados, alfabeto, SimboloPila)== True:
                    if verificar_alfabeto(alfabeto)== True:
                        Crear_AutomataPila(nombre, alfabeto, SimboloPila, estados, estado_inicial, estados_aceptacion, transiciones)
                        
                        
                        
                        return True
    