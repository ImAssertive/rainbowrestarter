import discord, asyncio, checks, useful, sys
from discord.ext import commands

class mainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    @checks.has_role("Verification Notification")
    async def verify(self, ctx, user):
        userid = useful.getid(user)
        await ctx.author.send('```**Welcome, '+ctx.guild.get_member(userid).mention+
                              '!**\n• Please make sure to read #info'+
                              '\n• To set your profile tags, send <@770758387859456060> a DM with the command *`!info`*'+
                              '\n• Introduce yourself on #bio if you wish' +
                              '\n• Check out our opt-in channels with the command *`w!ranks`* on #bot!'+
                              '\n:42a:```')
        await ctx.author.send("<#331517548636143626> <#331517548636143626> <#331517548636143626> <#331517548636143626> <#331517548636143626> <#331517548636143626> ")

    @commands.command(hidden=True)
    async def whois(self, ctx, *, idString):
        idOutput = ""
        idListMentions = []
        idList = idString.split(", ")
        for counter in range(0,len(idList)):
            idListMentions.append("wew")
            idListMentions[counter] = "<@"+str(idList[counter])+">"
            idList[counter] = str(idList[counter])
            idOutput = idOutput + "\n" + idList[counter] + " is: " + idListMentions[counter]
        await ctx.channel.send(idOutput)


    async def on_member_join(self, ctx):
        if ctx.guild.id == 331517548636143626:
            await ctx.guild.get_member(163691476788838401).send('```**Welcome, '+ctx.mention+'!**\n• Please make sure to read <#441971134217322506>\n• To set your profile tags, send @SamBot#5904 a DM with the command *`!info`*\n• Introduce yourself in <#348800438176317441> if you wish\n• Check out our opt-in channels with the command *`w!ranks`* in <#348776263986446336>```')
            for counter in range(0,4):
                await ctx.guild.get_member(163691476788838401).send("NEW MEMBER <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960>")


def setup(bot):
    bot.add_cog(mainCog(bot))