import discord
from discord.ext import commands

def has_role(*arg):
    async def predicate(ctx):
        if ctx.author.id == 163691476788838401:
            return True
        else:
            for counter in range (0,len(arg)):
                if discord.utils.get(ctx.guild.roles, name=str(arg[counter])) in ctx.author.roles:
                    return True
            return False
    return commands.check(predicate)

def justme():
    async def predicate(ctx):
        if ctx.author.id == 163691476788838401:
            return True
        else:
            return False
    return commands.check(predicate)

def whitelisted():
    async def predicate(ctx):
        whitelistedmembers = [163691476788838401, 180523952114761728, 95575367317716992, 173498062260404225, 186081930972889088, 265953808381640704, 174982651759820800, 201731484363522048, 439291697634213888, 251334957954236416, 308302478657454095, 119035880575991808, 132919539766788096, 133884121830129664, 189774158853308417, 360118518533980172, 201370772109787136, 529323232105594880, 282148355944087552]
        if ctx.author.id in whitelistedmembers:
            return True
        else:
            return False
    return commands.check(predicate)

def process_running():
    async def predicate(ctx):
        if ctx.bot.cogs['restarter'].p.poll() != None:
            return True
        else:
            return False
    return commands.check(predicate)
