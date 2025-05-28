from aiogram import Router, html, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message


import keyboards.keyboard as kb
import database.requests as rq


router = Router()


@router.message(CommandStart())
async def start(message: Message, bot: Bot) -> None:
    await rq.set_user(message.from_user.id, message.from_user.full_name)
    await bot.send_message(message.from_user.id, f'''Привет👋 {html.bold(message.from_user.full_name)}!

    Я — бот для аренды игровых аккаунтов! 🎮✨ Здесь ты можешь быстро и безопасно взять топовый аккаунт на время, чтобы играть без лишних хлопот.

    🔹 Большой выбор — от премиум-аккаунтов до редких коллекционных!
    🔹 Гибкие тарифы — арендуй на час, день или неделю.
    🔹 Безопасно — все аккаунты проверены, а платежи защищены.

    Готов к мощному геймплею? Выбирай аккаунт и начинай играть! �💨''', reply_markup=kb.list)
    
