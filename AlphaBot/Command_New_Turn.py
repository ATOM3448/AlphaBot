import asyncio
import discord
import System_DataActions as db
from System_Resource import res


async def goNext(ctx):
    user = ctx.message.author.id

# Проверить процессы

    # Сохраняем последний ход
    last_turn = db.get_turn(user, 'общий')

    # Добавляем ход
    db.add_turn(user, 'общий', last_turn+1)

    # Сохраняем новый ход
    new_turn = db.get_turn(user, 'общий')

    # Заносим данные ресурсов
    for j in range(19):
            db.set_res(user, 'общий', new_turn, db.itemslocal[j+1], db.get_res(user, 'общий', last_turn, db.itemslocal[j+1]) + db.get_income(user, 'общий', last_turn, db.itemslocal[j+43]))
            db.set_income(user, 'общий', new_turn, db.itemslocal[j+43], db.get_income(user, 'общий', last_turn, db.itemslocal[j+43]))

    # Заносим данные кораблей
    for j in range(23):
        db.set_ship(user, 'общий', new_turn, db.itemslocal[j+20], db.get_ship(user, 'общий', last_turn, db.itemslocal[j+20]))

    # Забираем завершенные процессы
    complite_process = db.get_process(user, new_turn)

    for i in complite_process:
        if ((i[0] >= 20) and (i[0] <= 41)):
            db.set_ship(user, 'общий', new_turn, db.itemslocal[i[0]], db.get_ship(user, 'общий', last_turn, db.itemslocal[i[0]]) + i[2])
        if ((i[0] >= 101) and (i[0] <= 138)):
            db.set_tech(user, db.tech_list[i[0]-101], True)
    
    await ctx.send("Всё прошло успешно")
