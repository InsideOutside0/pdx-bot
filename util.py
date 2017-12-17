import discord

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def get_name(user: discord.Member):
    if user.nick: return user.nick
    else: return user.name