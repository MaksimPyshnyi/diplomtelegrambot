from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

choice = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text="🗞 TUT.BY",
                                          callback_data="tut-by"
                                      ),
                                      InlineKeyboardButton(
                                          text="📰 Onliner",
                                          callback_data="onliner"
                                      )
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text="⚽️ Sportarena",
                                          callback_data="sportarena"
                                      ),
                                      InlineKeyboardButton(
                                          text="🏀 Pressball",
                                          callback_data="pressball"
                                      )
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text="🌤 POGODA.BY",
                                          callback_data="pogoda"
                                      ),
                                      InlineKeyboardButton(
                                          text="☀️ Gismeteo",
                                          callback_data="gismeteo"
                                      )
                                  ],
                                  [
                                        InlineKeyboardButton(
                                            text="Отмена",
                                            callback_data="cancel"
                                        )
                                  ]
                              ])



tut_by_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Смотреть тут", url="https://www.tut.by")
    ]
])
onliner_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Смотреть тут", url="https://www.onliner.by")
    ]
])

sportarena_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Смотреть тут", url="https://sportarena.by/")
    ]
])
pressball_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Смотреть тут", url="https://www.pressball.by")
    ]
])

pogoda_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Смотреть тут", url="http://www.pogoda.by")
    ]
])
gismeteo_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Смотреть тут", url="https://www.gismeteo.by/")
    ]
])