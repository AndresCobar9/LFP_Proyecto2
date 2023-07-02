# Proyecto Lenguajes Formales y de Programación


El proyecto "Spark Stack" es un programa con Interfaz Gráfica desarrollado en Python que tiene como objetivo explorar los conceptos de los lenguajes independientes del contexto. El programa se divide en dos secciones principales, cada una enfocada en funcionalidades relacionadas con las gramáticas libres del contexto y los autómatas de pila, respectivamente.

La interfaz del programa permite a los usuarios acceder a diferentes funcionalidades a través de menús intuitivos. Estos menús facilitan la navegación entre las distintas opciones disponibles en cada módulo. Cada uno de estos módulos agrupa acciones que son de gran utilidad para aquellos que deseen comprender en profundidad el funcionamiento de los lenguajes libres del contexto.

Para crear los autómatas de pila y las gramáticas libres del contexto, el programa se basa en archivos de entrada. Estos archivos estructurados garantizan un funcionamiento óptimo del programa y pueden ser leídos utilizando las funcionalidades nativas de Python, sin necesidad de implementar analizadores adicionales.


# Manual Tecnico

![enter image description here](https://i.ibb.co/CJCxk2Y/image.png)
1.  `def iniciar_programa():` - Define una función llamada `iniciar_programa` que se encargará de iniciar el programa.
    
2.  `menu_principal = MenuEmergente()` - Crea una instancia de la clase `MenuEmergente` y la asigna a la variable `menu_principal`. Esto crea la ventana principal de la interfaz gráfica.
    
3.  `menu_principal.mainloop()` - Ejecuta el bucle principal de la ventana `menu_principal`. Este bucle se mantiene en ejecución hasta que la ventana se cierre, permitiendo que la interfaz gráfica responda a eventos y acciones del usuario.
    
4.  `if __name__ == '__main__':` - Verifica si el script se está ejecutando directamente (es decir, no ha sido importado como módulo).
    
5.  `iniciar_programa()` - Llama a la función `iniciar_programa()` para iniciar el programa. Esta es la entrada principal del programa y se encarga de iniciar la interfaz gráfica.
![enter image description here](https://i.ibb.co/g9qWcVd/image.png)

-   Método `__init__(nombre, alfabeto, SimboloPila, estados, estado_inicial, estados_aceptacion, transiciones)`:
    -   Asignar el parámetro `nombre` al atributo `nombre` de la instancia.
    -   Asignar el parámetro `alfabeto` al atributo `alfabeto` de la instancia.
    -   Asignar el parámetro `SimboloPila` al atributo `SimboloPila` de la instancia.
    -   Inicializar el atributo `Pila` como una lista vacía.
    -   Asignar el parámetro `estados` al atributo `estados` de la instancia.
    -   Asignar el parámetro `estado_inicial` al atributo `estado_inicial` de la instancia.
    -   Asignar el parámetro `estados_aceptacion` al atributo `estados_aceptacion` de la instancia.
    -   Inicializar el atributo `transiciones` como un diccionario vacío.
    -   Iterar sobre cada `transicion` en la lista de `transiciones`:
        -   Separar `transicion` en sus componentes (origen, entrada, sacarPila, destino, entraPila).
        -   Agregar una entrada al diccionario `transiciones` utilizando el valor `origen` como clave y un diccionario vacío como valor si la clave no existe.
        -   Agregar una entrada al diccionario interno utilizando el valor `entrada` como clave y el valor `destino` como valor.
-   Método `__str__()`:
    -   Convertir la lista de `estados` a una cadena separada por comas y asignarla a `estados_str`.
    -   Convertir la lista de `alfabeto` a una cadena separada por comas y asignarla a `alfabeto_str`.
    -   Convertir la lista de `estados_aceptacion` a una cadena separada por comas y asignarla a `estados_aceptacion_str`.
    -   Crear una lista de cadenas `transiciones_lista` que contenga las transiciones en formato "origen, entrada, destino".
    -   Unir los elementos de `transiciones_lista` en una cadena separada por saltos de línea y asignarla a `transiciones_str`.
    -   Retornar una cadena formateada que incluya información sobre el nombre, los estados, el alfabeto, el estado inicial, los estados de aceptación y las transiciones del autómata de pila.

![enter image description here](https://i.ibb.co/XJGgXZ6/image.png)

La función `verificar_alfabeto(alfabeto)` realiza la verificación de un alfabeto para asegurarse de que no contenga símbolos repetidos. Toma como parámetro una lista `alfabeto` y realiza las siguientes acciones:

-   Compara la longitud de un conjunto creado a partir de `alfabeto` con la longitud de `alfabeto`.
-   Si son diferentes, muestra un mensaje de error utilizando `messagebox.showerror()` y retorna `False`.
-   En caso contrario, retorna `True`.

La función `verificar_estado_inicial(estado_inicial, estados)` verifica que el estado inicial se encuentre en la lista de estados. Toma como parámetros el estado inicial y una lista de estados y realiza lo siguiente:

-   Verifica si `estado_inicial` no está en `estados`.
-   Si no se cumple la condición, muestra un mensaje de error utilizando `messagebox.showerror()` y retorna `False`.
-   En caso contrario, retorna `True`.

La función `Estados_aceptacion(estados_aceptacion, estados)` verifica que los estados de aceptación estén presentes en la lista de estados. Toma como parámetros una lista de estados de aceptación y una lista de estados y realiza lo siguiente:

-   Itera sobre cada `estado` en `estados_aceptacion`.
-   Verifica si `estado` no está en `estados`.
-   Si no se cumple la condición, muestra un mensaje de error utilizando `messagebox.showerror()` y retorna `False`.
-   Si se cumple para todos los estados de aceptación, retorna `True`.

La función `verificar_transiciones(transiciones, estados, alfabeto, SimboloPila)` realiza la verificación de las transiciones del autómata. Toma como parámetros una lista de transiciones, una lista de estados, un alfabeto y una lista de símbolos de pila, y realiza lo siguiente:

-   Itera sobre cada `transicion` en `transiciones`.
-   Divide `transicion` en sus componentes (origen, entrada, sacarPila, destino, entraPila).
-   Verifica si los estados de origen y destino están presentes en la lista de estados.
-   Verifica si el símbolo de entrada está presente en el alfabeto.
-   Verifica si el símbolo de sacarPila está presente en la lista de símbolos de pila.
-   Verifica si el símbolo de entraPila está presente en la lista de símbolos de pila.
-   Si alguna de las verificaciones no se cumple, muestra un mensaje de error utilizando `messagebox.showerror()` y retorna `False`.
-   Si todas las verificaciones se cumplen para todas las transiciones, retorna `True`

![enter image description here](https://i.ibb.co/Vv7GFjP/image.png)

La función `comprobar_cadena_ap(ap, cadena)` se utiliza para comprobar si una cadena es aceptada por un autómata de pila (AP). Toma como parámetros un objeto de la clase AutomataPila (`ap`) y una cadena (`cadena`), y realiza lo siguiente:

-   Agrega el símbolo de inicio de pila (`$`) al inicio y final de la cadena.
    
-   Establece el estado actual como el estado inicial del AP.
    
-   Itera sobre cada caracter en la cadena:
    
    -   Verifica si el caracter no está en el alfabeto del AP. Si no se cumple esta condición, muestra un mensaje de error utilizando `messagebox.showerror()` y retorna `False`.
    -   Verifica si no hay una transición definida para el estado actual y el caracter en el AP. Si no se cumple esta condición, muestra un mensaje de error utilizando `messagebox.showerror()` y retorna `False`.
    -   Actualiza el estado actual según la transición correspondiente en el AP.
-   Si el estado actual está en los estados de aceptación del AP, retorna un mensaje indicando que la cadena es válida en el AP.
    
-   En caso contrario, retorna un mensaje indicando que la cadena no es válida en el AP.
    

El mensaje de error muestra información sobre el caracter o estado que no está definido o no pertenece al AP en cuestión.


![enter image description here](https://i.ibb.co/kSQ7LGJ/image.png)

La función `comprobar_cadena_ap_ruta(ap, cadena)` se utiliza para comprobar una cadena en un autómata de pila (AP) y mostrar la ruta seguida durante la verificación. Toma como parámetros un objeto de la clase AutomataPila (`ap`) y una cadena (`cadena`) a verificar, y realiza lo siguiente:

-   Agrega el símbolo de inicio de pila (`$`) al inicio y final de la cadena.
    
-   Establece el estado actual como el estado inicial del AP.
    
-   Crea una lista vacía llamada `transicion` para almacenar las transiciones realizadas durante la verificación.
    
-   Itera sobre cada caracter en la cadena:
    
    -   Verifica si el caracter no está en el alfabeto del AP. Si no se cumple esta condición, muestra un mensaje de error utilizando `messagebox.showerror()` y retorna `False`.
        
    -   Verifica si no hay una transición definida para el estado actual y el caracter en el AP. Si no se cumple esta condición, muestra un mensaje de error utilizando `messagebox.showerror()` y retorna `False`.
        
    -   Actualiza el estado actual según la transición correspondiente en el AP.
        
    -   Itera sobre cada transición en `ap.transicionesN` (transiciones con detalles):
        
        -   Divide la transición en sus componentes: origen, entrada, sacarPila, destino, entraPila.
        -   Compara si el origen, la entrada y el destino coinciden con el estado anterior, el caracter actual y el estado actual respectivamente.
        -   Si hay una coincidencia, crea una cadena de ruta formateada con los detalles de la transición y la agrega a la lista `transicion`.
-   Si el estado actual está en los estados de aceptación del AP:
    
    -   Llama a la función `Interfaz.VentanaRuta.VistaRuta()` para mostrar la ventana de ruta con los parámetros de la cadena, la lista de transiciones y el nombre del AP.
-   En caso contrario, retorna un mensaje indicando que la cadena no es válida en el AP.
    

Si se encuentran errores en el alfabeto o en las transiciones, se mostrarán mensajes de error específicos utilizando `messagebox.showerror()`.

![enter image description here](https://i.ibb.co/NZFNHgW/image.png)

La función `comprobar_cadena_ap_Paso(ap, cadena)` se utiliza para comprobar una cadena en un autómata de pila (AP) y generar el paso a paso del proceso de verificación. Toma como parámetros un objeto de la clase AutomataPila (`ap`) y una cadena (`cadena`) a verificar, y realiza lo siguiente:

-   Primero verifica si la cadena es válida rápidamente utilizando la función `comprobarCadenaRapido(ap, cadena)`. Si la cadena no es válida, muestra un mensaje de error utilizando `messagebox.showerror()` y retorna `False`.
    
-   Agrega el símbolo de inicio de pila (`$`) al inicio y final de la cadena.
    
-   Establece el estado actual como el estado inicial del AP.
    
-   Crea una lista vacía llamada `transicion` para almacenar las transiciones realizadas durante la verificación.
    
-   Crea una cadena vacía llamada `caracteres` para almacenar los caracteres de la cadena que se van procesando.
    
-   Itera sobre cada caracter en la cadena:
    
    -   Agrega el caracter actual a la cadena `caracteres`.
        
    -   Verifica si el caracter no está en el alfabeto del AP. Si no se cumple esta condición, muestra un mensaje de error utilizando `messagebox.showerror()` y retorna `False`.
        
    -   Verifica si no hay una transición definida para el estado actual y el caracter en el AP. Si no se cumple esta condición, muestra un mensaje de error utilizando `messagebox.showerror()` y retorna `False`.
        
    -   Actualiza el estado actual según la transición correspondiente en el AP.
        
    -   Itera sobre cada transición en `ap.transicionesN` (transiciones con detalles):
        
        -   Divide la transición en sus componentes: origen, entrada, sacarPila, destino, entraPila.
        -   Compara si el origen, la entrada y el destino coinciden con el estado anterior, el caracter actual y el estado actual respectivamente.
        -   Si hay una coincidencia, crea una cadena de ruta formateada con los detalles de la transición y la agrega a la lista `transicion`.
-   Si el estado actual está en los estados de aceptación del AP:
    
    -   Llama a la función `Clases.RecorridoPasoaPaso.GenerarDOT()` para generar el diagrama de transiciones paso a paso con los parámetros del AP, la cadena, el estado actual, la lista de transiciones y la bandera `True` para indicar que es una cadena válida.
-   Si el estado actual no está en los estados de aceptación, retorna un mensaje indicando que la cadena no es válida en el AP.
    

Si se encuentran errores en el alfabeto o en las transiciones, se mostrarán mensajes de error específicos utilizando `messagebox.showerror()`. Durante el proceso de verificación, se generará un diagrama de transiciones paso a paso utilizando la función `Clases.RecorridoPasoaPaso.GenerarDOT()` en cada iteración del bucle para visualizar el proceso.

![enter image description here](https://i.ibb.co/8c1Dk04/image.png)

La función `SoloPaso(ap, cadena)` se utiliza para realizar la verificación de una cadena en un autómata de pila (AP) y mostrar el proceso paso a paso en una ventana de ruta. Toma como parámetros un objeto de la clase AutomataPila (`ap`) y una cadena (`cadena`) a verificar, y realiza lo siguiente:

-   Primero verifica si la cadena es válida rápidamente utilizando la función `comprobarCadenaRapido(ap, cadena)`. Si la cadena no es válida, muestra un mensaje de error utilizando `messagebox.showerror()` y retorna `False`.
    
-   Agrega el símbolo de inicio de pila (`$`) al inicio y final de la cadena.
    
-   Establece el estado actual como el estado inicial del AP.
    
-   Crea una lista vacía llamada `info` para almacenar la información del proceso paso a paso.
    
-   Crea una lista vacía llamada `pila` para simular la pila del AP.
    
-   Crea una cadena vacía llamada `caracteres` para almacenar los caracteres de la cadena que se van procesando.
    
-   Itera sobre cada caracter en la cadena:
    
    -   Agrega el caracter actual a la cadena `caracteres`.
        
    -   Verifica si el caracter no está en el alfabeto del AP. Si no se cumple esta condición, muestra un mensaje de error utilizando `messagebox.showerror()` y retorna `False`.
        
    -   Verifica si no hay una transición definida para el estado actual y el caracter en el AP. Si no se cumple esta condición, muestra un mensaje de error utilizando `messagebox.showerror()` y retorna `False`.
        
    -   Actualiza el estado actual según la transición correspondiente en el AP.
        
    -   Itera sobre cada transición en `ap.transicionesN` (transiciones con detalles):
        
        -   Divide la transición en sus componentes: origen, entrada, sacarPila, destino, entraPila.
        -   Compara si el origen, la entrada y el destino coinciden con el estado anterior, el caracter actual y el estado actual respectivamente.
        -   Si hay una coincidencia, actualiza la pila según las reglas de sacar y agregar símbolos a la pila.
        -   Crea una cadena de ruta formateada con los detalles de la transición, la pila actual, y los caracteres procesados, y la agrega a la lista `info`.
-   Si la cadena es válida en el AP:
    
    -   Llama a la clase `VistaRuta` para mostrar una ventana con la información del proceso paso a paso.
-   Si la cadena no es válida, muestra un mensaje de error indicando que la cadena no es válida en el AP.
    

La clase `VistaRuta` es una ventana que muestra la información del proceso paso a paso en forma de tabla. Recibe la lista `info` con la información de cada iteración y crea etiquetas para mostrar la iteración, la pila, la entrada y la transición en columnas separadas en la ventana. Luego, llena la tabla con la información proporcionada en la lista `info`. Cada fila de la tabla representa una iteración del proceso paso a paso.

# Manual de Usuario

## Menu de bienvenida

![enter image description here](https://i.ibb.co/KbrLb4g/image.png)

## Menu Principal
![enter image description here](https://i.ibb.co/7JxRntN/image.png)
- Boton de Gramatica Libre de Contexto
	- Abrir Modulo de Gramatica Libre
- Boton de Modulo Automata de Pila
	- Abre el Modulo de Automatas de Pila
- Botón de Salir
	- Se cierra el programa completamente
	
## Modulo Gramática Libre de Contexto
![enter image description here](https://i.ibb.co/37FLv3v/image.png)

- Carga de Archivos
- Informacion General
	- Modulo para seleccionar los AP Cargados y el boton para generar la informacion en un pdf
![enter image description here](https://i.ibb.co/54vKhfQ/image.png)
- Arbol de Derivacion
	-  Se selecciona un AP y se carga la informacion para poder generar el arbol de derivacion
![enter image description here](https://i.ibb.co/k9VXtSn/image.png)
## Modulo de Automatas de Pila

![enter image description here](https://i.ibb.co/ZcBQBkm/image.png)
- Carga de Archivo
	- Abrira para poder seleccionar el archivo de carga
- Informacion del Automata de Pila
	- Se seleccionara un Automa de Pila y mostrara la informacion del automata en un PDF
	![enter image description here](https://i.ibb.co/w0kKTdc/image.png)
- Ruta
	- ![enter image description here](https://i.ibb.co/25HDr1y/image.png)