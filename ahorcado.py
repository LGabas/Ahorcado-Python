import random
import string

from palabras import palabras
from ahorcado_diagramas import vidas_diccionario_visual

#-----------------FUNCIONES-------------
def obtener_palabra_valida(palabras):
    #Selecciona una palabra valida al azar de la lista de palabras
    palabra = random.choice(palabras)

    while "-" in palabra or " " in palabra:

        palabra = random.choice(palabras)

    return palabra.upper()

def ahorcado():

    print("=============================")
    print("   BIENVENIDO AL AHORCADO  ")
    print("=============================")

    palabra  = obtener_palabra_valida(palabras)

    letras_por_adivinar = set(palabra)
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase)

    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:

        print(f"Te quedan {vidas} vidas")
        
        if len(letras_adivinadas) > 0:

            print(f"Has usado estas letras: {' '.join(letras_adivinadas)}")

        # Mostramos el estado actual de la palabra
        palabra_lista = [letra if letra in letras_adivinadas else "-" for letra in palabra]
        # Mostramos estado del ahorcado
        print(vidas_diccionario_visual[vidas])
        # Mostramos las letras separadas por un espacio
        print(f"Palabra: {' '.join(palabra_lista)}")

        letra_usuario = input("Elige una letra: ").upper()

        # Si la letra es correcta se agrega la letra al conjunto de letras ingresadas
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            # Si la letra esta en la palabra, se quita una letra por adivinar, de lo contrario se resta una vida
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print(" ") 

            else:

                vidas = vidas - 1
                print(f"\nTu letra, {letra_usuario} no esta en la palabra.")
        # Si la letra elegida ya fue ingresada
        elif letra_usuario in letras_adivinadas:
            print("\nYa elegiste esa letra, elige una nueva letra.")
        else:
            print("\nEsta letra no es valida.")    

    # El juego llega a esta linea cuando se adivina todas las letras de la palabra o cuando se termiman las vidas del jugador

    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print("AHORCADO, PERDISTE. LA PALABRA ERA: {palabra}")
    else:
        print("GANASTE!! ADIVINASTE LA PALABRA: {palabra}")


#---------------------------PROGRAMA PRINCIPAL------------------

ahorcado()












    
