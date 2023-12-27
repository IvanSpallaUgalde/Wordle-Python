import discord
from discord.ext import commands

f = open("token.txt", "r")
BOT_TOKEN = f.read()
CHANNEL_ID = 1180127744567279727

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

prefix = "|"
@bot.event
async def on_ready():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Hola! Soy tu bot de testeo")

@bot.command()
async def say(ctx, *, mg = None):
    await bot.delete_message(ctx.message)

    if not mg: await bot.say("Please specify a message to send")
    else: await bot.say(mg)

bot.run(BOT_TOKEN)