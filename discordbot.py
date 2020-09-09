#!/usr/bin/env python3
import sys
sys.path.append('/home/Hyugo/.local/lib/python3.7/site-packages')
print(sys.path)
import discord 
from discord.ext import commands

bot = commands.Bot(prefix='/')
token = ""

async def to_send(id:int,ctn:str):
    try:
        who = bot.get_user(id)
        await who.send(ctn)
    except:
        return 'error'
    else:
        return 'succsess'
    
bot.run(token)
