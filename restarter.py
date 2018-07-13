import discord, asyncio, checks, useful, os, subprocess
from discord.ext import commands

class restarter:
    def __init__(self, bot):
        self.bot = bot
        self.bot.currentColour = -1

    @commands.command()
    @checks.justme()
    async def eval(ctx, *, toeval):
        response = (eval(toeval))
        if response != "":
            embed = discord.Embed(colour=useful.getcolour(ctx), title=response)
        else:
            embed = discord.Embed(colour=useful.getcolour(ctx), title="Returned without response")
        await ctx.channel.send(embed=embed)


    @commands.command()
    @checks.justme()
    async def updatetraa(self, ctx):
        shellcommand = "cd .. && cd traatan && git pull && cd .. traatan && python3 traatan.py"
        desc="Updated and restarted traatan!"
        await self.shellfunction(ctx, shellcommand, desc)

    @commands.command(name="launchtraa", aliases=['start','starttraa'])
    @checks.has_role("Admin")
    async def launchtraa(self, ctx):
        shellcommand="cd .. && cd traatan && python3 traatan.py"
        desc="Launching traatan!"
        await self.shellfunction(ctx, shellcommand,desc)

    @commands.command()
    @checks.has_role("Admin")
    async def killtraa(self, ctx):
        subprocess.Popen.kill(self)
        embed = discord.Embed(colour=useful.getcolour(ctx), title="Killing traatan...", description="You monster...")
        await ctx.channel.send(embed=embed)


    async def shellfunction(self, ctx, shellcommand, desc):
        subprocess.Popen(shellcommand, shell=True)
        embed = discord.Embed(colour=useful.getcolour(ctx), title=desc)
        await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(restarter(bot))