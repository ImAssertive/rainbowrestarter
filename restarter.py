import discord, asyncio, checks, useful, os, subprocess, random
from discord.ext import commands

class restarter:
    def __init__(self, bot):
        self.bot = bot
        self.bot.currentColour = -1

    @commands.command(hidden=True)
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
    @checks.process_running()
    async def updatetraa(self, ctx, branch = None):
        if branch:
            shellcommand = "cd .. && cd traatan && git pull origin " + str(branch)
        else:
            shellcommand = "cd .. && cd traatan && git pull"
        desc="Updating traatan!"
        self.p = subprocess.Popen(shellcommand, shell=True)
        embed = discord.Embed(colour=useful.getcolour(ctx), title=desc)
        await ctx.channel.send(embed=embed)


    @commands.command(name="launchtraa", aliases=['start','starttraa'])
    @checks.has_role("Admin")
    @checks.process_running()
    async def launchtraa(self, ctx):
        shellcommand="cd .. && cd traatan && python3 traatan.py"
        desc="Launching traatan!"
        self.p = subprocess.Popen(shellcommand, shell=True)
        embed = discord.Embed(colour=useful.getcolour(ctx), title=desc)
        await ctx.channel.send(embed=embed)

    @commands.command()
    @checks.has_role("Admin")
    async def killtraa(self, ctx):
        #subprocess.Popen.kill(self)
        embed = discord.Embed(colour=useful.getcolour(ctx), title="Killing traatan...", description="You monster...")
        await ctx.channel.send(embed=embed)
        print(ctx.author.display_name + " killed Traa tan.")
        shh = await ctx.channel.send("traa!quit")
        await shh.delete()

    @commands.command(name = "exit", aliases =['quit'], hidden = True)
    @checks.justme()
    @checks.process_running()
    async def exit(self, ctx):
        thanos = random.randint(1,5)
        if thanos == 1:
            await ctx.channel.send("Mrs Assertive I dont feel so good...")
        if thanos == 2:
            await ctx.channel.send("Why...")
        if thanos == 3:
            await ctx.channel.send(":wave: Goodbye.")
        if thanos == 4:
            await ctx.channel.send("The machine... stops")
        if thanos == 5:
            await ctx.channel.send("The horror. The horror.")
        sys.exit()



    async def shellfunction(self, shellcommand):
        self.p = subprocess.Popen(shellcommand, shell=True)


def setup(bot):
    bot.add_cog(restarter(bot))