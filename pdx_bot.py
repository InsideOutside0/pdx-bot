import discord
from discord.ext import commands
from discord.ext.commands import Bot
from random import *
from util import *

from pymongo import MongoClient
import mongo

from general import General
# client = MongoClient(port=27017)

bot = commands.Bot(command_prefix='?')
client = discord.Client()

dow_sentences = ["May God have mercy on us all.",
                 "May this war hopefully end before Christmas.",
                 "One can hope that this war shall not cause further conflict.",
                 "The global community hopes that this war shall resolve any current tensions."]

paradox_games = {"Europa Universalis 4": "Emperor",
                 "Victoria 2": "President",
                 "Stellaris": "Space Emperor",
                 "Hearts of Iron IV": "Chancellor",
                 "Crusader Kings 2": "Duke"}

def compare(str1, str2):
    print("{0} | {1}".format(str1, str2))

@bot.event
async def on_ready():
    print ("PDX Bot starting")
    print ("ID: " + bot.user.id)
    await bot.change_presence(game=discord.Game(name='with your minds'))


@bot.command(pass_context=True)
async def pyr(ctx, arg=None, cent=None):
    if arg is None: arg="a"
    if len(arg)>1: arg += " "
    arg = arg.replace("_", " ")
    if cent is None: cent=""
    if is_int(cent)==False: center=3
    elif cent is None: center=3
    else: center=int(cent)
    str=""
    for line in range(1,center+2):
        for i in range(1, line):
            str+=arg
        str+="\n"
    for line in range(center, 1, -1):
        for i in range(1, line):
            str+=arg
        str+="\n"
    await bot.say(str)

@bot.command(pass_context=True)
async def fuck(ctx, num=None):
    if num is None: num="5"
    if is_int(num)==False: await bot.say("Fuck you")
    elif int(num) > 0 and int(num)<=50:
        str=""
        num_i=int(num)
        for i in range(1, num_i+1):
            str+="FUCK\n"
        await bot.say(str)
    else: await bot.say("Fuck you")

@bot.command(pass_context=True)
async def DOW(ctx, target: discord.Member=None):
    user=ctx.message.author
    user_name=get_name(user)
    target_name=get_name(target)
    if target is None: await bot.say("{0} has declared war on...someone.".format(user_name))
    elif target == user: await bot.say("{0 has declared war on themself.\nWhat an idiot.".format(user_name))
    else:
        sentence = sample(dow_sentences, 1)
        await bot.say("{0} has declared war on {1}!\n{2}".format(user_name, target_name, sentence[0]))

@bot.command(pass_context=True)
async def insult(ctx, target: discord.Member=None):
    user=ctx.message.author
    user_name = get_name(user)
    if target is None: await bot.say("Erm...whom shall you insult?")
    elif target==user:
        await bot.say("{0} has sent a diplomatic insult to...themself.  What a fool.".format(user_name))
    else:
        u_leader = None
        t_leader = None
        for game in paradox_games:
            if user.game is not None:
                if user.game.name == game: u_leader = paradox_games[game]
            if target.game is not None:
                if target.game.name == game: t_leader = paradox_games[game]
        if u_leader is None: u_leader = "King"
        if t_leader is None: t_leader = "King"
        target_name = get_name(target)
        await bot.say("{0} has sent a diplomatic insult to {1}! {0}'s {2} appears to be astounded by the profane "
                      "actions of {1}'s {3}!".format(user_name, target_name, u_leader, t_leader))

@bot.command(pass_context=True)
async def roles(ctx, user: discord.Member=None):
    if user is None: user=ctx.message.author
    str="The roles of {} are:".format(get_name(user))
    for role in user.roles:
        if role.name != "@everyone": str+=" {},".format(role.name)
    str=str.rstrip(",")
    await bot.say(str)

@bot.command(pass_context=True)
async def gift(ctx, target: discord.Member=None, ducats: str=None):
    user=ctx.message.author
    if target is None: await bot.say("You can't just give your buckets of ducats away like that!")
    elif target==user: await bot.say("That is quite literally impossible")
    else:
        if ducats is None or is_int(ducats)==False: ducats = "500"
        user_name=get_name(user)
        target_name=get_name(target)
        await bot.say("{0} has just given {1} ducat(s) to {2}!\nWhat a nice guy!".format(user_name, ducats, target_name))

@bot.command(pass_context=True)
async def battle(ctx, target: discord.Member=None):
    user=ctx.message.author
    if target is None: await bot.say("Pick a target ya dummy")
    elif target==user: await bot.say("{0} wants to battle themself.\nBoth sides have lost".format(get_name(user)))
    else:
        await bot.say(General.battle(user, target))


bot.run("Mzg4NTMwMTc2MDY3MTA4ODY0.DQuZGw.gRTRDpXSCspIu78QGv5lAscXr3U")