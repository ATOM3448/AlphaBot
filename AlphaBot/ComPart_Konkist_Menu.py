import asyncio
import discord
import System_DataActions as db
from System_Resource import res

async def getShipMenu(ctx, bot):
    user = ctx.message.author.id
    embed1 = discord.Embed(title = 'Меню постройки', description='Отправьте НОМЕР для постройки', colour=0x008b)
    
    # Лёгкие
    embed1.add_field(name = "1. Мусорщик", value = f"Роль: Добыча\nСтоимость: 200{res['titan']}\nЭкипаж: 20{res['zest']}\nВремя: 2\nДобыча: 40\nНеобходим: Лёгкий верфяник/Станция", inline=True)
    embed1.add_field(name = "2. Каменщик", value = f"Роль: Добыча\nСтоимость: 500{res['titan']}\nЭкипаж: 10{res['zest']}\nВремя: 2\nДобыча: 4\nНеобходим: Лёгкий верфяник/Станция", inline=True)
    embed1.add_field(name = "3. Лёгкий Верфяник", value = f"Роль: Производство\nСтоимость: 500{res['titan']}\nЭкипаж: 50{res['zest']}\nПотребление: 50{res['energy']}\nВремя: 2\nПроизводство: 4\nНеобходим: Лёгкий верфяник/ОК", inline=True)
    embed1.add_field(name = "4. Истребитель-Капля", value = f"Роль: Боевой\nСтоимость: 1000{res['titan']}\nПотребление: 200{res['energy']}\nВремя: 2\nНеобходим: Лёгкий верфяник", inline=True)
    embed1.add_field(name = "5. Каравелла", value = f"Роль: Боевой\nСтоимость: 300{res['titan']}\nПерестройка: 100{res['zest']}\nЭкипаж: 50{res['zest']}\nПотребление: 75{res['energy']}\nВремя: 2\nНеобходим: Лёгкий верфяник", inline=True)

    # Средние
    embed1.add_field(name = "6. Средний Верфяник", value = f"Роль: Производство\nСтоимость: 700{res['titan']}\nЭкипаж: 100{res['zest']}\nПотребление: 100{res['energy']}\nВремя: 3\nПроизводство: 2\nНеобходим: Средний верфяник/ОК", inline=True)
    embed1.add_field(name = "7. Галера", value = f"Роль: Боевой\nСтоимость: 600{res['titan']}\nЭкипаж: 150{res['zest']}\nПотребление: 150{res['energy']}\nВремя: 3\nНеобходим: Средний верфяник", inline=True)
    embed1.add_field(name = "8. Фрегат", value = f"Роль: Боевой\nСтоимость: 500{res['titan']}\nЭкипаж: 200{res['zest']}\nПотребление: 150{res['energy']}\nВремя: 3\nНеобходим: Средний верфяник", inline=True)
    embed1.add_field(name = "9. Линкор", value = f"Роль: Боевой\nСтоимость: 1000{res['titan']} 300{res['volst']}\nЭкипаж: 300{res['zest']}\nПотребление: 300{res['energy']}\nВремя: 3\nНеобходим: Средний верфяник", inline=True)

    # Тяжёлые
    embed1.add_field(name = "10. Тяжёлый Верфяник", value = f"Роль: Производство\nСтоимость: 1000{res['titan']} 500{res['volst']}\nЭкипаж: 400{res['zest']}\nПотребление: 500{res['energy']}\nВремя: 4\nПроизводство: 1\nНеобходим: Тяжёлый верфяник/ОК", inline=True)
    embed1.add_field(name = "11. Погибель", value = f"Роль: Боевой\nСтоимость: 3000{res['volst']}\nЭкипаж: 500{res['zest']}\nПотребление: 600{res['energy']}\nВремя: 4\nНеобходим: Тяжёлый верфяник", inline=True)
    embed1.add_field(name = "12. Корсар", value = f"Роль: Боевой\nСтоимость: 3000{res['volst']}\nЭкипаж: 600{res['zest']}\nПотребление: 600{res['energy']}\nВремя: 4\nНеобходим: Тяжёлый верфяник", inline=True)
    embed1.add_field(name = "13. Бомбардир", value = f"Роль: Боевой\nСтоимость: 4500{res['volst']}\nЭкипаж: 500{res['zest']}\nПотребление: 700{res['energy']}\nВремя: 4\nНеобходим: Тяжёлый верфяник", inline=True)
    embed1.add_field(name = "14. Браконьер", value = f"Роль: Боевой\nСтоимость: 6000{res['volst']} 20 {res['sverol']}\nЭкипаж: 500{res['zest']}\nПотребление: 1000{res['energy']}\nВремя: 4\nНеобходим: Тяжёлый верфяник", inline=True)
    embed1.add_field(name = "15. Серая Шляпа", value = f"Роль: Особый\nСтоимость: 2500{res['volst']} 100 {res['kamen3']}\nЭкипаж: 2000{res['zest']}\nПотребление: 1000{res['energy']}\nВремя: 4\nНеобходим: Тяжёлый верфяник", inline=True)
    embed1.add_field(name = "16. Красный Шарф", value = f"Роль: Особый\nСтоимость: 2500{res['volst']} 100 {res['kamen3']}\nЭкипаж: 1000{res['zest']}\nПотребление: 1000{res['energy']}\nВремя: 4\nНеобходим: Тяжёлый верфяник", inline=True)
    embed1.add_field(name = "17. Чёрная перчатка", value = f"Роль: Особый\nСтоимость: 2500{res['volst']} 100 {res['kamen3']}\nЭкипаж: 1000{res['zest']}\nПотребление: 1000{res['energy']}\nВремя: 4\nНеобходим: Тяжёлый верфяник", inline=True)
    embed1.add_field(name = "18. Синий Сапог", value = f"Роль: Особый\nСтоимость: 2500{res['volst']} 100 {res['kamen3']}\nЭкипаж: 1000{res['zest']}\nПотребление: 1000{res['energy']}\nВремя: 4\nНеобходим: Тяжёлый верфяник", inline=True)

    # Вспомогательные
    embed1.add_field(name = "19. Станция", value = f"Роль: Универсален\nСтоимость: 6000{res['titan']} 1000{res['volst']} 3000{res['energy']}\nЭкипаж: 500{res['zest']}\nПотребление: 500{res['energy']}\nВремя: 5\nПроизводство: 10\nНеобходим: ОК", inline=True)
    embed1.add_field(name = "20. Научное судно", value = f"Роль: Исследования\nСтоимость: 1700{res['titan']} 250{res['kamen2']} 500{res['energy']}\nЭкипаж: 1000{res['zest']}\nПотребление: 1000{res['energy']}\nВремя: 5\nНеобходим: ОК", inline=True)
    embed1.add_field(name = "21. Вахтер", value = f"Роль: Детектор\nСтоимость: 900{res['titan']} 700{res['energy']}\nЭкипаж: 100{res['zest']}\nПотребление: 200{res['energy']}\nВремя: 5\nНеобходим: ОК", inline=True)
    embed1.add_field(name = "22. Солярист", value = f"Роль: Производство\nСтоимость: 15000{res['volst']} 10{res['sverol']}\nВремя: 5\nПроизводство: inf\nНеобходим: ОК", inline=True)

    await ctx.send(embed = embed1)

    # Ожидаем ввод
    check = lambda m: m.author == ctx.author and m.channel == ctx.channel
    try:
        type = await bot.wait_for('message', check=check, timeout=45)
    except asyncio.TimeoutError:
        await ctx.send('Команда постройки отменена. Время вышло')
        return

    # Преобразование типа, для дальнейшей работы
    try:
        type = int(type.clean_content)
    except ValueError:
        await ctx.send('Убедитесь, что вводите число')
        return

    # Проверяем корректность ввода и запрашиваем количество
    if((type >= 1) and (type <= 22)):
        await ctx.send('Введите количество')
    else:
        await ctx.send('Не верный тип')
        return
    
    # Ожидание ввода
    try:
        count = await bot.wait_for('message', check=check, timeout=15)
    except asyncio.TimeoutError:
        await ctx.send('Команда постройки отменена. Время вышло')
        return

    # Преобразование типа, для дальнейшей работы
    try:
        count = int(count.clean_content)
    except ValueError:
        await ctx.send('Убедитесь, что вводите число')
        return

    # Проверим на <=0
    if(count <= 0):
        await ctx.send('Значение должно быть больше 0')
        return

    # Функция проверки может ли игрок позволить себе заказ
    def check_price(player, list_res, list_price, count):
        last_Turn = db.get_turn(player, 'общий')
        for i in range(len(list_res)):
            if(db.get_res(player, 'общий', last_Turn, list_res[i]) < list_price[i]*count):
                return 0
        return 1

    # Функция проверки производственной мощности
    def check_slot(player, wight, count):
        last_Turn = db.get_turn(player, 'общий')
        if(db.get_active_process_w(player, last_Turn, wight)+count > db.get_max_process_c(player, last_Turn, wight)):
            return 0
        return 1
    
    # Обрабатываем заказ пользователя
    last_Turn = db.get_turn(user, 'общий')

    # Проверяем, хватает ли мощностей
    if((type <= 5)and(type >= 1)):
        if(not(check_slot(user, 1, count))):
            await ctx.send('Недостаточно производственных мощностей')
            return
    if((type <= 9)and(type >= 6)):
        if(not(check_slot(user, 2, count))):
            await ctx.send('Недостаточно производственных мощностей')
            return
    if((type <= 18)and(type >= 10)):
        if(not(check_slot(user, 3, count))):
            await ctx.send('Недостаточно производственных мощностей')
            return
    if((type <= 22)and(type >= 19)):
        if(not(check_slot(user, 4, count))):
            await ctx.send('Недостаточно производственных мощностей')
            return

    # Формируем цену
    list_res = []
    list_price = []
    if (type == 1):
        list_res.append(db.itemslocal[3])
        list_res.append(db.itemslocal[2])

        list_price.append(200)
        list_price.append(20)
        
    if (type == 2):
        list_res.append(db.itemslocal[3])
        list_res.append(db.itemslocal[2])

        list_price.append(500)
        list_price.append(10)
        
    if (type == 3):
        list_res.append(db.itemslocal[3])
        list_res.append(db.itemslocal[2])

        list_price.append(500)
        list_price.append(50)
        
    if (type == 4):
        list_res.append(db.itemslocal[3])

        list_price.append(100)
        
    if (type == 5):
        list_res.append(db.itemslocal[3])
        list_res.append(db.itemslocal[2])

        list_price.append(300)
        list_price.append(50)
        
    if (type == 6):
        list_res.append(db.itemslocal[3])
        list_res.append(db.itemslocal[2])

        list_price.append(700)
        list_price.append(100)
        
    if (type == 7):
        list_res.append(db.itemslocal[4])
        list_res.append(db.itemslocal[3])

        list_price.append(600)
        list_price.append(150)
        
    if (type == 8):
        list_res.append(db.itemslocal[3])
        list_res.append(db.itemslocal[2])

        list_price.append(500)
        list_price.append(200)
        
    if (type == 9):
        list_res.append(db.itemslocal[4])
        list_res.append(db.itemslocal[3])
        list_res.append(db.itemslocal[2])

        list_price.append(300)
        list_price.append(1000)
        list_price.append(300)
        
    if (type == 10):
        list_res.append(db.itemslocal[4])
        list_res.append(db.itemslocal[3])
        list_res.append(db.itemslocal[2])

        list_price.append(500)
        list_price.append(1000)
        list_price.append(400)
        
    if (type == 11):
        list_res.append(db.itemslocal[4])
        list_res.append(db.itemslocal[2])

        list_price.append(3000)
        list_price.append(500)
        
    if (type == 12):
        list_res.append(db.itemslocal[4])
        list_res.append(db.itemslocal[2])

        list_price.append(3000)
        list_price.append(600)
        
    if (type == 13):
        list_res.append(db.itemslocal[4])
        list_res.append(db.itemslocal[2])

        list_price.append(4500)
        list_price.append(500)
        
    if (type == 14):
        list_res.append(db.itemslocal[12])
        list_res.append(db.itemslocal[4])
        list_res.append(db.itemslocal[2])

        list_price.append(20)
        list_price.append(6000)
        list_price.append(500)
        
    if (type == 15):
        list_res.append(db.itemslocal[10])
        list_res.append(db.itemslocal[4])
        list_res.append(db.itemslocal[2])

        list_price.append(100)
        list_price.append(2500)
        list_price.append(2000)
        
    if (type == 16):
        list_res.append(db.itemslocal[10])
        list_res.append(db.itemslocal[4])
        list_res.append(db.itemslocal[2])

        list_price.append(100)
        list_price.append(2500)
        list_price.append(1000)
        
    if (type == 17):
        list_res.append(db.itemslocal[10])
        list_res.append(db.itemslocal[4])
        list_res.append(db.itemslocal[2])

        list_price.append(100)
        list_price.append(2500)
        list_price.append(1000)
        
    if (type == 18):
        list_res.append(db.itemslocal[10])
        list_res.append(db.itemslocal[4])
        list_res.append(db.itemslocal[2])

        list_price.append(100)
        list_price.append(5000)
        list_price.append(1000)
        
    if (type == 19):
        list_res.append(db.itemslocal[7])
        list_res.append(db.itemslocal[4])
        list_res.append(db.itemslocal[3])
        list_res.append(db.itemslocal[2])

        list_price.append(3000)
        list_price.append(1000)
        list_price.append(6000)
        list_price.append(500)
        
    if (type == 20):
        list_res.append(db.itemslocal[9])
        list_res.append(db.itemslocal[7])
        list_res.append(db.itemslocal[3])
        list_res.append(db.itemslocal[2])

        list_price.append(250)
        list_price.append(500)
        list_price.append(1700)
        list_price.append(1000)

    if (type == 21):
        list_res.append(db.itemslocal[7])
        list_res.append(db.itemslocal[3])
        list_res.append(db.itemslocal[2])

        list_price.append(700)
        list_price.append(900)
        list_price.append(100)
        
    if (type == 22):
        list_res.append(db.itemslocal[12])
        list_res.append(db.itemslocal[4])

        list_price.append(10)
        list_price.append(15000)
    
    # Проверяем, достаточно ли ресурсов
    if(not(check_price(user, list_res, list_price, count))):
        await ctx.send('Недостаточно ресурсов')
        return        

    # Отправляем в процессы
    if((type <= 5)and(type >= 1)):
        db.set_process(user, type + 19, 1, count, last_Turn+2)
    if((type <= 9)and(type >= 6)):
        db.set_process(user, type + 19, 2, count, last_Turn+3)
    if((type <= 18)and(type >= 10)):
        db.set_process(user, type + 19, 3, count, last_Turn+4)
    if((type <= 22)and(type >= 19)):
        db.set_process(user, type + 19, 4, count, last_Turn+5)

    # Снимаем цену
    for i in range(len(list_res)):
        db.set_res(user, 'общий', last_Turn, list_res[i], db.get_res(user, 'общий', last_Turn, list_res[i]) - (list_price[i]*count))
    
    # Сообщение о успехе
    await ctx.send("Всё прошло успешно")

