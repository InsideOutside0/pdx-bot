import discord

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
         0: "Sunday"}

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
         12: "December",}

coms = ["roles [user]- check your roles, or the roles of the selected user",
            "info [user] - gives your info or that of the selected user",
            "pyr [letter/word] [size] - spams a pyramid",
            "fuck [iterations] - fuck",
            "insult [user] - send a diplomatic insult",
            "DOW [user] - declares war on the target",
            "battle [user] - battles the target",
            "gift [target - sends a gift to the target"]

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

def Info(user: discord.Member):
    date = user.created_at
    dow = dates[date.weekday()]
    month = months[date.month]
    str = "{0}'s account was created on {1}, {2} {3}, {4} at {5}:{6}".format(get_name(user), dow, month,
                                                                            date.day, date.year, date.hour, date.minute)
    return str
