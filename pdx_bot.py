from util import *
from spam import *
from eu4 import *
from general import General
from config import *

from pymongo import MongoClient
import mongo

bot = setup()

# Startup events
@bot.event
async def on_ready():
    print ("PDX Bot starting")
    print ("ID: " + bot.user.id)
    await bot.change_presence(game=discord.Game(name='with your minds'))

# Spams a pyramid of desired size
@bot.command(pass_context=False)
async def pyr(arg=None, cent=None):
    await bot.say(Pyr(arg, cent))

# Says "FUCK" a select number of times
@bot.command(pass_context=False)
async def fuck(num=None):
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

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member = None):
    if user is None: user = ctx.message.author
    await bot.say(Info(user))

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

@bot.command(pass_context=False)
async def test():
    await bot.say(Test())

token = get_token()
bot.run(token)