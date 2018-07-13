import discord, asyncio, checks, useful, os, subprocess
from discord.ext import commands

class restarter:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.justme()
    async def eval(ctx, *, toeval):
        response = (eval(toeval))
        if response != "":
            embed = discord.Embed(colour=self.bot.getcolour(), title=response)
        else:
            embed = discord.Embed(colour=self.bot.getcolour(), title="Returned without response")
        statusmessage = ("Python Eval")
        embed.set_thumbnail("https://i.imgur.com/DC65Tix.png")
        await ctx.channel.send(embed=embed)


    @commands.command()
    @checks.justme()
    async def updatetraa(self, ctx):
        shellcommand = "cd .. && cd traatan && git pull && cd .. traatan && python3 traatan.py"
        description="Updated and restarted traatan!"
        await self.shellfunction(ctx, shellcommand)

    @commands.command()
    @checks.has_role("Admin")
    async def launchtraa(self, ctx):
        shellcommand="cd .. && cd traatan && python3 traatan.py"
        description="Launching traatan!"
        await self.shellfunction(ctx, shellcommand)

    @commands.command()
    @checks.has_role("Admin")
    async def killtraa(self, ctx):
        subprocess.Popen.kill()
        embed = discord.Embed(colour=self.bot.getcolour(), title="Killing traatan...", description="You monster...")
        await ctx.channel.send(embed=embed)


    async def shellfunction(self, ctx, shellcommand, description):
        subprocess.Popen(shellcommand, shell=True)
        embed = discord.Embed(colour=self.bot.getcolour(), title=description)
        await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(restarter(bot))