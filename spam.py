import discord
from util import *

def Fuck(num=None):
    if num is None: num="5"
    if is_int(num)==False: return "Fuck you"
    elif int(num) > 0 and int(num)<=50:
        str=""
        num_i=int(num)
        for i in range(1, num_i+1):
            str+="FUCK\n"
        return str
    else: return "Fuck you"

def Pyr(arg=None, cent=None):
    if arg is None: arg="a"
    if len(arg)>1: arg += " "
    if arg[0]!=":" and arg[-1]!=":": arg = arg.replace("_", " ")
    if cent is None: cent=""
    if is_int(cent)==False: center=3
    elif cent is None: center=3
    else: center=int(cent)
    pyr_flag = False
    if center > 43 or len(arg)*center>100: pyr_flag = True
    elif pyr_flag and arg[0]!=":" and arg[-1]!=":": return "Too much pyramid"
    else:
        str=""
        for line in range(1,center+2):
            for i in range(1, line):
                str+=arg
            str+="\n"
        for line in range(center, 1, -1):
            for i in range(1, line):
                str+=arg
            str+="\n"
        return str