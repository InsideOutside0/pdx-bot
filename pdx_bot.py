import discord
from discord.ext import commands
from discord.ext.commands import Bot
from random import *
from util import *
from spam import *
from eu4 import *
from general import General


from pymongo import MongoClient
import mongo

# client = MongoClient(port=27017)

bot = commands.Bot(command_prefix='?')
client = discord.Client()

# Startup events
@bot.event
async def on_ready():
    print ("PDX Bot starting")
    print ("ID: " + bot.user.id)
    await bot.change_presence(game=discord.Game(name='with your minds'))

# Spams a pyramid of desired size
@bot.command(pass_context=True)
async def pyr(ctx, arg=None, cent=None):
    await bot.say(Pyr(arg, cent))

# Says "FUCK" a select number of times
@bot.command(pass_context=True)
async def fuck(ctx, num=None):
    await bot.say(Fuck(num))

# Declares war on the target
@bot.command(pass_context=True)
async def DOW(ctx, target: discord.Member=None):
    user = ctx.message.author
    await bot.say(DoW(user, target))

# Insults the target
@bot.command(pass_context=True)
async def insult(ctx, target: discord.Member=None):
    user=ctx.message.author
    await bot.say(Insult(user, target))

# Returns the roles of the user or target
@bot.command(pass_context=True)
async def roles(ctx, user: discord.Member=None):
    if user is None: user=ctx.message.author
    await bot.say(Roles(user))

# Sends a gift to the target
@bot.command(pass_context=True)
async def gift(ctx, target: discord.Member=None, ducats: str=None):
    user=ctx.message.author
    await bot.say(Gift(user, target, ducats))

# Battles the target
@bot.command(pass_context=True)
async def battle(ctx, target: discord.Member=None):
    user=ctx.message.author
    await bot.say(General.battle(user, target))


bot.run("Mzg4NTMwMTc2MDY3MTA4ODY0.DQuZGw.gRTRDpXSCspIu78QGv5lAscXr3U")