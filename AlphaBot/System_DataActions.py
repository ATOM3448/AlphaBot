import sqlite3
import os

itemsnormal = [
                'Ход',                          #1
                'Железо',                       #2
                'Жесть',                        #3
                'Титан',                        #4
                'Волст',                        #5
                'Гуголь',                       #6
                'Газ',                          #7
                'Энергия',                      #8
                'Камень1',                      #9
                'Камень2',                      #10
                'Камень3',                      #11
                'Камень4',                      #12
                'Сверол',                       #13
                'Релик',                        #14
                'Вода',                         #15
                'Микробот',                     #16
                'Мох',                          #17
                'Соль',                         #18
                'Антивещество',                 #19
                'Нано',                         #20
                'Мусорщик',                     #21
                'Каменьщик',                    #22
                'Легкий_Верфятник',             #23
                'Истребитель_Капля',            #24
                'Каравелла',                    #25
                'Средний_Верфятник',            #26
                'Галера_Конкистадоров',         #27
                'Фрегат_Конкистадоров',         #28
                'Линкор_Конкистадоров',         #29
                'Тяжёлый_Верфятник',            #30
                'Погибель',                     #31
                'Корсар',                       #32
                'Бомбандир',                    #33
                'Браконьер',                    #34
                '★Серая_Шляпа★',               #35
                '★Красный_Шарф★',              #36
                '★Чёрная_Перчатка★',           #37
                '★Синий_Сапог★',               #38
                'Станиця',                      #39
                'Научное_судно',                #40
                'Вахтер',                       #41
                'СоляристT',                    #42
                '★Отцовский_Корабль★',         #43
                'Доход железа',                 #44
                'Доход жести',                  #45
                'Доход титана',                 #46
                'Доход волста',                 #47
                'Доход гугля',                  #48
                'Доход газа',                   #49
                'Доход энергии',                #50
                'Доход камня1',                 #51
                'Доход камня2',                 #52
                'Доход камня3',                 #53
                'Доход камня4',                 #54
                'Доход сверола',                #55
                'Доход релика',                 #56
                'Доход воды',                   #57
                'Доход населения',              #58
                'Доход микроботов',             #59
                'Доход моха',                   #60
                'Доход соли',                   #61
                'Доход антивещества',           #62
                'Доход нано'                    #63
            ]

itemslocal =  [
                'Turn',
                'zelezo',
                'zest',
                'titan',
                'volst',
                'gugol',
                'gas',
                'energy',
                'kamen1',
                'kamen2',
                'kamen3',
                'kamen4',
                'sverol',
                'relik',
                'voda',
                'mikrobot',
                'moh',
                'sol',
                'antivec',
                'nano',
                'Мусорщик',
                'Каменьщик',
                'Легкий_Верфятник',
                'Истребитель_Капля',
                'Каравелла',
                'Средний_Верфятник',
                'Галера_Конкистадоров',
                'Фрегат_Конкистадоров',
                'Линкор_Конкистадоров',
                'Тяжёлый_Верфятник',
                'Погибель',
                'Корсар',
                'Бомбандир',
                'Браконьер',
                '★Серая_Шляпа★',
                '★Красный_Шарф★',
                '★Чёрная_Перчатка★',
                '★Синий_Сапог★',
                'Станиця',
                'Научное_судно',
                'Вахтер',
                'СоляристT',
                '★Отцовский_Корабль★',
                'income_of_zelezo',
                'income_of_zest',
                'income_of_titan',
                'income_of_volst',
                'income_of_gugol',
                'income_of_gas',
                'income_of_energy',
                'income_of_kamen1',
                'income_of_kamen2',
                'income_of_kamen3',
                'income_of_kamen4',
                'income_of_sverol',
                'income_of_relik',
                'income_of_voda',
                'income_of_naselenie',
                'income_of_mikrobotT',
                'income_of_moh',
                'income_of_sol',
                'income_of_antivec',
                'income_of_nano'
                ]

