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

def compare(str1, str2):
    print("{0} | {1}".format(str1, str2))

def Roles(user: discord.Member):
    str="The roles of {} are:".format(get_name(user))
    for role in user.roles:
        if role.name != "@everyone": str+=" {},".format(role.name)
    str=str.rstrip(",")
    return str