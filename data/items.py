from aiogram import types
from aiogram.types import LabeledPrice


from utils.misc.item import Item

MacBook_Pro_16 = Item(
    title="Apple MacBook Pro 16 2019",
    description="Apple MacBook Pro 16 - 16.0 3072x1920 IPS, Intel Core i7 9750H 2600 МГц, 16 ГБ, SSD 512 ГБ, граф. адаптер: AMD Radeon Pro 5300M 4ГБ, Mac OS, цвет крышки серый",
    currency="USD",
    prices=[
        LabeledPrice(
            label="Apple MacBook Pro 16 2019",
            amount=29_00_00
        )
    ],
    start_parameter="create_invoice_macbook_pro_16",
    photo_url="https://content2.onliner.by/catalog/device/main@2/db499f52fa0d4b9c31fd30231359b4c1.jpeg"
)

MacBook_Pro_13 = Item(
    title="Apple MacBook Pro 13 Touch Bar 2020",
    description="Apple MacBook Pro 13 Touch Bar 2020 — 13.3 2560 x 1600 IPS, Intel Core i5 8257U 1400 МГц, 8 ГБ, SSD 256 ГБ, граф. адаптер: встроенный, Mac OS, цвет крышки серый",
    currency="USD",
    prices=[
        LabeledPrice(
            label="Apple MacBook Pro 13 Touch Bar 202",
            amount=17_00_00
        ),
        LabeledPrice(
            label="Доставка",
            amount=10_00
        ),
        LabeledPrice(
            label="Скидка",
            amount=-30_00
        ),
        LabeledPrice(
            label="НДС",
            amount=30_00
        ),
    ],
    need_shipping_address=True,
    start_parameter="create_invoice_macbook_pro_13",
    photo_url="https://content2.onliner.by/catalog/device/main@2/8b2f2c3c18c6102c0537aaf5cea17561.jpeg",
    photo_size=600,
    is_flexible=True
)

POST_REGULAR_SHIPPING = types.ShippingOption(
    id='post_reg',
    title='Почтой',
    prices=[
        types.LabeledPrice(
            'Обычная коробка', 0),
        types.LabeledPrice(
            'Почтой обычной', 10_00),
    ]
)
POST_FAST_SHIPPING = types.ShippingOption(
    id='post_fast',
    title='Почтой (vip)',
    prices=[
        types.LabeledPrice(
            'Супер прочная коробка', 10_00),
        types.LabeledPrice(
            'Почтой срочной - DHL (3 дня)', 30_00),
    ]
)

PICKUP_SHIPPING = types.ShippingOption(id='pickup',
                                       title='Самовывоз',
                                       prices=[
                                           types.LabeledPrice('Самовывоз из магазина', -10_00)
                                       ])