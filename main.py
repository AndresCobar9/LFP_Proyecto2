import tkinter as tk
from Interfaz.MenuPrincipal import MenuPrincipal 
from Interfaz.MenuPrincipal import MenuEmergente

def iniciar_programa():
    menu_principal = MenuEmergente()
    menu_principal.mainloop()



if __name__ == '__main__':
    iniciar_programa()