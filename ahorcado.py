import random
import string
from logo import art
from palabras import lista_palabras
from ahorcado_diagramas import vidas_diccionario_visual

"""---------------------------------FUNCIONES--------------------------------------------------"""


def valida_cadena(texto):
    """VALIDA QUE LA CADENA DE CARACTERES NO TENGA DIGITOS NI CARACTERES ESPECIALES"""
    cadena = input(texto)

    while cadena.isdigit() or not cadena.isalpha():
        cadena = input("ERROR ----> NO INGRESAR DIGITOS NI CARACTERES ESPECIALES" + texto)

    return cadena


def obtener_palabra_valida(palabras):
    """SELECCIONA UNA PALABRA AL AZAR DE LA LISTA DE PALABRAS"""
    palabra = random.choice(palabras)

    while "-" in palabra or " " in palabra:
        palabra = random.choice(palabras)

    return palabra.upper()


def ahorcado(score):
    """FUNCION DEL JUEGO DEL AHORCADO"""
    print(art)

    palabra = obtener_palabra_valida(lista_palabras)
    letras_por_adivinar = set(palabra)

    print(letras_por_adivinar)

    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase)
    vidas = 7

    print("Tenes 7 vidas. Suerte!")

    while len(letras_por_adivinar) > 0 and vidas > 0:

        if len(letras_adivinadas) > 0:
            print(f"\nLetras utilizadas: {' '.join(letras_adivinadas)}")

        """MOSTRAMOS EL ESTADO ACTUAL DE LA PALABRA"""
        palabra_lista = [letra if letra in letras_adivinadas else "-" for letra in palabra]

        """MOSTRAMOS ESTADO DEL AHORCADO"""
        print(vidas_diccionario_visual[vidas])

        """MOSTRAMOS LAS LETRAS SEPARADAS POR ESPACIO"""
        print(f"Palabra: {' '.join(palabra_lista)}")

        letra_usuario = input("Elige una letra: ").upper()

        """SI LA LETRA ES CORRECTA SE AGREGA AL CONJUNTO DE LETRAS_ADIVINADAS"""
        if letra_usuario in (abecedario - letras_adivinadas):
            letras_adivinadas.add(letra_usuario)

            """SI LA LETRA ESTA EN LA PALABRA, SE QUITA UNA LETRA POR ADIVINAR, SINO SE RESTA UNA VIDA"""
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)

            else:
                vidas = vidas - 1
                if vidas > 0:
                    print(f"\nTe quedan {vidas} vidas")

                print(f"\nLa letra {letra_usuario} no esta en la palabra.")

        elif letra_usuario in letras_adivinadas:
            print("\nERROR ---> YA INGRESASTE ESA LETRA, INGRESA UNA NUEVA.")
        else:
            print("\nERROR -----> LETRA NO VALIDA")

    """SE LLEGA A ESTA LINEA CUANDO SE ACABARON LAS VIDAS O SE ADIVINA LA PALABRA"""

    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"AHORCADO, PERDISTE. LA PALABRA ERA: {palabra}")
        return score

    else:
        print(f"ADIVINASTE! LA PALABRA ERA: {palabra}")

        return ahorcado(score + 1)


def escribir_archivo(nom, ape, sco):
    """FUNCION PARA ESCRIBIR EN EL ARCHIVO, NOMBRE, APELLIDO Y SCORE DEL JUGADOR"""
    try:
        with open(r'scoreboard.csv', 'a') as arch_score:

            arch_score.write(f"{nom};{ape};{str(sco)}\n")

    except IOError as mensaje:
        print(f"ERROR -------> {mensaje}")


def mostrar_tabla_maxima(ln, la, ls):
    """MUESTRA EN FORMATO TABLA LOS 3 JUGADORES CON LOS SCORES MAS ALTOS"""
    cont = 0

    print("\n -----------------TOP 3 SCORES-------------------")
    print("--------------------------------------------------")
    print("|      NOMBRE       |     APELLIDO     |  SCORE  |")
    print("----------------------------------------------------")
    for sco, nom, ape in sorted(zip(ls, ln, la), reverse=True):

        fila_formateada = "| {:<17} | {:<17} | {:^7} |".format(nom, ape, sco)
        print(fila_formateada)

        cont += 1
        if cont == 3:
            break

    print("--------------------------------------------------")


def lee_archivo():
    """FUNCION QUE LEE EL ARCHIVO SCOREBOARD Y SEPARA LOS DATOS PARA MOSTRARLO EN LA TABLA"""
    try:
        with open(r'scoreboard.csv', 'r') as arch_scores:

            contenido = arch_scores.readline()
            lista_nombres = []
            lista_apellidos = []
            lista_scores = []

            while contenido:
                contenido = contenido.strip()
                nombres, apellidos, scores = contenido.split(";")
                lista_nombres.append(nombres)
                lista_apellidos.append(apellidos)
                lista_scores.append(scores)

                contenido = arch_scores.readline()

        mostrar_tabla_maxima(lista_nombres, lista_apellidos, lista_scores)

    except IOError as mensaje:
        print(f"ERROR ------> {mensaje}")


"""---------------------------------PROGRAMA PRINCIPAL--------------------------------------------------"""

puntos = 0
score_nuevo = ahorcado(puntos)

nombre = valida_cadena("\nIngrese su nombre: ").title()
apellido = valida_cadena("Ingrese su apellido: ").title()

escribir_archivo(nombre, apellido, score_nuevo)
lee_archivo()
