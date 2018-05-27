from util import *
from spam import *
from eu4 import *
from war import General
from config import *

# Initializing the bot from the config file
bot = setup()

# This is which files the commands are house in
startup_extensions = ["eu4", "war", "spam", "util"]

# Startup events
@bot.event
async def on_ready():
    print("PDX Bot starting")
    print("ID: " + bot.user.id)
    await bot.change_presence(game=discord.Game(name='with your minds'))

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
    token = get_token()
    print(token)
    bot.run(token)