tech_list = [
                'Кинетические_ядра',        #1
                'Заряженные_ядра',          #2
                'Плазменные_ядра',          #3
                'Нейтронные_ядра',          #4
                'Жёлтый_луч',               #5
                'Алый_луч',                 #6
                'Тёмный_луч',               #7
                'Обычная_броня',            #8
                'Заряженная_броня',         #9
                'Алая_броня',               #10
                'Тёмная_броня',             #11
                'Грави_броня',              #12
                'Звёздные_паруса',          #13
                'Алые_паруса',              #14
                'Тёмные_паруса',            #15
                'Двигатель_Тёмной_энергии', #16
                'Транспортный_канал',       #17
                'Убежище',                  #18
                'Транспортные_кольца',      #19
                'Насморк',                  #20
                'Тугие_сплавы',             #21
                '★Солнечная_Эра★',         #22
                'Каменистые',               #23
                'Второй_слой',              #24
                'Природные_способности',    #25
                'Алые',                     #26
                'Лучевая_болезнь',          #27
                'Импульсивная_броня',       #28
                'Алое_пламя',               #29
                'Алые_камни',               #30
                'Тёмные',                   #31
                'Чёрная_метка',             #32
                'Вылазка',                  #33
                'Проникновение',            #34
                'Тёмные_силы',              #35
                'Синие',                    #36
                'Синий_луч',                #37
                'Совмещение',               #38
            ]

def get_db(player):

    path = 'System_UsersData'
    directory = os.listdir(path)

    for i in range(len(directory)):
        if str(player) in directory[i]:
            db_name = directory[i]
    db = sqlite3.connect(f'System_UsersData/{db_name}')
    return db

# Получение хода
def get_turn(player, where):

    db = get_db(player)
    cursor = db.cursor()

    result = cursor.execute(f"""SELECT max(Turn) FROM  {where}""")

    request = []
    for i in result:
        request.append(*i)

    db.commit()
    db.close()

    if(request[0] == None):
        return 0

    return request[0]

# Добавление хода
def add_turn(player, where, turn):

    db = get_db(player)
    cursor = db.cursor()   

    cursor.execute(f"""INSERT INTO {where} (Turn) VALUES ({turn})""") 

    db.commit()
    db.close()

# Получение конкретного ресурса в конкретной табличке на конкрентом ходу
def get_res(player, where, turn, res):
    db = get_db(player)
    cursor = db.cursor()

    result = cursor.execute(f"""SELECT {res} FROM {where} WHERE Turn={turn}""")
    
    request = []
    for i in result:
        request.append(*i)

    db.commit()
    db.close()

    if(request[0] == None):
        return 0

    return request[0]

# Вставка конкретного ресурса в конкретной табличке на конкретном ходу
def set_res(player, where, turn, res, value):

    db = get_db(player)
    cursor = db.cursor()   

    cursor.execute(f"""UPDATE {where} SET {res} = {value} WHERE Turn = {turn}""") 

    db.commit()
    db.close()

# Получение ресурсов без названий в конкретной табличке на конкретном ходу
def get_all_res_nn(player, where, turn):

    db = get_db(player)
    cursor = db.cursor()

    cursor.execute(f""" SELECT * FROM {where} WHERE Turn = {turn}""")
    data = cursor.fetchall()

    request = []
    for i in range(1, 20):
           request.append(data[0][i])

    db.commit()
    db.close()

    return request

# Получение всех ресурсов в конкретной табличке на конкретном ходу
def get_all_res(player, where, turn):

    db = get_db(player)
    cursor = db.cursor()

    cursor.execute(f""" SELECT * FROM {where} WHERE Turn={turn}""")
    data = cursor.fetchall()

    request = []
    for i in range(1, 20):
        request.append(str(itemsnormal[i]) + ' - ' + str(data[0][i]))


    db.commit()
    db.close()

    return request

# Получение конкретного корабля в конкретной табличке на конкретном ходу
def get_ship(player, where, turn, ship):

    db = get_db(player)
    cursor = db.cursor()

    result = cursor.execute(f"""SELECT {ship} FROM  {where} WHERE Turn={turn}""")
    
    request = []
    for i in result:
        request.append(*i)

    db.commit()
    db.close()

    if(request[0] == None):
        return 0

    return request[0]

# Вставка конкретного корабля в конкретной табличке
def set_ship(player, where, turn, ship, value):

    db = get_db(player)
    cursor = db.cursor()   
 
    cursor.execute(f"""UPDATE {where} SET {ship} = {value} WHERE Turn = {turn}""") 

    db.commit()
    db.close()

# Получение кораблей без названий в конкретной табличке на конкретном ходу
def get_all_ship_nn(player, where, turn):

    db = get_db(player)
    cursor = db.cursor()

    cursor.execute(f""" SELECT * FROM {where} WHERE Turn = {turn}""")
    data = cursor.fetchall()

    request = []
    for i in range(20, 43):
           request.append(data[0][i])

    db.commit()
    db.close()

    return request

