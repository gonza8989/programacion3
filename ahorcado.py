def jugar():
    print ("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
    print ("Bienvenido al juego del ahorcado")
    print ("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
    
    palabra_secreta = "mandarina"
    
    ahorcado = False
    acerto = False
    
    while(not ahorcado and not acerto):
        entrada = input('ingresar una letra ...')
        for letra in palabra_secreta:
            if(entrada == letra):
                print(entrada)
        
        
    print("Fin del juego")
    
if(__name__ == "__main__"):
    jugar()