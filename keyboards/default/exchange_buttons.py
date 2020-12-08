from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

markup = ReplyKeyboardMarkup(resize_keyboard=True,
                               keyboard=[
                                   [
                                       KeyboardButton(text="USD")
                                   ],
                                   [
                                       KeyboardButton(text="EUR")
                                   ],
                                   [
                                       KeyboardButton(text="RUB")
                                   ]
                               ])