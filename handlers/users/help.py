from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from utils.misc import rate_limit


@rate_limit(5, 'help')
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = [
        'Список команд: ',
        '/start - Начать тестовый диалог',
        '/items - Просмотр актуальных новостей',
        '/exchange - Курсы валют',
        '/invoices - Осуществляем тестовый платеж',
        '/show_on_map - Моя геопозиия',
        '/help - Получить справку'
    ]
    await message.answer('\n'.join(text))