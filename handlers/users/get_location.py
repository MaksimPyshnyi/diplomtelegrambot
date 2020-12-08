from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.default import location_button
from loader import dp

@dp.message_handler(Command("show_on_map"))
async def show_on_map(message: types.Message):
    await message.answer(f"Здравствуйте, {message.from_user.full_name}.\n"
                         f"Нажав на кнопку ниже, можно отправить текущую геолокацию нашему боту!", reply_markup=location_button.keyboard)
