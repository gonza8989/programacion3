def jugar():
    
    print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
    print("Bienvenido al juego del ahorcado")
    print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
    
    palabera_secreta = 'mandarina'
    
    ahorcado = False
    acerto = False
    
    while(not ahorcado and not acerto):
        entrada = input('ingrese ina letra....')
        entrada = entrada.strip()
        entrada = entrada.lower()
        indice = 0
        
        for letra in palabera_secreta:
            if(entrada == letra):
                print('se encontro la letra {} en la posicion {}'.format(letra,indice))

                indice = indice + 1

        print('jugando ....')

    print('fin del juego.....')

if (__name__ == '__main__'):
    jugar()