import configparser
from pathlib import Path
from discord.ext import commands
import discord

config = configparser.ConfigParser()
config_file = Path("config.ini")

def setup():
    config['setup'] = {"token": "none",
                       "command_prefix": "?"}
    if config_file.is_file() == False:
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
    config.read("config.ini")
    prefix = config["setup"]["command_prefix"]
    bot = commands.Bot(command_prefix=prefix)
    return bot

def get_token():
    if config_file.is_file:
        token = config['setup']['token']
        return token