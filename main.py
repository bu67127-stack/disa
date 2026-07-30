import discord
from discord.ext import commands


loadbot = os.getenv("discordbotrun")

intents = discord.Intents.all()
bot = discord.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print("Bot ReOnline")
    await client.change_presence(activity=discord.Game(name="서버 보호중 ($설명서)"))

bot.command(aliases="설명서")
async def help()


bot.run(loadbot)
