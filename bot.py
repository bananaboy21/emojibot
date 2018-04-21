import discord
import os
import io
import traceback
import sys
import time
import datetime
import asyncio
import random
import aiohttp
import random
import textwrap
import inspect
from contextlib import redirect_stdout
from discord.ext import commands
import json
bot = commands.Bot(command_prefix=commands.when_mentioned_or('e/'),description="TheEmperor™'s Discord bot.\n\nHelp Commands",owner_id=250674147980607488)



@bot.event
async def on_ready():
    print('Bot is online, and ready to ROLL!')
    while True:
        await bot.change_presence(activity=discord.Game(name=f"with emojis."))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game(name=f"on discord."))
        await asyncio.sleep(10)

bot._last_result = None

startup_extensions = [

    
    'cogs.utility'	
	
]


startTime = time.time()
        
        
@bot.command()
async def ping(ctx):
    """Get the bot's Websocket latency."""
    color = discord.Color(value=0x18a8cc)
    em = discord.Embed(color=color, title='Pong! Websocket Latency:')
    em.description = f"{bot.latency * 1000:.4f} ms"
    await ctx.send(embed=em)
    
    
    
if not os.environ.get('TOKEN'):
   print("no token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('"'))
