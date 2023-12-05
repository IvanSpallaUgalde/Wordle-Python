import discord
from discord.ext import commands

BOT_TOKEN = 'MTE3OTgxNDk5Nzc5OTQ4OTU0Ng.GDlqG-.M-vU4Xw-GxoW5VpK69QeXGXG-YJSdevTvkkIh8'
CHANNEL_ID = 1180127744567279727

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Hello! I'm ready to work!")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Hello! I'm ready to work!")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

bot.run(BOT_TOKEN)