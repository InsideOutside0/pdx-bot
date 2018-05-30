import discord
from discord.ext import commands
from util import *
from random import *

classes = ["English",
           "Math Anal-ISIS",
           "Calculus",
           "Chemistry",
           "Dick Physics",
           "Gov",
           "APUSH",
           "Spanglish",
           "Baguette class",
           "Comp Gov",
           "Comp Sci", ]


class Spam:

    def __init__(self, bot):
        self.bot = bot

    # Spams a pyramid of desired size
    @commands.command(pass_context=False)
    async def pyr(self, arg=None, cent=None):
        if arg is None: arg = "a"
        if len(arg) > 1: arg += " "
        if arg[0] != ":" and arg[-1] != ":": arg = arg.replace("_", " ")
        if cent is None: cent = ""
        if is_int(cent) == False: center = 3
        elif cent is None: center = 3
        else: center = int(cent)
        pyr_flag = False
        if center > 43 or len(arg) * center > 100:
            content = "Too much pyramid"
        elif pyr_flag and arg[0] != ":" and arg[-1] != ":":
            content = "Too much pyramid"
        else:
            content = ""
            for line in range(1, center + 2):
                for i in range(1, line):
                    content += arg
                content += "\n"
            for line in range(center, 1, -1):
                for i in range(1, line):
                    content += arg
                content += "\n"
        await self.bot.say(content)

    # Says "FUCK" a select number of times
    @commands.command(pass_context=False)
    async def fuck(self, num=None):
        if num is None: num = "5"
        if is_int(num) == False:
            content = "Fuck you"
        elif int(num) > 0 and int(num) <= 50:
            content = ""
            num_i = int(num)
            for i in range(1, num_i + 1):
                content += "FUCK\n"
        else:
            content = "Fuck you"
        await self.bot.say(content)

    @commands.command(pass_context=False)
    async def test(self):
        test_class = sample(classes, 1)[0]
        tier = randint(1, 10)

        if tier == 1:
            score = str(randint(0, 50))
        elif tier == 2:
            score = str(randint(50, 60))
        elif tier == 3:
            score = str(randint(60, 70))
        elif tier == 4 or tier == 5:
            score = str(randint(70, 80))
        elif tier >= 6 and tier <= 8:
            score = str(randint(80, 90))
        elif tier == 9 or tier == 10:
            score = str(randint(90, 100))

        content = "You got a {0} on your {1} test".format(score, test_class)
        await self.bot.say(content)


def setup(bot):
    bot.add_cog(Spam(bot))