# from aiogram import types
# from aiogram.dispatcher.filters.builtin import CommandStart
#
# from loader import dp
#
#
# @dp.message_handler(CommandStart())
# async def bot_start(message: types.Message):
#     await message.answer(f'Привет, {message.from_user.full_name}! '
#                          f'Жми /menu')


import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
    except sqlite3.IntegrityError as err:
        print(err)
    count = db.count_users()[0]
    await message.answer(
        "\n".join(
            [
                f'Привет, {message.from_user.full_name}!',
                f'Ты был занесен в базу',
                f'В базе <b>{count}</b> пользователей',
                f'Чтобы добавить в базу свой эмейл необходимо ввести команду /email',
                f'Чтобы посмотреть справку со всеми доступными командами можно ввести команду /help',
            ]))