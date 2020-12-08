
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.choice_buttons import choice, tut_by_keyboard, onliner_keyboard, sportarena_keyboard, \
    pressball_keyboard, pogoda_keyboard, gismeteo_keyboard
from loader import dp

@dp.message_handler(Command("items"))
async def show_items(message: types.Message):
    await message.answer(text="С помощью данного меню можно посмотреть актуальные новоти Беларуси на самых популярных порталах \n"
                              "Если вам ничего не нужно - жмите отмену",
                         reply_markup=choice)


@dp.callback_query_handler(text="tut-by")
async def exchange_eur(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("Вы выбрали посмотреть новости на TUT.BY",
                              reply_markup=tut_by_keyboard)


@dp.callback_query_handler(text="onliner")
async def exchange_eur(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("Вы выбрали посмотреть новости на ONLINER",
                              reply_markup=onliner_keyboard)

@dp.callback_query_handler(text="sportarena")
async def exchange_eur(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("Вы выбрали посмотреть новости спорта на Sportarena",
                              reply_markup=sportarena_keyboard)


@dp.callback_query_handler(text="pressball")
async def exchange_eur(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("Вы выбрали посмотреть новости спорта на Pressball",
                              reply_markup=pressball_keyboard)

@dp.callback_query_handler(text="pogoda")
async def exchange_eur(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("Вы выбрали посмотреть прогноз погоды на POGODA.BY",
                              reply_markup=pogoda_keyboard)


@dp.callback_query_handler(text="gismeteo")
async def exchange_eur(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("Вы выбрали посмотреть прогноз погоды на Gismeteo",
                              reply_markup=gismeteo_keyboard)


@dp.callback_query_handler(text="cancel")
async def cancel(call: CallbackQuery):
    await call.answer("Вы закрыли новостной саджест!", show_alert=True)
    await call.message.edit_reply_markup(reply_markup=None)
