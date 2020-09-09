import discord
import sys
import io
from discord.ext import commands
import cgi
token = "
bot = commands.Bot(prefix="/")

@bot.event
async def on_ready():
    print("ready")
    


