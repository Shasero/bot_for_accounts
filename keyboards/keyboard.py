from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton,
                           ReplyKeyboardMarkup, KeyboardButton)

from aiogram.utils.keyboard import InlineKeyboardBuilder

from database.requests import select_accounts


list = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Аккаунты', callback_data='accounts')]
])


payment_keyboard_one = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Оплата ⭐️', callback_data='stars_one', pay=True)]
], resize_keyboard=True)


payment_keyboard_two = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Оплата ⭐️', callback_data='stars_two', pay=True)]
], resize_keyboard=True)


payment_keyboard_three = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Оплата ⭐️', callback_data='stars_three', pay=True)]
], resize_keyboard=True)


choosing_the_time = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='1 час', callback_data='one_hour')],
    [InlineKeyboardButton(text='2 часа', callback_data='two_hour')],
    [InlineKeyboardButton(text='3 часа', callback_data='three_hour')]
], resize_keyboard=True)


async def select_acc():
    all_acc = await select_accounts()
    keyboard = InlineKeyboardBuilder()
    for acc in all_acc:
        keyboard.add(InlineKeyboardButton(text=acc.game, callback_data=f"select_{acc.game}"))
    return keyboard.adjust(1).as_markup()

