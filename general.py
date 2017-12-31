from random import *
import discord
import math
from util import *

class General:

    terrain = {"grassy": 1,
               "desert": 1,
               "hilly": 1.25,
               "forested": 1.25,
               "jungle": 1.5,
               "mountainous": 1.5}

    general_names = ["Nappleon Borntoparty",
                     "Captain Shrimp",
                     "Gott von Moltke",
                     "Alexander the Dead",
                     "Enrique IV de Trastamara",
                     "Santa Clausewitz"]

    def __init__(self, name):
        self.name = name
        self.fire = None
        self.shock = None
        self.maneuver = None
        self.siege = None

    def create_stats(self):
        self.fire=randint(0,6)
        self.shock=randint(0,6)
        self.maneuver=randint(0,6)
        self.siege=randint(0,6)

    @classmethod #Creates a randomly generated battle
    def battle(cls, user: discord.Member, target: discord.Member):
        if target is None: return "Pick a target ya dummy"
        elif target == user: return "{0} wants to battle themself.\nBoth sides have lost".format(get_name(user))

        user_name = get_name(user)
        target_name = get_name(target)

        u_general_name=sample(cls.general_names, 1)
        t_general_name=sample(cls.general_names, 1)
        while u_general_name[0] == t_general_name[0]:
            t_general_name = sample(cls.general_names, 1)
        u_general = General(u_general_name[0])
        t_general = General(t_general_name[0])
        u_general.create_stats()
        t_general.create_stats()

        is_river=True
        if randint(1,2)==2: is_river=False
        river_penalty=1
        if t_general.maneuver>=u_general.maneuver and is_river: river_penalty=1.25
        battle_terrain = choice(list(cls.terrain.keys()))
        terrain_penalty=cls.terrain[battle_terrain]

        u_troops = float(randint(0, 100000))
        t_troops = float(randint(0, 100000))
        u_deaths = (t_troops/20)*(1+t_general.fire/10)+ (t_troops/20)*(1+t_general.shock/10)
        u_deaths = u_deaths*terrain_penalty*river_penalty
        t_deaths = (u_troops/20)*(1+u_general.fire/10)+ (u_troops/20)*(1+u_general.shock/10)

        u_deaths=int(math.floor(u_deaths))
        t_deaths=int(math.floor(t_deaths))
        u_troops=int(math.floor(u_troops))
        t_troops=int(math.floor(t_troops))
        if u_deaths>u_troops: u_deaths=u_troops
        if t_deaths>t_troops: t_deaths=t_troops
        u_remaining=u_troops-u_deaths
        t_remaining = t_troops-t_deaths

        winner = None
        if u_remaining>t_remaining: winner = get_name(user)
        else: winner = get_name(target)
        crossing = None
        if is_river: crossing = "will"
        else: crossing = "will not"

        return "{0} has initiated a battle with {1} on a {17} terrain!\n" \
               "The attacker {18} face a river crossing penalty.\n" \
               "{0} will start out with {2} troops, and {1} with {3}.\n" \
               "{0}'s general, {4}, a {5} {6} {7} {8}, will fight {1}'s general, {9}, a {10} {11} {12} {13}. " \
               "{0} has lost {14} men, and {1} has lost {15}\n{16} is the winner!"\
            .format(user_name, target_name, str(u_troops), str(t_troops), u_general.name, str(u_general.fire), str(u_general.shock),
                    str(u_general.maneuver), str(u_general.siege), t_general.name, str(t_general.fire), str(t_general.shock),
                    str(t_general.maneuver), str(t_general.siege), str(u_deaths), str(t_deaths), winner, battle_terrain, crossing)