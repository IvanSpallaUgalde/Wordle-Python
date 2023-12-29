import discord
from discord.ext import commands

from WordleGame import WordleGame

f = open("token.txt", "r")
BOT_TOKEN = f.read()
CHANNEL_ID = 1180127744567279727

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

games_list = []

help_msg = ("Para jugar conmigo tendras a tu disposicion los siguientes comandos: \n!help -> Muestra los comandos disponibles del bot \n!play -> Inicia una partida"
            "\n!endgame -> Termina una partida forzosamente \n!vidas -> Te muestra tus intentos restantes \n!guia -> Muestra una guia de como jugar al juego"
            "\n!answer -> Comando utilizado para dar una respuesta")

@bot.event
async def on_ready():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Hola! Soy un bot preparado para jugar al ahoracado con personajes de Genshin impcat!")
    '''
    await channel.send(help_msg)
    await channel.send(":warning: Es importante saber lo siguiente antes de jugar :warning:")
    await channel.send("***Como los personajes de Genshin Impact tienen nombres de diferentes longitudes, la cantidad de cuadrados que salen corresponde al numero de letras del personaje que hay que adivinar***")

    await channel.send(":green_square: :point_left: Este cuadrado verde representa que la letra en esta posicion de tu respuesta es correcta")
    await channel.send(":orange_square: :point_left: Este cuadrado naranja representa que la letra en esta posicion de tu respuesta esta en la respuesta correcta pero en una posicion diferente")
    await channel.send(":white_large_square: :point_left: Este cuadrado blanco representa que la letra en esta posicion de tu respuesta es no esta en la respuesta correcta, o que en esta posicion no has puesto ninguna letra")
    '''

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

@bot.command()
async def ayuda(ctx):
    await ctx.send(help_msg)

@bot.command()
async def initGame(ctx):
    global GAME_INSTANCE
    GAME_INSTANCE = WordleGame()
    await ctx.send(f"Juego iniciado con  vidas")

@bot.command()
async def personaje(ctx):
    global GAME_INSTANCE
    if GAME_INSTANCE == None:
        await ctx.send("No existe una partida")
    else:
        await ctx.send(f"El pesonaje de esta partida es: {GAME_INSTANCE.get_personaje()}")

@bot.command()
async def vidas(ctx):
    global GAME_INSTANCE
    if GAME_INSTANCE == None:
        await ctx.send("No existe una partida")
    else:
        await ctx.send(f"Te quedan {str(GAME_INSTANCE.get_vidas)} vidas")


bot.run(BOT_TOKEN)