import discord
from discord.ext import commands
from discord.ext.commands import Bot
from random import *
from mongoengine import *
import db

# connect('pdxbot_db', host='localhost', port=27017)
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

members = client.get_all_members()

def get_name(user: discord.Member):
    if (user.nick):
        return user.nick
    else:
        return user.name

@bot.event
async def on_ready():
    print ("PDX Bot starting")
    print ("ID: " + bot.user.id)
    # for member in members:
    #     user = db.User(
    #         name=member.name,
    #         id=member.id,
    #         wars=[],
    #         soldiers=0,
    #     )
    #     user.save()

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
    user_name=get_name(user)
    target_name=get_name(target)
    if target is None:
        await bot.say("{0} has declared war on...someone.".format(user_name))
    elif target == user:
        await bot.say("{0 has declared war on themself.  What an idiot.".format(user_name))
    else:
        sentence = sample(dow_sentences, 1)
        await bot.say("{0} has declared war on {1}!  {2}".format(user_name, target_name, sentence))

@bot.command(pass_context=True)
async def Insult(ctx, target: discord.Member=None):
    user=ctx.message.author
    if target is None:
        await bot.say("Erm...whom shall you insult?")
    elif target==user:
        user_name = get_name(user)
        await bot.say("{0} has sent a diplomatic insult to...themself.  What a fool.".format(user_name))
    else:
        u_leader = None
        t_leader = None
        for game in paradox_games:
            if user.game is not None:
                if user.game.name == game:
                    u_leader = paradox_games[game]
            if target.game is not None:
                if target.game.name == game:
                    t_leader = paradox_games[game]
        if u_leader is None:
            u_leader = "King"
        if t_leader is None:
            t_leader = "King"
        user_name = get_name(user)
        target_name = get_name(target)
        await bot.say("{0} has sent a diplomatic insult to {1}! {0}'s {2} appears to be astounded by the profane "
                      "actions of {1}'s {3}!".format(user_name, target_name, u_leader, t_leader))


bot.run("Mzg4NTMwMTc2MDY3MTA4ODY0.DQuZGw.gRTRDpXSCspIu78QGv5lAscXr3U")