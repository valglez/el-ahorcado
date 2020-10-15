miNombre = input('Introduce nombre del jugador: ')

intentos = 0
error = 0
intentos_maximos = 5
intentos_restantes = intentos_maximos - error

print('_ o _ _ o')

while intentos < 5:

    letra = input('Escoge una letra: ')
    if letra == 'm':
        print('m o _ _ o')

        intentos+=1

        letra = input('Escoge otra letra: ')
        if letra == 's':
            print('m o s _ o')

            intentos+=1

            letra = input('Escoge otra letra: ')
            if letra == 't':
                print('m o s t o')

                intentos+=1

                print(f'¡La palabra era MOSTO! {miNombre}, has acertado en {intentos} intentos')
                break
            else:
                print(f'Intentos restantes {intentos_restantes}')
                print('m o s _ o')

                intentos+=1
                error+=1

                letra = input('Escoge otra letra: ')
                if letra == 't':
                    print('m o s t o')
                
                    intentos+=1

                    print(f'¡La palabra era MOSTO! {miNombre}, has acertado en {intentos} intentos')
                    break

        elif letra == 't':
            print('m o _ t o')

            intentos+=1

            letra = input('Escoge otra letra: ')
            if letra == 's':
                print('m o s t o')

                intentos+=1

                print(f'¡La palabra era MOSTO! {miNombre}, has acertado en {intentos} intentos')
                break
            else:
                print(f'Intentos restantes {intentos_restantes}')
                print('m o _ t o')

                intentos+=1
                error+=1

                letra = input('Escoge otra letra: ')
                if letra == 's':
                    print('m o s t o')
                
                    intentos+=1

                    print(f'¡La palabra era MOSTO! {miNombre}, has acertado en {intentos} intentos')
                    break
        else:
            print(f'Intentos restantes {intentos_restantes}')
            print('m o s _ o')

            intentos+=1
            error+=1

            letra = input('Escoge otra letra: ')
            if letra == 't':
                print('m o s t o')
            
                intentos+=1

                print(f'¡La palabra era MOSTO! {miNombre}, has acertado en {intentos} intentos')
                break
    elif letra == 's':
        print('_ o s _ o')

        intentos+=1

        letra = input('Escoge otra letra: ')
        if letra == 'm':
            print('m o s _ o')

            intentos+=1

            letra = input('Escoge otra letra: ')
            if letra == 't':
                print('m o s t o')

                intentos+=1

                print(f'¡La palabra era MOSTO! {miNombre}, has acertado en {intentos} intentos')
                break
            else:
                print(f'Intentos restantes {intentos_restantes}')
        elif letra == 't':
            print('_ o s t o')

            intentos+=1

            letra = input('Escoge otra letra: ')
            if letra == 'm':
                print('m o s t o')

                intentos+=1

                print(f'¡La palabra era MOSTO! {miNombre}, has acertado en {intentos} intentos')
                break
            else:
                print(f'Intentos restantes {intentos_restantes}')
        else:
            print(f'Intentos restantes {intentos_restantes}')
    elif letra == 't':
        print('_ o _ t _')

        intentos+=1
        
        letra = input('Escoge otra letra: ')
        if letra == 'm':
            print('m o _ t o')

            intentos+=1

            letra = input('Escoge otra letra: ')
            if letra == 's':
                print('m o s t o')

                intentos+=1

                print(f'¡La palabra era MOSTO! {miNombre}, has acertado en {intentos} intentos')
                break
        elif letra == 's':
                print('_ o s t o')

                intentos+=1

                letra = input('Escoge otra letra: ')
                if letra == 'm':
                    print('m o s t o')

                    intentos+=1

                    print(f'¡La palabra era MOSTO! {miNombre}, has acertado en {intentos} intentos')
                    break
                else:
                    print(f'Intentos restantes {intentos_restantes}')
        else:
            print(f'Intentos restantes {intentos_restantes}')
    else:
        print(f'Intentos restantes {intentos_restantes}')    