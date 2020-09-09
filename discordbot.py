#!/usr/bin/env python3
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
    
