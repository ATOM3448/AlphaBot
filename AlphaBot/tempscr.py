from System_Config import settingsForSrever as localSet
import asyncio
import discord
import System_DataActions as db
from System_Resource import res

async def giveres(ctx, where, turn, name, value):
    now = db.get_turn(ctx.message.author.id, where)
    if(now < int(turn)):
        db.add_turn(ctx.message.author.id, where, turn)
    db.set_res(ctx.message.author.id, where, turn, name, value)