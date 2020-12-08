from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("invoices", "Совершить тестовый платеж"),
        types.BotCommand("items", "Посмотреть новости Беларуси"),
        types.BotCommand("exchange", "Посмотреть курсы валют"),
        types.BotCommand("help", "Посмотреть справку"),
        types.BotCommand("show_on_map", "Показать мою геолокацию"),
    ])