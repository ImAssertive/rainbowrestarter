import discord, asyncio, checks, useful, os, subprocess, random, signal
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
    async def updatetraa(self, ctx, branch = None):
        try:
            os.killpg(os.getpgid(self.p.pid), signal.SIGTERM)
        except:
            print("Killing failed")
        if branch:
            shellcommand = "cd .. && cd traatan && git pull origin " + str(branch)
        else:
            shellcommand = "cd .. && cd traatan && git pull"
        desc="Updating traatan!"
        self.p = subprocess.Popen(shellcommand, stdout=subprocess.PIPE,
                       shell=True, preexec_fn=os.setsid)
        embed = discord.Embed(colour=useful.getcolour(ctx), title=desc)
        await ctx.channel.send(embed=embed)


    @commands.command(name="launchtraa", aliases=['start','starttraa'])
    @checks.has_role("Admin")
    async def launchtraa(self, ctx):
        try:
            os.killpg(os.getpgid(self.p.pid), signal.SIGTERM)
            print("p.kill ran?")
        except:
            print("Killing failed")
        shellcommand="cd .. && cd traatan && python3 traatan.py"
        desc="Launching traatan!"
        self.p = subprocess.Popen(shellcommand, shell=True)
        embed = discord.Embed(colour=useful.getcolour(ctx), title=desc)
        await ctx.channel.send(embed=embed)

    @commands.command()
    @checks.has_role("Admin")
    async def killtraa(self, ctx):
        embed = discord.Embed(colour=useful.getcolour(ctx), title="Killing traatan...", description="You monster...")
        await ctx.channel.send(embed=embed)
        print(ctx.author.display_name + " killed Traa tan.")
        shh = await ctx.channel.send("traa!quit")
        await shh.delete()
        await asyncio.sleep(5)
        try:
            self.p.kill()
        except:
            print("Killing failed")

    @commands.command(name = "exit", aliases =['quit'], hidden = True)
    @checks.justme()
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
        quit()



def setup(bot):
    bot.add_cog(restarter(bot))