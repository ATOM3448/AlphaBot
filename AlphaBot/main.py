import Command_GetMyInventory
import Command_StartRegistration
import System_GetInfoOfUser
import discord
from discord.ext import commands
from System_Config import settings

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = settings['prefix'], intents=intents)

#тест класса
@bot.command()
@commands.has_permissions(administrator=True)
async def clastes(ctx, nameOfRes, when = 'общий'):
    await ctx.send(str(System_GetInfoOfUser.getExtractionChResBal(ctx.message.author.id, nameOfRes, when)))

#информация о игроке
@bot.command()
async def info(ctx):
    await Command_GetMyInventory.inf(ctx, bot)

#информация о игроке для админов
@bot.command()
@commands.has_permissions(administrator=True)
async def infoFA(ctx, userpin):
    await Command_GetMyInventory.infFA(ctx, bot, userpin)

#новая регистрация
@bot.command()
@commands.has_permissions(administrator=True)
async def newreg(ctx):
    await Command_StartRegistration.newreg(ctx, bot)

#действия на добавление реакции
@bot.event
async def on_raw_reaction_add(self):
    await Command_StartRegistration.roleset(bot, self)

bot.run(settings['token'])