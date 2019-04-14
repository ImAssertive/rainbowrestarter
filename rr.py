import discord, asyncio, sys, traceback, checks
from discord.ext import commands

initial_extensions = ['restarter', 'main']

def getPrefix(bot, message):
    prefixes = ["rr!","r!","!"]
    return commands.when_mentioned_or(*prefixes)(bot, message)

def gettoken():
    tokenfile = open("token.txt", "r")
    tokenstring = tokenfile.read()
    tokentoken = tokenstring.split("\n")
    token = str(tokentoken[0])
    return token
token = gettoken()


bot = commands.Bot(command_prefix=getPrefix, pm_help=False, description="Restarter bot for Assertive's bots!")
bot.remove_command("help")

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print('Failed to load extension ' + extension, file=sys.stderr)
            traceback.print_exc()
token = gettoken()


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    game = discord.Game("chess with Traa-tan!")
    await bot.change_presence(status=discord.Status.online, activity=game)



bot.run(token)
