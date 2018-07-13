import discord, asyncio, checks, useful
from discord.ext import commands

class verify:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.whitelisted()
    async def verify(self, ctx, user):
        userid = useful.getid(user)
        await ctx.author.send('``**Welcome, '+ctx.guild.get_member(userid).mention+'!**\n• Please make sure to read <#441971134217322506>\n• To set your profile tags, send @SamBot#5904 a DM with the command *`!info`*\n• Introduce yourself on <#348800438176317441> if you wish\n• Check out our opt-in channels with the command *`?ranks`* on <#348776263986446336>``')

    @commands.command

    async def on_member_join(ctx):
        if ctx.guild.id == 331517548636143626:
            await ctx.guild.get_member(163691476788838401).send('``**Welcome, '+ctx.mention+'!**\n• Please make sure to read <#441971134217322506>\n• To set your profile tags, send @SamBot#5904 a DM with the command *`!info`*\n• Introduce yourself on <#348800438176317441> if you wish\n• Check out our opt-in channels with the command *`?ranks`* on <#348776263986446336>``')
            for counter in range(0,4):
                await ctx.guild.get_member(163691476788838401).send("NEW MEMBER <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960> <#448388368129064960>")


def setup(bot):
    bot.add_cog(verify(bot))