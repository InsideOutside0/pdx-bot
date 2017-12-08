import discord
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix='?')

def get_name(user: discord.User):
    if (user.nick):
        return user.nick
    else:
        return user.name

@bot.event
async def on_ready():
    print ("PDX Bot starting")
    print ("ID: " + bot.user.id)

@bot.command(pass_context=True)
async def pyr(ctx, arg=None):
    if arg is None:
        arg="a"
    if len(arg)>1:
        arg += " "
    await bot.say(arg)
    await bot.say(arg + arg)
    await bot.say(arg + arg + arg)
    await bot.say(arg + arg)
    await bot.say(arg)

@bot.command(pass_context=True)
async def DOW(ctx, arg: discord.Member=None):
    user=ctx.message.author
    if arg is None:
        await bot.say(get_name(user) + " has declared war on...someone.")
    else:
        await bot.say(get_name(user) + " has declared war on " + get_name(arg))
        await bot.say("May God have mercy on us all.")



bot.run("Mzg4NTMwMTc2MDY3MTA4ODY0.DQuZGw.gRTRDpXSCspIu78QGv5lAscXr3U")