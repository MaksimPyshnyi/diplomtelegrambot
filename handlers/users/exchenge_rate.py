import requests
from aiogram import types
from aiogram.dispatcher.filters import Command

from data import api_nbrb
from keyboards.default.exchange_buttons import markup
from loader import bot

from loader import dp

response = requests.get(api_nbrb.url).json()

@dp.message_handler(Command("exchange"))
async def exchange (message: types.Message):
    await bot.send_message(message.chat.id, "С помощью данного меню можно узнать актуальный курс валют",
                           reply_markup=markup)

    @dp.message_handler()
    async def exchange_rate(message: types.Message):
        try:
            markup = types.ReplyKeyboardRemove(selective=False)

            for coin in response:
                if (message.text == coin['Cur_Abbreviation']):
                    await bot.send_message(message.chat.id, printCoin(coin['Cur_OfficialRate']),
                                     reply_markup=markup, parse_mode="Markdown")

        except Exception as e:
            await bot.reply_to(message, 'ooops!')

    def printCoin(Cur_OfficialRate):
        return "💰 *Актуальный курс:* " + str(Cur_OfficialRate)