async def getTechMenu(ctx, bot):
    user = ctx.message.author.id

    last_turn = db.get_turn(user, 'общий')

    # Проверки возможности выполнения команды
    if(not(db.get_ship(user, 'общий', last_turn, db.itemslocal[39]))):
        await ctx.send("Для исследований необходимо научное судно")
        return 0

    # Проверка уже идущего изучения
    if(db.get_active_process_w(user, last_turn, 0)):
        tech_in_process = db.get_tech_in_process(user, last_turn)
        await ctx.send(f"У вас уже имеется в процессе изучение технологии {db.tech_list[tech_in_process[0]-101]} до которой осталось {tech_in_process[3] - last_turn} ходов")
        return 0
    
    # Список
    embed1 = discord.Embed(title = 'Меню изучений(общие)', description='Отправьте НОМЕР для старта изучения', colour=0x008b)

    tech_list = db.get_all_tech(user)

    embed1.add_field(name = "1. Кинетические ядра", value = f"Тип: Оружие\nВ наличии: {tech_list[0]}", inline=True)
    embed1.add_field(name = "2. Заряженные ядра", value = f"Тип: Оружие\nВ наличии: {tech_list[1]}\nСтоимость: 100{res['kamen2']}\nВремя: 5", inline=True)
    embed1.add_field(name = "3. Плазменные ядра", value = f"Тип: Оружие\nВ наличии: {tech_list[2]}\nСтоимость: 100{res['kamen2']} 100{res['kamen3']}\nВремя: 5", inline=True)
    embed1.add_field(name = "4. Нейтронные ядра", value = f"Тип: Оружие\nВ наличии: {tech_list[3]}\nСтоимость: 100{res['kamen2']} 100{res['kamen3']} 100{res['kamen4']}\nВремя: 5", inline=True)
    embed1.add_field(name = "5. Жёлтый луч", value = f"Тип: Оружие\nВ наличии: {tech_list[4]}", inline=True)
    embed1.add_field(name = "6. Алый луч", value = f"Тип: Оружие\nВ наличии: {tech_list[5]}\nСтоимость: 100{res['kamen3']} 300{res['volst']}\nВремя: 5", inline=True)
    embed1.add_field(name = "7. Тёмный луч", value = f"Тип: Оружие\nВ наличии: {tech_list[6]}\nСтоимость: 100{res['kamen4']} 400{res['volst']}\nВремя: 5", inline=True)

    embed1.add_field(name = "8. Обычная броня", value = f"Тип: Защита\nВ наличии: {tech_list[7]}", inline=True)
    embed1.add_field(name = "9. Заряженная броня", value = f"Тип: Защита\nВ наличии: {tech_list[8]}\nСтоимость: 100{res['kamen2']}\nВремя: 5", inline=True)
    embed1.add_field(name = "10. Алая броня", value = f"Тип: Защита\nВ наличии: {tech_list[9]}\nСтоимость: 100{res['kamen3']}\nВремя: 5", inline=True)
    embed1.add_field(name = "11. Тёмная броня", value = f"Тип: Защита\nВ наличии: {tech_list[10]}\nСтоимость: 100{res['kamen4']}\nВремя: 5", inline=True)
    embed1.add_field(name = "12. Грави-броня", value = f"Тип: Защита\nВ наличии: {tech_list[11]}\nСтоимость: 200{res['kamen4']} 10{res['sverol']}\nВремя: 5", inline=True)

    embed1.add_field(name = "13. Звёздные паруса", value = f"Тип: Перемещение\nВ наличии: {tech_list[12]}", inline=True)
    embed1.add_field(name = "14. Алые паруса", value = f"Тип: Перемещение\nВ наличии: {tech_list[13]}\nСтоимость: 100{res['kamen3']}\nВремя: 5", inline=True)
    embed1.add_field(name = "15. Тёмные паруса", value = f"Тип: Перемещение\nВ наличии: {tech_list[14]}\nСтоимость: 100{res['kamen4']}\nВремя: 5", inline=True)
    embed1.add_field(name = "16. Двигатель \"Тёмной энергии\"", value = f"Тип: Перемещение\nВ наличии: {tech_list[15]}\nСтоимость: 200{res['kamen4']}\nВремя: 5", inline=True)

    embed1.add_field(name = "17. Транспортный канал", value = f"Тип: Специализированные\nВ наличии: {tech_list[16]}\nСтоимость: 200{res['kamen2']} 1500{res['volst']}\nВремя: 5", inline=True)
    embed1.add_field(name = "18. Убежище", value = f"Тип: Специализированные\nВ наличии: {tech_list[17]}\nСтоимость: 300{res['kamen3']} 3000{res['volst']}\nВремя: 5", inline=True)
    embed1.add_field(name = "19. Транспортные кольца", value = f"Тип: Специализированные\nВ наличии: {tech_list[18]}\nСтоимость: 100{res['kamen4']} 5000{res['volst']}\nВремя: 5", inline=True)
    embed1.add_field(name = "20. Насморк", value = f"Тип: Специализированные\nВ наличии: {tech_list[19]}\nСтоимость: 80{res['kamen3']} 4000{res['volst']}\nВремя: 5", inline=True)
    embed1.add_field(name = "21. Тугие сплавы", value = f"Тип: Специализированные\nВ наличии: {tech_list[20]}\nСтоимость: 400{res['kamen3']} 3000{res['volst']}\nВремя: 5", inline=True)
    embed1.add_field(name = "22. ★Солнечная Эра★", value = f"Тип: Специализированные\nВ наличии: {tech_list[21]}\nСтоимость: 100{res['relik']} 10{res['antivec']}\nВремя: 1", inline=True)

    await ctx.send(embed = embed1)
    embed1 = discord.Embed(title = 'Меню изучений(капитанские)', description='Отправьте НОМЕР для старта изучения', colour=0x008b)

    embed1.add_field(name = "23. Каменистые", value = f"Тип: Серая Шляпа\nВ наличии: {tech_list[22]}\nСтоимость: 250{res['kamen2']}\nНеобходим: ★Серая Шляпа★\nВремя: 5", inline=True)
    embed1.add_field(name = "24. Второй слой", value = f"Тип: Серая Шляпа\nВ наличии: {tech_list[23]}\nСтоимость: 300{res['kamen3']}\nНеобходим: ★Серая Шляпа★\nВремя: 5", inline=True)
    embed1.add_field(name = "25. Природные способности", value = f"Тип: Серая Шляпа\nВ наличии: {tech_list[24]}\nСтоимость: 500{res['kamen4']}\nНеобходим: ★Серая Шляпа★\nВремя: 5", inline=True)

    embed1.add_field(name = "26. Алые", value = f"Тип: Красный Шарф\nВ наличии: {tech_list[25]}\nСтоимость: 300{res['kamen4']}\nНеобходим: ★Красный Шарф★\nВремя: 3", inline=True)
    embed1.add_field(name = "27. Лучевая болезнь", value = f"Тип: Красный Шарф\nВ наличии: {tech_list[26]}\nСтоимость: 350{res['kamen4']}\nНеобходим: ★Красный Шарф★\nВремя: 3", inline=True)
    embed1.add_field(name = "28. Импульсивная броня", value = f"Тип: Красный Шарф\nВ наличии: {tech_list[27]}\nСтоимость: 400{res['kamen4']}\nНеобходим: ★Красный Шарф★\nВремя: 3", inline=True)
    embed1.add_field(name = "29. Алое пламя", value = f"Тип: Красный Шарф\nВ наличии: {tech_list[28]}\nСтоимость: 400{res['kamen4']}\nНеобходим: ★Красный Шарф★\nВремя: 3", inline=True)
    embed1.add_field(name = "30. Алые камни", value = f"Тип: Красный Шарф\nВ наличии: {tech_list[29]}\nСтоимость: 500{res['kamen4']}\nНеобходим: ★Красный Шарф★\nВремя: 3", inline=True)

    embed1.add_field(name = "31. Тёмные", value = f"Тип: Чёрная Перчатка\nВ наличии: {tech_list[30]}\nСтоимость: 200{res['kamen3']}\nНеобходим: ★Чёрная Перчатка★\nВремя: 4", inline=True)
    embed1.add_field(name = "32. Чёрная метка", value = f"Тип: Чёрная Перчатка\nВ наличии: {tech_list[31]}\nСтоимость: 300{res['kamen3']}\nНеобходим: ★Чёрная Перчатка★\nВремя: 4", inline=True)
    embed1.add_field(name = "33. Вылазка", value = f"Тип: Чёрная Перчатка\nВ наличии: {tech_list[32]}\nСтоимость: 400{res['kamen3']}\nНеобходим: ★Чёрная Перчатка★\nВремя: 4", inline=True)
    embed1.add_field(name = "34. Проникновение", value = f"Тип: Чёрная Перчатка\nВ наличии: {tech_list[33]}\nСтоимость: 250{res['kamen3']}\nНеобходим: ★Чёрная Перчатка★\nВремя: 4", inline=True)
    embed1.add_field(name = "35. Тёмные силы", value = f"Тип: Чёрная Перчатка\nВ наличии: {tech_list[34]}\nСтоимость: 450{res['kamen3']}\nНеобходим: ★Чёрная Перчатка★\nВремя: 4", inline=True)

    embed1.add_field(name = "36. Синие", value = f"Тип: Синий Сапог\nВ наличии: {tech_list[35]}\nСтоимость: 400{res['kamen2']}\nНеобходим: ★Синий Сапог★\nВремя: 6", inline=True)
    embed1.add_field(name = "37. Синий луч", value = f"Тип: Синий Сапог\nВ наличии: {tech_list[36]}\nСтоимость: 500{res['kamen2']}\nНеобходим: ★Синий Сапог★\nВремя: 6", inline=True)
    embed1.add_field(name = "38. Совмещение", value = f"Тип: Синий Сапог\nВ наличии: {tech_list[37]}\nСтоимость: 600{res['kamen2']}\nНеобходим: ★Синий Сапог★\nВремя: 6", inline=True)

    await ctx.send(embed = embed1)

     # Ожидаем ввод
    check = lambda m: m.author == ctx.author and m.channel == ctx.channel
    try:
        type = await bot.wait_for('message', check=check, timeout=30)
    except asyncio.TimeoutError:
        await ctx.send('Команда изучения отменена. Время вышло')
        return

    # Преобразование типа, для дальнейшей работы
    try:
        type = int(type.clean_content)
    except ValueError:
        await ctx.send('Убедитесь, что вводите число')
        return

    # Проверяем область значений
    if(not((type >= 1) and (type <= 38))):
        await ctx.send('Не верный тип')
        return
    
    # Отедельная проверка возможности изучать капитанские корабли
    if((type >= 23) and (type <= 38)):
        if((type >= 23) and (type <= 25) and not(db.get_ship(user, 'общий', last_turn, db.itemslocal[34]))):
            await ctx.send('Для этой технологии нужен определенный капитанский корабль')
            return 0
        if((type >= 26) and (type <= 30) and not(db.get_ship(user, 'общий', last_turn, db.itemslocal[35]))):
            await ctx.send('Для этой технологии нужен определенный капитанский корабль')
            return 0
        if((type >= 31) and (type <= 35) and not(db.get_ship(user, 'общий', last_turn, db.itemslocal[36]))):
            await ctx.send('Для этой технологии нужен определенный капитанский корабль')
            return 0
        if((type >= 36) and (type <= 38) and not(db.get_ship(user, 'общий', last_turn, db.itemslocal[37]))):
            await ctx.send('Для этой технологии нужен определенный капитанский корабль')
            return 0
        
    # Формируем цену
    list_res = []
    list_price = []
    if (type == 1):
        if(tech_list[type-1]):
            await ctx.send("Технология уже изучена")
            return 0
    if (type == 2):
        if(tech_list[type-1]):
            await ctx.send("Технология уже изучена")
            return 0
        list_res.append(db.itemslocal[9])

        list_price.append(100)

    if type == 3:
        if(tech_list[type-1]):
            await ctx.send("Технология уже изучена")
            return 0

        list_res.append(db.itemslocal[9])
        list_res.append(db.itemslocal[10])

        list_price.append(100)
        list_price.append(100)

    if type == 4:
        if(tech_list[type-1]):
            await ctx.send("Технология уже изучена")
            return 0

        list_res.append(db.itemslocal[9])
        list_res.append(db.itemslocal[10])
        list_res.append(db.itemslocal[11])

        list_price.append(100)
        list_price.append(100)
        list_price.append(100)

    if type == 5:
        if(tech_list[type-1]):
            await ctx.send("Технология уже изучена")
            return 0


    if type == 6:
        if(tech_list[type-1]):
            await ctx.send("Технология уже изучена")
            return 0

        list_res.append(db.itemslocal[10])
        list_res.append(db.itemslocal[4])

        list_price.append(100)
        list_price.append(300)

    if type == 7:
        if(tech_list[type-1]):
            await ctx.send("Технология уже изучена")
            return 0

        list_res.append(db.itemslocal[11])
        list_res.append(db.itemslocal[4])

        list_price.append(100)
        list_price.append(300)

    if type == 8:
        if(tech_list[type-1]):
            await ctx.send("Технология уже изучена")
            return 0


    if type == 9:
        if(tech_list[type-1]):
            await ctx.send("Технология уже изучена")
            return 0

        list_res.append(db.itemslocal[9])

        list_price.append(100)


    if type == 10:
        if(tech_list[type-1]):
            await ctx.send("Технология уже изучена")
            return 0

        list_res.append(db.itemslocal[10])

        list_price.append(100)


    if type == 11:
        if(tech_list[type-1]):
            await ctx.send("Технология уже изучена")
            return 0

        list_res.append(db.itemslocal[11])

        list_price.append(100)


    if type == 12:
        if(tech_list[type-1]):
            await ctx.send("Технология уже изучена")
            return 0

        list_res.append(db.itemslocal[11])
        list_res.append(db.itemslocal[12])

        list_price.append(200)
        list_price.append(10)


    if type == 13:
        if(tech_list[type-1]):
            await ctx.send("Технология уже изучена")
            return 0


    if type == 14:
        if(tech_list[type-1]):
            await ctx.send("Технология уже изучена")
            return 0

        list_res.append(db.itemslocal[10])

        list_price.append(100)

    if type == 15:
        if(tech_list[type-1]):
            await ctx.send("Технология уже изучена")
            return 0

        list_res.append(db.itemslocal[11])

        list_price.append(100)

    if type == 16:
        if(tech_list[type-1]):
            await ctx.send("Технология уже изучена")
            return 0

        list_res.append(db.itemslocal[10])

        list_price.append(200)


    if type == 17:
        if(tech_list[type-1]):
            await ctx.send("Технология уже изучена")
            return 0

        list_res.append(db.itemslocal[9])
        list_res.append(db.itemslocal[4])

        list_price.append(200)
        list_price.append(1500)

    if type == 18:
        if(tech_list[type-1]):
            await ctx.send("Технология уже изучена")
            return 0

        list_res.append(db.itemslocal[10])
        list_res.append(db.itemslocal[4])

        list_price.append(300)
        list_price.append(3000)


    if type == 19:
        if(tech_list[type-1]):
            await ctx.send("Технология уже изучена")
            return 0

        list_res.append(db.itemslocal[11])
        list_res.append(db.itemslocal[4])

        list_price.append(100)
        list_price.append(5000)

    if type == 20:
        if(tech_list[type-1]):
            await ctx.send("Технология уже изучена")
            return 0

        list_res.append(db.itemslocal[10])
        list_res.append(db.itemslocal[4])

        list_price.append(80)
        list_price.append(4000)


    if type == 21:
        if(tech_list[type-1]):
            await ctx.send("Технология уже изучена")
            return 0

        list_res.append(db.itemslocal[10])
        list_res.append(db.itemslocal[4])

        list_price.append(400)
        list_price.append(3000)

    if type == 22:
        if(tech_list[type-1]):
            await ctx.send("Технология уже изучена")
            return 0

        list_res.append(db.itemslocal[13])
        list_res.append(db.itemslocal[18])

        list_price.append(100)
        list_price.append(10)

    if type == 23:
        if(tech_list[type-1]):
            await ctx.send("Технология уже изучена")
            return 0

        list_res.append(db.itemslocal[9])

        list_price.append(250)

    if type == 24:
        if(tech_list[type-1]):
            await ctx.send("Технология уже изучена")
            return 0

        list_res.append(db.itemslocal[10])

        list_price.append(300)

    if type == 25:
        if(tech_list[type-1]):
            await ctx.send("Технология уже изучена")
            return 0

        list_res.append(db.itemslocal[11])

        list_price.append(500)

    if type == 26:
        if(tech_list[type-1]):
            await ctx.send("Технология уже изучена")
            return 0

        list_res.append(db.itemslocal[11])

        list_price.append(300)


    if type == 27:
        if(tech_list[type-1]):
            await ctx.send("Технология уже изучена")
            return 0

        list_res.append(db.itemslocal[11])

        list_price.append(350)


    if type == 28:
        if(tech_list[type-1]):
            await ctx.send("Технология уже изучена")
            return 0

        list_res.append(db.itemslocal[11])

        list_price.append(400)


    if type == 29:
        if(tech_list[type-1]):
            await ctx.send("Технология уже изучена")
            return 0

        list_res.append(db.itemslocal[11])

        list_price.append(400)


    if type == 30:
        if(tech_list[type-1]):
            await ctx.send("Технология уже изучена")
            return 0

        list_res.append(db.itemslocal[11])

        list_price.append(500)


    if type == 31:
        if(tech_list[type-1]):
            await ctx.send("Технология уже изучена")
            return 0

        list_res.append(db.itemslocal[10])

        list_price.append(200)

    if type == 32:
        if(tech_list[type-1]):
            await ctx.send("Технология уже изучена")
            return 0

        list_res.append(db.itemslocal[10])

        list_price.append(300)


    if type == 33:
        if(tech_list[type-1]):
            await ctx.send("Технология уже изучена")
            return 0

        list_res.append(db.itemslocal[10])

        list_price.append(400)

    if type == 34:
        if(tech_list[type-1]):
            await ctx.send("Технология уже изучена")
            return 0

        list_res.append(db.itemslocal[10])

        list_price.append(250)


    if type == 35:
        if(tech_list[type-1]):
            await ctx.send("Технология уже изучена")
            return 0

        list_res.append(db.itemslocal[10])

        list_price.append(450)


    if type == 36:
        if(tech_list[type-1]):
            await ctx.send("Технология уже изучена")
            return 0

        list_res.append(db.itemslocal[9])

        list_price.append(400)


    if type == 37:
        if(tech_list[type-1]):
            await ctx.send("Технология уже изучена")
            return 0

        list_res.append(db.itemslocal[9])

        list_price.append(500)

    if type == 38:
        if(tech_list[type-1]):
            await ctx.send("Технология уже изучена")
            return 0

        list_res.append(db.itemslocal[9])

        list_price.append(600)

    # Функция проверки может ли игрок позволить себе заказ
    def check_price(player, list_res, list_price):
        last_Turn = db.get_turn(player, 'общий')
        for i in range(len(list_res)):
            if(db.get_res(player, 'общий', last_Turn, list_res[i]) < list_price[i]):
                return 0
        return 1

    # Проверяем, достаточно ли ресурсов
    if(not(check_price(user, list_res, list_price))):
        await ctx.send('Недостаточно ресурсов')
        return   

    if((type <= 25)and(type >= 1)):
        if type == 22:
            db.set_process(user, type + 100, 0, 1, last_turn+1)
        else:
            db.set_process(user, type + 100, 0, 1, last_turn+5)
    if type <= 30 and type >= 26:
        db.set_process(user, type + 100, 0, 1, last_turn+3)
    if type <= 35 and type >= 31:
        db.set_process(user, type + 100, 0, 1, last_turn+4)
    if type <= 38 and type >= 36:
        db.set_process(user, type + 100, 0, 1, last_turn+6)

    # Снимаем цену
    for i in range(len(list_res)):
        db.set_res(user, 'общий', last_turn, list_res[i], db.get_res(user, 'общий', last_turn, list_res[i]) - list_price[i])

    # Сообщение о успехе
    await ctx.send("Всё прошло успешно")
    
