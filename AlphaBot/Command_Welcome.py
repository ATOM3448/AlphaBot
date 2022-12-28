import sqlite3
import os

def get_player(ID):

    path = 'System_UsersData'
    directory = os.listdir(path)

    index = ''
    for i in range(len(directory)):
        if str(ID) in directory[i]:
            index = directory[i]
    
    if index:
        return index

    return 0



async def start_game(ID, name_space):

    db = sqlite3.connect(f'System_UsersData/{get_player(ID)}')
    cursor = db.cursor()

    cursor.execute(f"""SELECT * FROM sqlite_master WHERE type='table';""")
    data = cursor.fetchall()

    for i in range(len(data)):
        if name_space in data[i]:
            cursor.execute(f"""UPDATE {name_space} SET zest = 1000, Мусорщик = 1, ★Отцовский_Корабль★ = 1 WHERE Turn=0""")
            cursor.execute(f"""UPDATE общий SET zest = 1000, Мусорщик = 1, ★Отцовский_Корабль★ = 1 WHERE Turn=0""")
            break

    db.commit()
    db.close()