from aiogram import types
from aiogram.dispatcher.filters import Command
from loader import dp, bot
from data.items import POST_FAST_SHIPPING, POST_REGULAR_SHIPPING, PICKUP_SHIPPING, MacBook_Pro_16, \
    MacBook_Pro_13


@dp.message_handler(Command("invoices"))
async def show_invoices(message: types.Message):
    await bot.send_invoice(chat_id=message.from_user.id,
                           **MacBook_Pro_16.generate_invoice(),
                           payload="123456")
    await bot.send_invoice(chat_id=message.from_user.id,
                           **MacBook_Pro_13.generate_invoice(),
                           payload="123457")


@dp.shipping_query_handler()
async def choose_shipping(query: types.ShippingQuery):
    if query.shipping_address.country_code == "BY":
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        shipping_options=[POST_FAST_SHIPPING, POST_REGULAR_SHIPPING, PICKUP_SHIPPING],
                                        ok=True)
    elif query.shipping_address.country_code == "US":
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        ok=False,
                                        error_message="Сюда не доставляем")
    else:
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        shipping_options=[POST_REGULAR_SHIPPING],
                                        ok=True)


@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query_id=pre_checkout_query.id,
                                        ok=True)
    await bot.send_message(chat_id=pre_checkout_query.from_user.id,
                           text="Спасибо за покупку! Ожидайте отправку")