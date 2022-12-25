import Command_StartRegistration
import ComPart_Konkist_Menu
import discord
from discord.ext import commands
from System_Config import settings

import tempscr as tp

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = settings['prefix'], intents=intents)

# Тест класса
@bot.command()
@commands.has_permissions(administrator=True)
async def clastes(ctx):
    await ComPart_Konkist_Menu.getTechMenu(ctx, bot)

# Установка валюты
@bot.command()
@commands.has_permissions(administrator=True)
async def cheat(ctx, where, turn, res, value):
    await tp.giveres(ctx, where, turn, res, value)

# Новая регистрация
@bot.command()
@commands.has_permissions(administrator=True)
async def newreg(ctx):
    await Command_StartRegistration.newreg(ctx)

# Действия на добавление реакции
@bot.event
async def on_raw_reaction_add(self):
    await Command_StartRegistration.roleset(bot, self)

bot.run(settings['token'])