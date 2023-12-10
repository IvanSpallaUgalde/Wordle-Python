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


def iniciar_game():
    index = random.randint(0, len(characters) - 1)
    final_word = characters[index].upper()
    letras = len(final_word)
    guess = ""
    vidas = 5
    print("Respuesta: " + final_word)

    print(guess)

    while True:

        personaje = final_word
        letras_pool = final_word

        for i in range(letras):
            guess = guess[:i] + "_" + guess[i + 1:]

        respuesta = input().upper()

        if respuesta == "QUIT()":
            limpiar_consola()
            return

        respuesta = respuesta.replace("\n", "")

        k = len(personaje)
        if len(respuesta) < len(personaje):
            k = len(respuesta)

        for i in range(k):
            if respuesta[i] == personaje[i]:
                guess = guess[:i] + respuesta[i] + guess[i+1:]
                letras_pool = eliminar_letra(respuesta[i], letras_pool)

        for i in range(k):
            if guess[i] == "_":
                if in_word(respuesta[i], letras_pool):
                    guess = guess[:i] + "?" + guess[i + 1:]

        if (guess == final_word) and (len(final_word) == len (respuesta)):
            print(guess)
            print(f"Has ganado en {6 - vidas} intentos")
            return
        elif (guess == final_word) and (len(final_word) != len(respuesta)):
            print("Dentro de la palabra que has escrito esta la respuesta correcta")
        else:
            print(guess)
            print("Respuesta incorrecta")

        vidas -= 1
        print(f"Intentos restantes {vidas}")


def in_word(letra, palabra):
    return letra in palabra


def eliminar_letra(letra, word):
    for i in range(len(word)):
        if word[i] == letra:
            word = word[:i] + word[i + 1:]
            return word


def limpiar_consola():
    sistema_operativo = os.name

    if sistema_operativo == 'posix':  # Para sistemas basados en Unix/Linux/Mac
        os.system('clear')
    elif sistema_operativo == 'nt':  # Para sistemas basados en Windows
        os.system('cls')


def display_menu():
    while True:
        print("Que deseas hacer?\n[1] Iniciar partida\n[2] Salir")
        entrada = int(input())
        if entrada == 1:
            iniciar_game()
        elif entrada == 2:
            return
        else:
            limpiar_consola()
            print("Opcion no valida, vuelva a ingresar su opcion")


def main():
    limpiar_consola()
    display_menu()
    print("Fin, Bye Bye")


if __name__ == "__main__":
    main()
