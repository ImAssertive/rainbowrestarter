import discord, asyncio, checks, useful
from discord.ext import commands

class mainCog:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    @checks.whitelisted()
    async def verify(self, ctx, user):
        userid = useful.getid(user)
        if ctx.author.id == 265953808381640704:
            await ctx.author.send('```**Welcome, ' + ctx.guild.get_member(userid).mention + '!**\n• Please make sure to read <#441971134217322506>\n• To set your profile tags, send @SamBot#5904 a DM with the command *`!info`*\n• Introduce yourself on <#348800438176317441> if you wish\n• Check out our opt-in channels with the command *`?ranks`* on <#348776263986446336>\nPlease enjoy your time with us :tophat:```')
        else:
            await ctx.author.send('```**Welcome, '+ctx.guild.get_member(userid).mention+'!**\n• Please make sure to read <#441971134217322506>\n• To set your profile tags, send @SamBot#5904 a DM with the command *`!info`*\n• Introduce yourself on <#348800438176317441> if you wish\n• Check out our opt-in channels with the command *`?ranks`* on <#348776263986446336>```')
        await ctx.author.send("<#331517548636143626> <#331517548636143626> <#331517548636143626> <#331517548636143626> <#331517548636143626> <#331517548636143626> ")

    @commands.command(hidden=True, name="togglenotif", aliases=['shutup'])
    @checks.justme()
    async def togglenotif(self, ctx):
        ctx.bot.welcomeNotif = not ctx.bot.welcomeNotif
        if ctx.bot.welcomeNotif:
            await ctx.channel.send(":white_check_mark: | Enabled welcome spam.")
        else:
            await ctx.channel.send(":white_check_mark: | Disabled welcome spam.")

    @commands.command(hidden=True)
    async def whois(self, ctx, *, idString):
        idOutput = ""
        idListMentions = []
        idList = idMentions.split(", ")
        for counter in range(0,len(idList)):
            idListMentions[counter] = "<@"+str(idList[counter])+">"
            idList[counter] = str(idList[counter])
            idOutput = idOutput + "\n" + idList[counter] + " is: " + idListMentions[counter]
        await ctx.channel.send(idOutput)


    async def on_member_join(self, ctx):
        if ctx.guild.id == 331517548636143626 and ctx.bot.welcomeNotif:
            await ctx.guild.get_member(163691476788838401).send('```**Welcome, '+ctx.mention+'!**\n• Please make sure to read <#441971134217322506>\n• To set your profile tags, send @SamBot#5904 a DM with the command *`!info`*\n• Introduce yourself on <#348800438176317441> if you wish\n• Check out our opt-in channels with the command *`?ranks`* on <#348776263986446336>```')
            for counter in range(0,4):
                await ctx.guild.get_member(163691476788838401).send("NEW MEMBER <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960>")


def setup(bot):
    bot.add_cog(mainCog(bot))