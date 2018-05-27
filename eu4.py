import discord
from discord.ext import commands
from util import *
from random import *

dow_sentences = ["May God have mercy on us all.",
                 "May this war hopefully end before Christmas.",
                 "One can hope that this war shall not cause further conflict.",
                 "The global community hopes that this war shall resolve any current tensions."]

paradox_games = {"Europa Universalis 4": "Emperor",
                 "Victoria 2": "President",
                 "Stellaris": "Space Emperor",
                 "Hearts of Iron IV": "Chancellor",
                 "Crusader Kings 2": "Duke"}

class Eu4():

    def __init__(self, bot):
        self.bot = bot

    # Declares war on the target
    @commands.command(pass_context=True)
    async def DOW(self, ctx, target: discord.Member = None):
        user = ctx.message.author
        user_name = get_name(user)
        target_name = get_name(target)
        if target is None:
            content =  "{0} has declared war on...someone.".format(user_name)
        elif target == user:
            content = "{0 has declared war on themself.\nWhat an idiot.".format(user_name)
        else:
            sentence = sample(dow_sentences, 1)
            content = "{0} has declared war on {1}!\n{2}".format(user_name, target_name, sentence[0])
        await self.bot.say(content)

    # Insults the target
    @commands.command(pass_context=True)
    async def insult(self, ctx, target: discord.Member = None):
        user = ctx.message.author
        user_name = get_name(user)
        if target is None:
            content = ("Erm...whom shall you insult?")
        elif target == user:
            content = ("{0} has sent a diplomatic insult to...themself.  What a fool.".format(user_name))
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
            content = "{0} has sent a diplomatic insult to {1}! {0}'s {2} appears to be astounded by the profane " \
                   "actions of {1}'s {3}!".format(user_name, target_name, u_leader, t_leader)
        await self.bot.say(content)

    # Sends a gift to the target
    @commands.command(pass_context=True)
    async def gift(self, ctx, target: discord.Member = None, ducats: str = None):
        user = ctx.message.author
        if target is None:
            content =  "You can't just give your buckets of ducats away like that!"
        elif target == user:
            content =  "That is quite literally impossible"
        else:
            if ducats is None or is_int(ducats) == False: ducats = "500"
            user_name = get_name(user)
            target_name = get_name(target)
            content = "{0} has just given {1} ducat(s) to {2}!\nWhat a nice guy!".format(user_name, ducats, target_name)
        await self.bot.say(content)

def setup(bot):
    bot.add_cog(Eu4(bot))