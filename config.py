import configparser
from pathlib import Path
from discord.ext import commands

config = configparser.ConfigParser()
config_file = Path("config.ini")


def setup():
    try:
        config.read("config.ini")
        prefix = config["setup"]["command_prefix"]
        return commands.Bot(command_prefix=prefix)
    except Exception:
        config['setup'] = {"token": "none",
                       "command_prefix": "?", "presence": "with your minds"}
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
        print("Failed to locate config.ini. Generating new file.")
        raise SystemExit


def get_token():
    try:
        return config.get("setup", "token")
    except Exception:
        print("Failed to retrieve proper token.  Aborting.")
        raise SystemExit


def get_presence():
    try:
        return config.get("setup", "presence")
    except Exception:
        print("Failed to retrieve presence.  Aborting.")