import os
import random

characters = ["Albedo", "Alhacen", "Aloy", "Arataki Itto", "Baizhu", "Cyno", "Dehya", "Diluc", "Eula", "Furina",
              "Ganyu", "Hu Tao", "Jean", "Kazuha", "Ayaka", "Ayato", "Keching", "Klee", "Lyney", "Mona", "Nahida",
              "Neuvillette", "Nilou", "Qiqi", "Kokomi", "Shenhe", "Shogun Raiden", "Tartaglia", "Tignari",
              "Scaramouche",
              "Venti", "Viajero", "Wriothesley", "Xiao", "Yae Miko", "Yelan", "Yoimiya", "Zhongli", "Amber", "Beidou",
              "Bennett", "Barbara", "Candace", "Charlotte", "Chongyun", "Collei", "Diona", "Dori", "Faruzan", "Fischl",
              "Freminet", "Gorou", "Kaeya", "Kaveh", "Kirara", "Kujou Sara", "Kuki Shinobu", "Laila", "Lisa", "Lynette",
              "Mika", "Ninguang", "Noelle", "Razor", "Rosaria", "Sacarosa", "Sayu", "Heizou", "Thoma", "Xiangling",
              "Xingchiu", "Xinyan", "Yanfei", "Yaoyao", "Yun Jin"]


def iniciarGame():
    index = random.randint(0, len(characters) - 1)
    finalWord = characters[index].upper()
    letras = len(finalWord)
    gess = ""
    vidas = 5
    print("Respuesta: " + finalWord)

    print(gess)

    while True:

        personaje = finalWord
        letrasPool = finalWord

        for i in range(letras):
            gess = gess[:i] + "_" + gess[i + 1:]

        respuesta = input().upper()

        if respuesta == "QUIT()":
            limpiarConsola()
            return

        respuesta = respuesta.replace("\n", "")

        k = len(personaje)
        if len(respuesta) < len(personaje):
            k = len(respuesta)

        for i in range(k):
            if respuesta[i] == personaje[i]:
                gess = gess[:i] + respuesta[i] + gess[i+1:]
                letrasPool = eliminarLetra(respuesta[i], letrasPool)

        for i in range(k):
            if gess[i] == "_":
                if inWord(respuesta[i], letrasPool):
                    gess = gess[:i] + "?" + gess[i + 1:]

        print(gess)

        if gess == finalWord:
            print(f"Has ganado en {6 - vidas} intentos")
            return

        vidas -= 1
        print(f"Intentos restantes {vidas}")


def inWord(letra, palabra):
    for i in range(len(palabra)):
        if letra == palabra[i]:
            return True
    return False


def eliminarLetra(letra, word):
    for i in range(len(word)):
        if word[i] == letra:
            word = word[:i] + word[i + 1:]
            return word


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
