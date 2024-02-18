import discord
import sys
import time

from discord.ext import commands
from BotGame import BotGame

'''
------------------------------------------Function definition zone------------------------------------------------------
'''


def check_user(id: int):
    global games_list
    for i in range(len(games_list)):
        if games_list[i].get_user_id() == id:
            return i
    return -1


def remove_all_extra_spaces(string: str):
    return " ".join(string.split())


def finish_game(i: int):
    del games_list[i]


'''
---------------------------------------End of Function definiton zone---------------------------------------------------
'''

f = open("token.txt", "r")
BOT_TOKEN = f.read()
CHANNEL_ID = 1206981689356714024

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

games_list = []

help_msg = ("Comandos:\n\!ayuda: Te repito los comandos que tienes disponibles\n!play: Pienso en un personaje para que "
            "lo adivines. Si ya he penasdo en uno tienes que adivinar ese primero\n!intentos: te dice cuantos intentos "
            "llevas\n!p: Si estas en partida con este comando me puedes decir que personaje crees que tengo en mente\n"
            "!end: Si no te ves capaz de adivinar el presonaje, te rindes y te digo que personaje era")

rules_msg = ("Para jugar al juego es muy sencillo. Pensare en un personaje de genshin impact, y te dare cuantas letras"
             "tiene. \nPor ejemplo:\nSi el personaje es **Hu tao**, entonces te dare lo siguiente: **-- ---**\n\n"
             "Ademas, para facilitar la tarea visualemente usare emoticonos para que te resulte mas facil saber que"
             "letras tienes mal y cuales bien\n"
             ":green_square: :point_left: Este cuadrado verde representa que esta letra esta en la posicion correcta\n"
             ":orange_square: :point_left: Este cuadrado naranja representa que esta letra esta en una posicion "
             "incorrecta\n"
             ":white_large_square: :point_left: Este cuadrado blanco representa que el personaje no tiene esta letra"
             "en el nombre\n\n"
             ":warning: _*Es importante saber lo siguiente antes de jugar*_ :warning:\n"
             "1.\tLa palabra que me digas tiene que ser igual de largas y tener los espacios en el mismo sitio que "
             "tiene el personaje\n"
             "2.\tLos nombres que tendras que adivinar estan sacados de la pagina: https://genshin.honeyhunterworld.com"
             "/fam_chars/?lang=EN \n"
             "3.\tEl creador de este juego <@200636184110694400> se ha tomado la libertad de cambiar los siguientes "
             "nombre: \n"
             "\tKaedehara Kazuha :point_right: Kazuha\n"
             "\tShikanoin Heizou :point_right: Heizou\n"
             "\tTraveler :point_right: Aether\n"
             "\tTraveler :point_right: Lumine\n"
             "\tWanderer :point_right: Scaramouche\n\n"
             "Ya estas listo para jugar!! Si tienes alguna duda puedes preguntarlo en <#1208760758935093268> y el "
             "creador del juego te resolvera tus dudas")


@bot.event
async def on_ready():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(f"Hola! Paimon quiere comprobar cuanto sabes sobre Genshin Impact. Seras capaz de adivinar "
                       f"en que personaje estoy pensando?\n\n"
                       f"{help_msg}\n\n{rules_msg}")
    '''
    await channel.send(help_msg)
    await channel.send(":warning: Es importante saber lo siguiente antes de jugar :warning:")
    await channel.send("***Como los personajes de Genshin Impact tienen nombres de diferentes longitudes, la cantidad de 
    cuadrados que salen corresponde al numero de letras del personaje que hay que adivinar***")

    await channel.send(":green_square: :point_left: Este cuadrado verde representa que la letra en esta posicion de tu 
    respuesta es correcta")
    await channel.send(":orange_square: :point_left: Este cuadrado naranja representa que la letra en esta posicion de 
    tu respuesta esta en la respuesta correcta pero en una posicion diferente")
    await channel.send(":white_large_square: :point_left: Este cuadrado blanco representa que la letra en esta posicion 
    de tu respuesta es no esta en la respuesta correcta, o que en esta posicion no has puesto ninguna letra")
    '''


