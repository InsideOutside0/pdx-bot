import config
import discord
import os.path
import db

# Initializing the bot from the config file
bot = config.setup()

# This is which files the commands are house in
startup_extensions = ["eu4", "war", "spam", "util"]


@bot.event  # Startup events
async def on_ready():
    print("PDX Bot starting")
    print("ID: " + bot.user.id)
    await bot.change_presence(game=discord.Game(name=config.get_presence()))

if __name__ == "__main__":
    # load extensions or yield an error for why they couldn't be loaded
    for extension in startup_extensions:
        try: bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
    if not os.path.isfile("database.db"): db.create_db()
    # retrieve the token and launch the bot
    token = config.get_token()
    try: bot.run(token)
    except Exception:
        print("Failed to send proper token. Aborting.")
        raise SystemExit

