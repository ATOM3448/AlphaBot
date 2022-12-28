import discord
import ComPart_RegistationNewKonkist
from System_Config import settingsForSrever as localSet
import sqlite3

async def newreg(ctx):
    embed1 = discord.Embed(title = 'Регистрация', description = 'Для завершения регистрации напишите выбранную расу\nПОВТОРНО ВЫБРАТЬ НЕ ПОЛУЧИТСЯ\nя пытался',
    colour=0x008b)
    embed1.add_field(name="1️⃣Конкистадоры", value='Чтобы выбрать поставьте реакцию', inline=True)
    embed1.add_field(name="2️⃣Матрикс", value='Чтобы выбрать поставьте реакцию', inline=True)
    embed1.add_field(name="3️⃣Крюксы", value='Чтобы выбрать поставьте реакцию', inline=True)
    embed1.add_field(name="4️⃣Ящуры", value='Чтобы выбрать поставьте реакцию', inline=True)
    embed1.add_field(name="5️⃣Биомехи", value='Чтобы выбрать поставьте реакцию', inline=True)
    embed1.add_field(name="6️⃣Симилянты", value='Чтобы выбрать поставьте реакцию', inline=True)
    embed1.add_field(name="7️⃣Спектралы", value='Чтобы выбрать поставьте реакцию', inline=True)
    embed1.add_field(name="Раса8️⃣", value='Пока не существует', inline=True)
    embed1.add_field(name="Раса9️⃣", value='Не существует', inline=True)
    panel1 = await ctx.send(embed = embed1)

    with sqlite3.connect('System_BotData/SystemData.db') as db:
        cursor = db.cursor()

        cursor.execute("""DROP TABLE IF EXISTS RegPanelID;""")

        db.commit()

        cursor.execute("""CREATE TABLE IF NOT EXISTS RegPanelID(
            id INTEGER PRIMARY KEY,
            MessageOfRegistrationPanel INT);
            """)

        cursor.execute(f"""INSERT INTO RegPanelID VALUES(1, {panel1.id});""")

        db.commit()

    await panel1.add_reaction('1️⃣')
    await panel1.add_reaction('2️⃣')
    await panel1.add_reaction('3️⃣')
    await panel1.add_reaction('4️⃣')
    await panel1.add_reaction('5️⃣')
    await panel1.add_reaction('6️⃣')
    await panel1.add_reaction('7️⃣')

async def roleset(bot, self):

    with sqlite3.connect('System_BotData/SystemData.db') as db:
        cursor = db.cursor()
        cursor.execute("""SELECT * from RegPanelID""")
        pane = cursor.fetchall()
        
    pane = pane[0][1]

    if(self.message_id != pane): #проверяем рег панель ли это
        return
    if(self.member.bot == True):
        return
    
    guild = bot.get_guild(localSet['guild'])
    roles = self.member.roles
    rolin = guild.get_role(localSet['regrole'])
    if(not(rolin in roles)):
        return
    
    
    if(self.emoji == discord.PartialEmoji(name = '1️⃣')): #КОНКИСТЫ 655340889530433536
        role_id = localSet['konkisti']
        role = guild.get_role(role_id)
        await ComPart_RegistationNewKonkist.regKon(self, bot)
        await self.member.add_roles(role)
    if(self.emoji == discord.PartialEmoji(name = '2️⃣')): #МАТРИКС 653246548762951680
        role_id = localSet['matriks']
        role = guild.get_role(role_id)
        await self.member.add_roles(role)
    if(self.emoji == discord.PartialEmoji(name = '3️⃣')): #КРЮКСЫ 652224021533818912
        role_id = localSet['cruks']
        role = guild.get_role(role_id)
        await self.member.add_roles(role)
    if(self.emoji == discord.PartialEmoji(name = '5️⃣')): #БИОМЕХИ 760752746965762078
        role_id = localSet['biomachine']
        role = guild.get_role(role_id)
        await self.member.add_roles(role)
    if(self.emoji == discord.PartialEmoji(name = '7️⃣')): #СПЕКТРАЛЫ 778016234368794667
        role_id = localSet['spectrals']
        role = guild.get_role(role_id)
        await self.member.add_roles(role)
    if(self.emoji == discord.PartialEmoji(name = '6️⃣')): #СИМЕЛЯНТЫ 674317063246053387
        role_id = localSet['similants']
        role = guild.get_role(role_id)
        await self.member.add_roles(role)
    if(self.emoji == discord.PartialEmoji(name = '4️⃣')): #ЯЩУРЫ 675802459691679766
        role_id = localSet['yashur']
        role = guild.get_role(role_id)
        await self.member.add_roles(role)
    
    with sqlite3.connect(f'System_BotData/SystemData.db') as db:
        cursor = db.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS List_of_players(
            Discord_ID INT PRIMARY KEY,
            Discord_Name TEXT);
            """)
        
        db.commit()

        cursor.execute(f"""INSERT INTO List_of_players VALUES({self.user_id}, "{self.member.display_name}");""")

        db.commit()

    await self.member.remove_roles(rolin)