@bot.command()
async def ayuda(ctx):
    await ctx.send(help_msg)


@bot.command()
async def play(ctx):
    global games_list
    i = check_user(ctx.author.id)
    if i < 0:
        aux = BotGame(ctx.author.id)
        games_list.append(aux)
        string1 = aux.get_resp_fin()
        string2 = ""
        for i in range(len(string1)):
            if string1[i] != " ":
                string2 += ":white_large_square:"
            else:
                string2 += "   "
        await ctx.send(f"Juego de <@{aux.get_user_id()}> iniciado\n{string1}\n{string2}")
    else:
        await ctx.send(f"<@{ctx.author.id}> ya estas en partida")


@bot.command()
async def pj(ctx):
    global games_list
    i = check_user(ctx.author.id)
    if i < 0:
        await ctx.send("Not in game")
    else:
        personaje = games_list[i].get_personaje()
        await ctx.send(f"Tu personaje es: {personaje}")


@bot.command()
async def intentos(ctx):
    global games_list
    i = check_user(ctx.author.id)
    if i < 0:
        await ctx.send(f"<@{ctx.author.id}> Not in game")
    else:
        vidas = games_list[i].get_attempts()
        await ctx.send(f"<@{ctx.author.id}> has hecho {vidas} intentos")


@bot.command()
async def my_id(cntx):
    await cntx.send(f"El id del usuario <@{cntx.author.id}> es: {cntx.author.id}")


@bot.command(pass_context=True)
async def p(cntx, *args):
    global games_list
    message_text = ""
    icon_message = ""
    index = check_user(cntx.author.id)
    if index >= 0:
        aux = games_list[index]
        for j in range(len(args)):
            if j == 0:
                message_text = args[j]
            else:
                message_text = f"{message_text} {args[j]}"
        # await cntx.send(message_text)
        respuesta_message = ""
        if not aux.check_word(message_text):
            await cntx.send(f"{message_text} --> La posicion de los caracteres y espacios debe coincidir con la de "
                            f"los caracteres de la palabra {aux.get_resp_fin()}")
        else:
            respuesta_message = aux.gess(message_text)

            for i in range(len(respuesta_message)):
                if respuesta_message[i] == "-":
                    icon_message += ":white_large_square:"
                elif respuesta_message[i] == "?":
                    icon_message += ":orange_square:"
                elif respuesta_message[i] == " ":
                    icon_message += " "
                else:
                    icon_message += ":green_square:"

            # await cntx.send(respuesta_message)

        text = (f"<@{cntx.author.id}>\nIntento: {aux.get_attempts()}\n")

        if aux.is_finished(message_text):
            await cntx.send(f"{text}{respuesta_message}\n{icon_message}\nCORRECTO! Has ganado!")
            del games_list[index]
        else:
            await cntx.send(text + respuesta_message + "\n" + icon_message)
    else:
        await cntx.send("Not in game")


'''
@bot.command()
async def players(ctx):
    if len(games_list) == 0:
        await ctx.send("0 Players")
    for i in range(len(games_list)):
        await ctx.send(f"<@{games_list[i].get_user_id()}> esta jugando")
'''


@bot.command()
async def end(ctx):
    global games_list
    i = check_user(ctx.author.id)
    if i < 0:
        await ctx.send("Not in game")
    else:

        await ctx.send(
            f"<@{games_list[i].get_user_id()}>\nBuen intento, tu personaje era: {games_list[i].get_personaje()}")
        del games_list[i]


@bot.command()
async def clear(ctx, amount=100):
    if ctx.author.id == 200636184110694400:
        await ctx.channel.purge(limit=amount)
    else:
        await ctx.channel.purge(limit=1)


@bot.command()
async def adios(ctx, amount=1000):
    if ctx.author.id == 200636184110694400:
        await ctx.channel.purge(limit=1)
        await ctx.send("Gracias por jugar con Paimon!! Es hora de irse, nos veremos otra vez para jugar mas juegos "
                       "\n Hasta la proxima!!")
        time.sleep(10)
        await ctx.channel.purge(limit=amount)
        time.sleep(2)
        sys.exit()


bot.run(BOT_TOKEN)
