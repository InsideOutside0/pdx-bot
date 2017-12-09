import discord
from discord.ext import commands
from discord.ext.commands import Bot
from random import *

bot = commands.Bot(command_prefix='?')

dow_sentences = ["May God have mercy on us all.",
                 "May this war hopefully end before Christmas.",
                 "One can hope that this war shall not cause further conflict.",
                 "The global community hopes that this war shall resolve any current tensions."]

def get_name(user: discord.User):
    if (user.nick):
        return user.nick
    else:
        return user.name

@bot.event
async def on_ready():
    print ("PDX Bot starting")
    print ("ID: " + bot.user.id)

# @bot.command(pass_context=True)
# async def pyr(ctx, arg=None):
#     if arg is None:
#         arg="a"
#     if len(arg)>1:
#         arg += " "
#     await bot.say(arg)
#     await bot.say(arg + arg)
#     await bot.say(arg + arg + arg)
#     await bot.say(arg + arg)
#     await bot.say(arg)

@bot.command(pass_context=True)
async def DOW(ctx, target: discord.Member=None):
    user=ctx.message.author
    if target is None:
        await bot.say(get_name(user) + " has declared war on...someone.")
    elif target == user:
        await bot.say(get_name(user) + " has declared war on themself.  What an idiot.")
    else:
        sentence = sample(dow_sentences, 1)
        await bot.say(get_name(user) + " has declared war on " + get_name(target) + "!  " + sentence[0])

@bot.command(pass_context=True)
async def Insult(ctx, target: discord.Member=None):
    user=ctx.message.author
    if target is None:
        await bot.say("Erm...whom shall you insult?")
    elif target==user:
        await bot.say(get_name(user) + " has sent a diplomatic insult to...themself.  What a fool.")
    else:
        await bot.say(get_name(user) + " has sent a diplomatic insult to " + get_name(target) + "!")


bot.run("Mzg4NTMwMTc2MDY3MTA4ODY0.DQuZGw.gRTRDpXSCspIu78QGv5lAscXr3U")