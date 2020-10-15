miNombre = input('Introduce nombre del jugador: ')
maximo_intentos = 5

print('_ o _ _ o')

letra = input('Escoge una letra: ')
if letra == 'm':
    print('m o _ _ o')
    letra = input('Escoge otra letra: ')
    if letra == 's':
        print('m o s _ o')
        letra = input('Escoge otra letra: ')
        if letra == 't':
            print('m o s t o')
            print(f'¡La palabra era MOSTO!')
        else:
            print(f'Intentos restantes {maximo_intentos - 1}')
    elif letra == 't':
        print('m o _ t o')
        letra = input('Escoge otra letra: ')
        if letra == 's':
            print('m o s t o')
            print(f'¡La palabra era MOSTO!')
        else:
            print(f'Intentos restantes {maximo_intentos - 1}')
    else:
        print(f'Intentos restantes {maximo_intentos - 1}')
elif letra == 's':
    print('_ o s _ o')
    letra = input('Escoge otra letra: ')
    if letra == 'm':
        print('m o s _ o')
        letra = input('Escoge otra letra: ')
        if letra == 't':
            print('m o s t o')
            print(f'¡La palabra era MOSTO!')
        else:
            print(f'Intentos restantes {maximo_intentos - 1}')
    elif letra == 't':
        print('_ o s t o')
        letra = input('Escoge otra letra: ')
        if letra == 'm':
            print('m o s t o')
            print(f'¡La palabra era MOSTO!')
        else:
            print(f'Intentos restantes {maximo_intentos - 1}')
    else:
        print(f'Intentos restantes {maximo_intentos - 1}')
elif letra == 't':
    print('_ o _ t _')
    letra = input('Escoge otra letra: ')
    if letra == 'm':
        print('m o _ t o')
        letra = input('Escoge otra letra: ')
        if letra == 's':
            print('m o s t o')
            print(f'¡La palabra era MOSTO!')
    elif letra == 's':
            print('_ o s t o')
            letra = input('Escoge otra letra: ')
            if letra == 'm':
                print('m o s t o')
                print(f'¡La palabra era MOSTO!')
            else:
                print(f'Intentos restantes {maximo_intentos - 1}')
    else:
        print(f'Intentos restantes {maximo_intentos - 1}')   
else:
    print(f'Intentos restantes {maximo_intentos - 1}')
