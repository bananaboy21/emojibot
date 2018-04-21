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
import urllib.parse





class Utility:
    def __init__(self, bot):
       self.bot = bot
       self.session = self.bot.session
       
       
       
       
    @commands.command()
    async def searchemoji(self, ctx, *, emoji):
        """Searches an emoji from the bot's servers."""
        await ctx.message.delete()
        e = discord.utils.get(self.bot.emojis, name=emoji)
        if e is None:
            return await ctx.send("No emoji found from the list of my servers.\nThe bot cannot search YOUR servers, only the servers that it is currently in.")
        resp = await self.session.get(f"https://cdn.discordapp.com/emojis/{e.id}") 
        resp = await resp.read()
        if e.animated:
            extension = '.gif'
        else:
            extension = '.png'
        await ctx.send(file=discord.File(resp, f"{e.name}{extension}"))
        
        
    @commands.command(aliases=['copyemoji', 'emojiadd', 'eadd'])
    @commands.has_permissions(manage_emojis = True)
    async def addemoji(self, ctx, *, emoji):
        """Adds an emoji by the emoji's name."""
        e = discord.utils.get(self.bot.emojis, name=emoji)
        if e is None:
            await ctx.send("No emoji found from the list of my servers.\nYou can reply with an emoji ID, and the bot will add it for you. Otherwise, reply 'cancel' to end the search.")
            try:
                x = await self.bot.wait_for("message", check=lambda x: x.channel == ctx.channel and x.author == ctx.author, timeout=45.0)
            except asyncio.TimeoutError:
                return await ctx.send("The request timed out. Please try again.")
            if x.content.lower() == 'cancel':
                return await ctx.send("The process has ended.")
            if self.bot.get_emoji(int(x.content)) is None:
                return await ctx.send("Sorry, no emoji with that ID is found.")
            e = self.bot.get_emoji(int(x.content)) 
        count = 0
        animate = 0
        for x in ctx.guild.emojis:
            if not e.animated:
                if not x.animated:
                    count += 1
                else:
                    animate += 1
        if count >= 50 or animate >= 50:
            return await ctx.send(f"This server has reached the limit for custom emojis! {self.bot.get_emoji(430853757350445077)}")
        resp = await self.session.get(f"https://cdn.discordapp.com/emojis/{e.id}")
        img = await resp.read()
        try:
            em = discord.Embed(color=discord.Color(value=0x00ff00), title=f"The emoji has been created in the server! Name: {e.name}")
            await ctx.guild.create_custom_emoji(name=e.name, image=img)
            em.set_image(url=f"https://cdn.discordapp.com/emojis/{e.id}")
            await ctx.send(embed=em)
        except discord.Forbidden:
            return await ctx.send("The bot does not have Manage Emojis permission.")

def setup(bot): 
    bot.add_cog(Utility(bot))