async def getManageGarbMenu(ctx, bot):
    user = ctx.message.author.id

    last_turn = db.get_turn(user, 'общий')

    garb_list = []

    for i in range(6):
        garb_list.append(int(db.get_income(user, 'общий', last_turn, db.itemslocal[i+43]) / 40))

    garb_list.append(int(db.get_income(user, 'общий', last_turn, db.itemslocal[59]) / 40))

    garb_all = db.get_ship(user, 'общий', last_turn, db.itemslocal[20])

    garb_free = garb_all

    for i in range(7):
        garb_free -= garb_list[i]

    garb_list.append(garb_free)

    #   Информация
    embed1 = discord.Embed(title = 'Ваши мусорщики', description=f"Общее количество: {garb_all}", colour=0x008b)

    embed1.add_field(name = f"1. На добыче {res['zelezo']}", value = f"{garb_list[0]}", inline=True)
    embed1.add_field(name = f"2. На добыче {res['zest']}", value = f"{garb_list[1]}", inline=True)
    embed1.add_field(name = f"3. На добыче {res['titan']}", value = f"{garb_list[2]}", inline=True)
    embed1.add_field(name = f"4. На добыче {res['volst']}", value = f"{garb_list[3]}", inline=True)
    embed1.add_field(name = f"5. На добыче {res['gugol']}", value = f"{garb_list[4]}", inline=True)
    embed1.add_field(name = f"6. На добыче {res['gas']}", value = f"{garb_list[5]}", inline=True)
    embed1.add_field(name = f"7. На добыче {res['moh']}", value = f"{garb_list[6]}", inline=True)
    embed1.add_field(name = f"8. Свободны", value = f"{garb_free}", inline=True)

    await ctx.send(embed = embed1)

    await ctx.send("Если вы хотите переместить мусорщики - отправьте номер группы, откуда вы хотите их переместить")

    # Ожидаем ввод точки A
    check = lambda m: m.author == ctx.author and m.channel == ctx.channel
    try:
        pointA = await bot.wait_for('message', check=check, timeout=15)
    except asyncio.TimeoutError:
        await ctx.send('Команда перемещения отменена. Время вышло')
        return

    # Преобразование типа, для дальнейшей работы
    try:
        pointA = int(pointA.clean_content)
    except ValueError:
        await ctx.send('Команда перемещения отменена(Введено не число)')
        return

    if(not((pointA >= 1)and(pointA <= 8))):
        await ctx.send('Команда перемещения отменена(Число выходит за границы)')
        return

    await ctx.send("Отправьте номер группы куда вы хотите их переместить")

    # Ожидаем ввод точки B
    try:
        pointB = await bot.wait_for('message', check=check, timeout=15)
    except asyncio.TimeoutError:
        await ctx.send('Команда перемещения отменена. Время вышло')
        return

    # Преобразование типа, для дальнейшей работы
    try:
        pointB = int(pointB.clean_content)
    except ValueError:
        await ctx.send('Команда перемещения отменена(Введено не число)')
        return
    
    if(not((pointB >= 1)and(pointB <= 8))):
        await ctx.send('Команда перемещения отменена(Число выходит за границы)')
        return

    if(pointB == 8):
        await ctx.send('Команда перемещения отменена(Нельзя освободить мусорщики)')
        return

    await ctx.send("Отправьте количество")

    # Ожидаем ввод count
    try:
        count = await bot.wait_for('message', check=check, timeout=15)
    except asyncio.TimeoutError:
        await ctx.send('Команда перемещения отменена. Время вышло')
        return

    # Преобразование типа, для дальнейшей работы
    try:
        count = int(count.clean_content)
    except ValueError:
        await ctx.send('Команда перемещения отменена(Введено не число)')
        return

    if(not((count > 0) and (count <= garb_list[pointA-1]))):
        await ctx.send('Команда перемещения отменена(Число либо меньше 0, либо больше доступных в группе кораблей)')
        return

    if(not(pointA == 8)):
        if(not(pointA == 7)):
            db.set_income(user, 'общий', last_turn, db.itemslocal[pointA+42], (garb_list[pointA-1]-count)*40)
        else:
            db.set_income(user, 'общий', last_turn, db.itemslocal[59], (garb_list[pointA-1]-count)*40)
    
    if(not(pointB == 7)):
        db.set_income(user, 'общий', last_turn, db.itemslocal[pointB+42], (garb_list[pointB-1]+count)*40)
    else:
        db.set_income(user, 'общий', last_turn, db.itemslocal[59], (garb_list[pointB-1]+count)*40)