# Получение всех кораблей в конкретной табличке на конкретном ходу
def get_all_ship(player, where, turn):

    db = get_db(player)
    cursor = db.cursor()

    cursor.execute(f""" SELECT * FROM {where} WHERE Turn={turn}""")
    data = cursor.fetchall()

    request = []
    for i in range(20, 43):
        request.append(str(itemsnormal[i]) + ' - ' + str(data[0][i]))

    db.commit()
    db.close()

    return request

# Получение прибыли конкретного ресурса в конкретной табличке на конкретном ходу
def get_income(player, where, turn, income):

    db = get_db(player)
    cursor = db.cursor()

    result = cursor.execute(f"""SELECT {income} FROM  {where} WHERE Turn={turn}""")
    
    request = []
    for i in result:
        request.append(*i)

    db.commit()
    db.close()

    if(request[0] == None):
        return 0

    return request[0]

# Вставка прибыли конкретного ресурса в конкретной табличке на конкретном ходу
def set_income(player, where, turn, income, value):

    db = get_db(player)
    cursor = db.cursor()   
 
    cursor.execute(f"""UPDATE {where} SET {income} = {value} WHERE Turn = {turn}""") 

    db.commit()
    db.close()

# Получение прибыли ресурсов без названий в конкретной табличке на конкретном ходу
def get_all_income_nn(player, where, turn):

    db = get_db(player)
    cursor = db.cursor()

    cursor.execute(f""" SELECT * FROM {where} WHERE Turn = {turn}""")
    data = cursor.fetchall()

    request = []
    for i in range(43, 63):
           request.append(data[0][i])

    db.commit()
    db.close()

    return request

# Получение всей прибыли ресурсов в конкретной табличке на конкретном ходу
def get_all_income(player, where, turn):

    db = get_db(player)
    cursor = db.cursor()

    cursor.execute(f""" SELECT * FROM {where} WHERE Turn={turn}""")
    data = cursor.fetchall()

    request = []
    for i in range(43, 63):
        request.append(str(itemsnormal[i]) + ' - ' + str(data[0][i]))

    db.commit()
    db.close()

    return request

# Вставка процесса
def set_process(player, type, wight, count, turn):
    db = get_db(player)
    cursor = db.cursor()   

    cursor.execute(f"""INSERT INTO things_in_the_process VALUES ({type}, {wight}, {count}, {turn})""") 

    db.commit()
    db.close()

# Получение всех процессов с завершением на конкретный ход
def get_process(player, turn):
    db = get_db(player)
    cursor = db.cursor()

    cursor.execute(f"""SELECT * FROM things_in_the_process WHERE Completion_turn = {turn}""")
    data = cursor.fetchall()

    request = [][2]
    for i in range(len(data)):
        request.append()
        request[i][0] = data[i][0]
        request[i][1] = data[i][2]

    db.commit()
    db.close()

    return request

# Получение количества всех активных процессов одного веса
def get_active_process_w(player, turn, wight):
    db = get_db(player)
    cursor = db.cursor()

    cursor.execute(f"""SELECT * FROM things_in_the_process WHERE Completion_turn > {turn} AND Wight = {wight}""")

    data = cursor.fetchall()

    request = 0
    for i in range(len(data)):
        request += data[i][2]

    db.commit()
    db.close()

    return request

# Получение максимального количества процессов одного веса для кораблей
def get_max_process_c(player, turn, wight):
    result = 0
    if(wight == 1):
        result = 4*get_ship(player, 'общий', turn, itemslocal[22])
    if(wight == 2):
        result = 2*get_ship(player, 'общий', turn, itemslocal[25])
    if(wight == 3):
        result = 1*get_ship(player, 'общий', turn, itemslocal[29])
    if(wight == 4):
        result = 10*get_ship(player, 'общий', turn, itemslocal[38]) + 10
    return result
    
# Получение данных технологий в процессе
def get_tech_in_process(player, turn):
    db = get_db(player)
    cursor = db.cursor()

    cursor.execute(f"""SELECT * FROM things_in_the_process WHERE Completion_turn > {turn} AND Wight = 0""")

    data = cursor.fetchall()

    request = data[0]

    db.commit()
    db.close()

    return request

# Получить все технологии игрока
def get_all_tech(player):
    db = get_db(player)
    cursor = db.cursor()

    cursor.execute("""SELECT * FROM technologies""")

    data = cursor.fetchall()

    request = data[0]

    db.commit()
    db.close()

    return request
