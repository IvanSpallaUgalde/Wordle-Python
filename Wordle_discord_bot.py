import discord
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

help_msg = ("Para jugar conmigo tendras a tu disposicion los siguientes comandos: \n!help -> Muestra los comandos "
            "disponibles del bot \n!play -> Inicia una partida \n!endgame -> Termina una partida forzosamente "
            "\n!vidas -> Te muestra tus intentos restantes \n!guia -> Muestra una guia de como jugar al juego "
            "\n!answer -> Comando utilizado para dar una respuesta")

@bot.event
async def on_ready():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Hola! Soy un bot preparado para jugar al ahoracado con personajes de Genshin impcat!")
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
async def hello(ctx):
    await ctx.send("Hello!")

@bot.command()
async def ayuda(ctx):
    await ctx.send(help_msg)

@bot.command()
async def init_game(ctx):
    global games_list
    i = check_user(ctx.author.id)
    if i < 0:
        aux = BotGame(ctx.author.id)
        games_list.append(aux)
        await ctx.send(f"Juego de <@{aux.get_user_id()}> iniciado")
    else:
        await ctx.send(f"<@{ctx.author.id}> ya estas en partida")

@bot.command()
async def personaje(ctx):
    global games_list
    i = check_user(ctx.author.id)
    if i < 0:
        await ctx.send("Not in game")
    else:
        personaje = games_list[i].get_personaje()
        await ctx.send(f"Tu personaje es: {personaje}")

@bot.command()
async def vidas(ctx):
    global games_list
    i = check_user(ctx.author.id)
    if i < 0:
        await ctx.send("Not in game")
    else:
        vidas = games_list[i].get_attempts()
        await ctx.send(f"Te quedan {vidas} vidas")

@bot.command()
async def my_id(cntx):
    await cntx.send(f"El id del usuario <@{cntx.author.id}> es: {cntx.author.id}")

@bot.command(pass_context=True)
async def p(cntx, *args):
    global games_list
    message_text = ""
    i = check_user(cntx.author.id)
    if i >= 0:
        aux = games_list[i]
        for j in range(len(args)):
            if j == 0:
                message_text = args[j]
            else:
                message_text = f"{message_text} {args[j]}"
        await cntx.send(message_text)
        respuesta = aux.gess(message_text)
        await cntx.send(respuesta)
        await cntx.send(len(args))
        respuesta_message = ""
        for m in range(len(respuesta)):
            if respuesta[m] == "-":
                respuesta_message = respuesta_message + ":white_large_square:"
            elif respuesta[m] == "?":
                respuesta_message = respuesta_message + ":orange_square:"
            elif respuesta[m] == "_":
                respuesta_message = respuesta_message + " "
            else:
                respuesta_message = respuesta_message + ":green_square:"


        text = (f"<@{cntx.author.id}>\nIntento: {aux.get_attempts()}\n")

        if aux.is_finished():
            del games_list[i]
            await cntx.send(f"{text}{respuesta_message}\nCORRECTO! Juego finalizado")
        else:
            await cntx.send(text+respuesta_message)

    else:
        await cntx.send("Not in game")

@bot.command(pass_context=True)
async def test(cntx, *args):
    message_text = ""
    for i in range(len(args)):
        message_text = message_text + args[i] + " "

    message_text[-1] = ""
    await cntx.send(message_text)

@bot.command()
async def players(ctx):
    if len(games_list) == 0:
        await ctx.send("0 Players")
    for i in range(len(games_list)):
        await ctx.send(f"<@{games_list[i].get_user_id()}> esta jugando")

@bot.command()
async def end_game(ctx):
    global games_list
    i = check_user(ctx.author.id)
    if i < 0:
        await ctx.send("Not in game")
    else:
        del games_list[i]

@bot.command(pass_context=True)
async def args_test(cntx, *args):
    await cntx.send(len(args))
    mensaje = ""
    for i in range(len(args)):
        mensaje =f"{mensaje} args[{i}]: {args[i]} \n"
    await cntx.send(mensaje)

bot.run(BOT_TOKEN)
