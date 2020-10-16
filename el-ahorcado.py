#!/usr/bin/env python3

import os 

palabra_adivinar = 'mosto'
intentos_permitidos = 5
intentos_realizados = 0

#Definimos función que comprueba si la letra está en la palabra
def letra_en_palabra(letra_adivinar, palabra_definitiva):
    if letra_adivinar not in palabra_definitiva:
        return False
    else:
        return True

#Bucle que se ejecuta mientras que intentos realizados sea menor o igual que intentos permitidos
while intentos_realizados <= intentos_permitidos:
    print(f'Intentos realizados: {intentos_realizados}')
    letra = input('Introduce letra: ')
    pertenece = letra_en_palabra(letra, palabra_adivinar)
    if pertenece == False:
        intentos_realizados+=1
        os.system('cls')
    else:
        True

