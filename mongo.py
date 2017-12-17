import pymongo
from mongoengine import *
import discord

class User(Document):
    name = StringField(required=True)
    wars = ListField(required=True)
    soldiers = IntField(required=True)