async def getManageRockMenu(ctx, bot):
    user = ctx.message.author.id

    last_turn = db.get_turn(user, 'общий')

    rock_list = []

    for i in range(4):
        rock_list.append(int(db.get_income(user, 'общий', last_turn, db.itemslocal[i+50]) / 4))

    rock_all = db.get_ship(user, 'общий', last_turn, db.itemslocal[21])

    rock_free = rock_all

    for i in range(4):
        rock_free -= rock_list[i]

    rock_list.append(rock_free)

    #   Информация
    embed1 = discord.Embed(title = 'Ваши каменьщики', description=f"Общее количество: {rock_all}", colour=0x008b)

    embed1.add_field(name = f"1. На добыче {res['kamen1']}", value = f"{rock_list[0]}", inline=True)
    embed1.add_field(name = f"2. На добыче {res['kamen2']}", value = f"{rock_list[1]}", inline=True)
    embed1.add_field(name = f"3. На добыче {res['kamen3']}", value = f"{rock_list[2]}", inline=True)
    embed1.add_field(name = f"4. На добыче {res['kamen4']}", value = f"{rock_list[3]}", inline=True)
    embed1.add_field(name = f"5. Свободны", value = f"{rock_free}", inline=True)

    await ctx.send(embed = embed1)

    await ctx.send("Если вы хотите переместить каменьщики - отправьте номер группы, откуда вы хотите их переместить")

    # Ожидаем ввод точки A
    check = lambda m: m.author == ctx.author and m.channel == ctx.channel
    try:
        pointA = await bot.wait_for('message', check=check, timeout=15)
    except asyncio.TimeoutError:
        await ctx.send('Команда перемещения отменена. Время вышло')
        return

    # Преобразование типа, для дальнейшей работы
    try:
        pointA = int(pointA.clean_content)
    except ValueError:
        await ctx.send('Команда перемещения отменена(Введено не число)')
        return

    if(not((pointA >= 1)and(pointA <= 5))):
        await ctx.send('Команда перемещения отменена(Число выходит за границы)')
        return

    await ctx.send("Отправьте номер группы куда вы хотите их переместить")

    # Ожидаем ввод точки B
    try:
        pointB = await bot.wait_for('message', check=check, timeout=15)
    except asyncio.TimeoutError:
        await ctx.send('Команда перемещения отменена. Время вышло')
        return

    # Преобразование типа, для дальнейшей работы
    try:
        pointB = int(pointB.clean_content)
    except ValueError:
        await ctx.send('Команда перемещения отменена(Введено не число)')
        return
    
    if(not((pointB >= 1)and(pointB <= 5))):
        await ctx.send('Команда перемещения отменена(Число выходит за границы)')
        return

    if(pointB == 5):
        await ctx.send('Команда перемещения отменена(Нельзя освободить каменьщики)')
        return

    await ctx.send("Отправьте количество")

    # Ожидаем ввод count
    try:
        count = await bot.wait_for('message', check=check, timeout=15)
    except asyncio.TimeoutError:
        await ctx.send('Команда перемещения отменена. Время вышло')
        return

    # Преобразование типа, для дальнейшей работы
    try:
        count = int(count.clean_content)
    except ValueError:
        await ctx.send('Команда перемещения отменена(Введено не число)')
        return

    if(not((count > 0) and (count <= rock_list[pointA-1]))):
        await ctx.send('Команда перемещения отменена(Число либо меньше 0, либо больше доступных в группе кораблей)')
        return

    if(not(pointA == 5)):
        db.set_income(user, 'общий', last_turn, db.itemslocal[pointA+49], (rock_list[pointA-1]-count)*4)

    db.set_income(user, 'общий', last_turn, db.itemslocal[pointB+49], (rock_list[pointB-1]+count)*4)