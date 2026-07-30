import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = discord.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print("Bot ReOnline")

bot.run()
