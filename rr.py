import discord, asyncio, sys, traceback, checks
from discord.ext import commands

initial_extensions = ['restarter', 'verify']

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

def run(token):
    bot = commands.Bot(command_prefix=getPrefix, pm_help=False, description="Restarter bot for Assertive's bots!")

    if __name__ == '__main__':
        for extension in initial_extensions:
            try:
                bot.load_extension(extension)
            except Exception as e:
                print('Failed to load extension ' + extension, file=sys.stderr)
                traceback.print_exc()

    bot.run(token)

class Bot(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(
            description=kwargs.pop("description"),
            command_prefix=getPrefix
        )
        self.currentColour = -1

    async def on_ready(self):
        print("Username: {0}\nID: {0.id}".format(self.user))
        game = discord.Game("chess with Traa tan.")
        await self.change_presence(status=discord.Status.online, activity=game)

    def getcolour(self):
        colours = ["5C6BC0", "AB47BC", "EF5350", "FFA726", "FFEE58", "66BB6A", "5BCEFA", "F5A9B8", "FFFFFF", "F5A9B8", "5BCEFA"]
        self.currentColour += 1
        if self.currentColour ==  len(colours) - 1:
            self.currentColour = 0
        return discord.Colour(int(colours[self.currentColour], 16))


@bot.event

run(token)