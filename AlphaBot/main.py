import Command_StartRegistration
import ComPart_Konkist_Menu
import Command_New_Turn
import Command_Welcome
import discord
from discord.ext import commands
from System_Config import settings

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = settings['prefix'], intents=intents)

# Тест класса
@bot.command()
@commands.has_permissions(administrator=True)
async def clastes(ctx):
    await ComPart_Konkist_Menu.getManageGarbMenu(ctx, bot)

# Заселение
@bot.command()
async def welc(ctx, user):
    await Command_Welcome.start_game(user, ctx.message.channel.name)

# Следующий ход
@bot.command()
async def Go(ctx):
    await Command_New_Turn.goNext(ctx)

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