import random
import os

characters = ["Albedo", "Alhacen", "Aloy", "Arataki Itto", "Baizhu", "Cyno", "Dehya", "Diluc", "Eula", "Furina",
              "Ganyu", "Hu Tao", "Jean", "Kazuha", "Ayaka", "Ayato", "Keching", "Klee", "Lyney", "Mona", "Nahida",
              "Neuvillette", "Nilou", "Qiqi", "Kokomi", "Shenhe", "Shogun Raiden", "Tartaglia", "Tignari", "Scaramouche",
              "Venti", "Viajero", "Wriothesley", "Xiao", "Yae Miko", "Yelan", "Yoimiya", "Zhongli", "Amber", "Beidou",
              "Bennett", "Barbara", "Candace", "Charlotte", "Chongyun", "Collei", "Diona", "Dori", "Faruzan", "Fischl",
              "Freminet", "Gorou", "Kaeya", "Kaveh", "Kirara", "Kujou Sara", "Kuki Shinobu", "Laila", "Lisa", "Lynette",
              "Mika", "Ninguang", "Noelle", "Razor", "Rosaria", "Sacarosa", "Sayu", "Heizou", "Thoma", "Xiangling",
              "Xingchiu", "Xinyan", "Yanfei", "Yaoyao", "Yun Jin"]

def iniciarGame():
    index = random.randint(0, len(characters) - 1)       #Numero aleatorio para elejir el personaje
    letras = len(characters[index])                         #Longitud de la palabra
    personaje = characters[index].upper()                   #Personaje que hay que adivinar
    gess = ""                                               #String que contiene la respuesta del jugador
    vidas = 5                                               #Numero de intentos restantes
    print("Respuesta : "+personaje)
    '''
    Preparacion del String respuesta del juego
    "_" Quiere decir que no existe esta letra en la palabra final o aun no se ha indicado
    "?" La letra indicada en esta posicion esta en la palabra final pero en una posicion diferente
    "ABC..." Un caracter indica que se ha acertado el caracter en esa posicion
    '''
    #Crea un String de tamaño igual a la palabra final que solo contenga "_"
    for i in range(letras):
        gess = gess[:i] + "_" + gess[i+1:]

    print(gess)

    #Inicio del juego
    while True:
        #Si las vidas son 0 se termina la partida
        if vidas == 0:
            return

        #Obtiene por consola la respuesta
        respuesta = input().upper()

        #Comando auxiliar para volver al menu
        if respuesta == "QUIT()":
            limpiarConsola()
            return

        #Elimina el salto de linea del final de la entrada
        respuesta = respuesta.replace("\n","")

        #Revisa que String es mas corto para hacer las iteraciones en funcion de este
        k = len(personaje)
        if len(respuesta) < len(personaje):
            k = len(respuesta)

        #Comprueba si las letras de la palabra introducida esta en la palabra final, en tal caso lo sustituye por el caracter que corresponda
        for i in range(k):
            if respuesta[i] == personaje[i]:
                gess = gess[:i] + respuesta[i].upper() + gess[i+1:]
            elif inWord(respuesta, personaje, i):
                if gess[i] == "_":
                    gess = gess[:i] + "?" + gess[i+1:]
                
        #Imprimer la palabra que has escrito y si es correcta termina la partida
        print(gess)

        gess = gess.replace("?","_")

        if gess == personaje:
            limpiarConsola()
            print("Has ganado  en " + str(6 - vidas) + " intentos")
            return

        #En caso de no estar correcta la palabra resta 1 intento y continua
        vidas -= 1
        print(f"Intentos restantes {vidas}")

        #Si no quedan mas intentos termina la partida
        if vidas == 0:
            print("Has perdido, no te quedan intentos")
            return


def inWord(respuesta, palabra, iteraton):
    i = iteraton
    letra = respuesta[i]

    k = len(palabra)
    if len(respuesta) < len(palabra):
        k = len(respuesta)

    if letraDup(letra, palabra):
        return
    else:
        for m in range(k):
            if palabra[m] == letra:
                return True
        return False

def letraDup(letra, palabra):
    count = 0
    for i in range(len(palabra)):
        if letra == palabra[i]:
            count += 1

    if count > 1:
        return True

    return False

def limpiarConsola():
    sistema_operativo = os.name

    if sistema_operativo == 'posix':  # Para sistemas basados en Unix/Linux/Mac
        os.system('clear')
    elif sistema_operativo == 'nt':  # Para sistemas basados en Windows
        os.system('cls')


def displayMenu():
    while True:
        print("Que deseas hacer?\n[1] Iniciar partida\n[2] Salir")
        entrada = int(input())
        if entrada == 1:
            iniciarGame()
        elif entrada == 2:
            return
        else:
            limpiarConsola()
            print("Opcion no valida, vuelva a ingresar su opcion")

def main():
    limpiarConsola()
    displayMenu()
    print("Fin, Bye Bye")



if __name__ == "__main__":
    main()