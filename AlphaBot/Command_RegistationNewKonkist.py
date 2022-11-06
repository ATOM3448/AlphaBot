from System_Config import settingsForSrever as localSet
import sqlite3

async def regKon(self, bot):
    newL = '\n'
    guild = bot.get_guild(localSet['guild'])
    filename = []
    userID = self.user_id
    userName = self.member.display_name

    #запускаем процесс занесения всех планет в список
        #внесение всех планет в Системе 1
    category = guild.get_channel(1024742962246193263)
    for channel in category.channels:
        if(channel.name != 'космос'):
            if(channel.name == 'пояс_астероидов'):
                filename.append(f'{channel.name}_1')
                continue
            filename.append(channel.name)
        else:
            filename.append(f'{channel.name}1')
            
        #внесение всех планет в Системе 2
    category = guild.get_channel(1024743072141152417)
    for channel in category.channels:
        if(channel.name != 'космос'):
            if(channel.name == 'пояс_астероидов'):
                filename.append(f'{channel.name}_2')
                continue
            filename.append(channel.name)
        else:
            filename.append(f'{channel.name}2')
    filename.append('общий')

    #----------
    
    #База данных игрока
    #Таблица на каждую планету
    for fn in filename:
        with sqlite3.connect(f'System_UsersData/Data_of_{userName}({userID}).db') as db:
            cursor = db.cursor()
            cursor.execute(f"""CREATE TABLE IF NOT EXISTS {fn}(
                Turn INT PRIMARY KEY,
                zelezo INT,
                zest INT,
                titan INT,
                vjoblost INT,
                gugol INT,
                gas INT,
                energy INT,
                kamen1 INT,
                kamen2 INT,
                kamen3 INT,
                kamen4 INT,
                sverol INT,
                relik INT,
                voda INT,
                mikrobot INT,
                moh INT,
                sol INT,
                antipizdec INT,
                nanohujna INT,
                Мусорщик INT,
                Каменьщик INT,
                Легкий_Верфятник INT,
                Истребитель_Капля INT,
                Каравелла INT,
                Средний_Верфятник INT,
                Галера_Конкистадоров INT,
                Фрегат_Конкистадоров INT,
                Линкор_Конкистадоров INT,
                Тяжёлый_Верфятник INT,
                \"Погибель\" INT,
                \"Корсар\" INT,
                \"Бомбандир\" INT,
                \"Браконьер\" INT,
                ★Серая_Шляпа★ INT,
                ★Красный_Шарф★ INT,
                ★Чёрная_Перчатка★ INT,
                ★Синий_Сапог★ INT,
                Станиця INT,
                Научное_судно INT,
                Вахтер INT,
                Солярист INT,
                ★Отцовский_Корабль★ INT,
                income_of_zelezo INT,
                income_of_zest INT,
                income_of_titan INT,
                income_of_vjoblost INT,
                income_of_gugol INT,
                income_of_gas INT,
                income_of_energy INT,
                income_of_kamen1 INT,
                income_of_kamen2 INT,
                income_of_kamen3 INT,
                income_of_kamen4 INT,
                income_of_sverol INT,
                income_of_relik INT,
                income_of_voda INT,
                income_of_naselenie INT,
                income_of_mikrobot INT,
                income_of_moh INT,
                income_of_sol INT,
                income_of_antipizdec INT,
                income_of_nanohujna INT);
                """)

            cursor.execute(f"""INSERT INTO {fn} VALUES(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);""")
            
            db.commit()
    
    
    with sqlite3.connect(f'System_UsersData/Data_of_{userName}({userID}).db') as db:
        
        cursor = db.cursor()

        #Таблица процессов
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS Things_in_the_process(
        Type INT,
        Count INT,
        Completion_turn INT);""")

        db.commit()

        #Таблица технологий
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS technologies(
            Кинетические_ядра BOOL
            Заряженные_ядра BOOL
            Плазменные_ядра BOOL
            Нейтронные_ядра BOOL
            Жёлтый_луч BOOL
            Алый_луч BOOL
            Тёмный_луч BOOL
            Обычная_броня BOOL
            Заряженная_броня BOOL
            Алая_броня BOOL
            Тёмная_броня BOOL
            Грави_броня BOOL
            Звёздные_паруса BOOL
            Алые_паруса BOOL
            Тёмные_паруса BOOL
            Двигатель_\"Тёмной-энергии\" BOOL
            Транспортный_канал BOOL
            Убежище BOOL
            Транспортные_кольца BOOL
            Насморк BOOL
            Тугие-сплавы BOOL
            ★Солнечная-Эра★ BOOL
            ★Серая Шляпа★ BOOL
            Каменистые BOOL
            Второй-слой BOOL
            Природные-способности BOOL
            ★Красный Шарф★ BOOL
            Алые BOOL
            Лучевая-болезнь BOOL
            Импульсивная-броня BOOL
            Алое-пламя BOOL
            Алые-ками BOOL
            ★Чёрная Перчатка★ BOOL
            Тёмные BOOL
            Чёрная-метка BOOL
            Вылазка BOOL
            Проникновение BOOL
            Тёмные-силы BOOL
            ★Синий Сапог★ BOOL
            Синие BOOL
            Синий-луч BOOL
            Совмещение BOOL
            Карабины BOOL
            Новые-гранаты BOOL);
        """)
        db.commit()
    #----------
    