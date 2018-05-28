import discord
from discord.ext import commands


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


dates = {1: "Monday",
         2: "Tuesday",
         3: "Wednesday",
         4: "Thursday",
         5: "Friday",
         6: "Saturday",
         0: "Sunday", }

months = {1: "January",
          2: "February",
          3: "March",
          4: "April",
          5: "May",
          6: "June",
          7: "July",
          8: "August",
          9: "September",
          10: "October",
          11: "November",
          12: "December", }


def get_name(user: discord.Member):
    if user.nick: return user.nick
    else: return user.name


def compare(str1, str2):
    print("{0} | {1}".format(str1, str2))


class Util:

    def __init__(self, bot):
        self.bot = bot

    # Returns the roles of the user or target
    @commands.command(pass_context=True)
    async def roles(self, ctx, user: discord.Member = None):
        if user is None: user = ctx.message.author
        content = "The roles of {} are:".format(get_name(user))
        for role in user.roles:
            if role.name != "@everyone": content += " {},".format(role.name)
        content = content.rstrip(",")
        await self.bot.say(content)

    @commands.command(pass_context=True)
    async def info(self, ctx, user: discord.Member = None):
        if user is None: user = ctx.message.author
        date = user.created_at
        dow = dates[date.weekday()]
        month = months[date.month]
        content = "{0}'s account was created on {1}, {2} {3}, {4} at {5}:{6}".format(get_name(user), dow, month,
                                                                                     date.day, date.year, date.hour,
                                                                                     date.minute)
        await self.bot.say(content)


def setup(bot):
    bot.add_cog(Util(bot))

