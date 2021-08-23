"""Funciones de ayuda"""

import os
import platform

#Funcion para limpiar boofer

def clear():  
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def input_text(min_lenght, max_lenght):
    while True:
        text=input(">")
        if len(text) >=min_lenght and len(text) <= max_lenght:
            return text