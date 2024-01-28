from model import *

with DB:
    DB.create_tables([User, Message, Relationship])
