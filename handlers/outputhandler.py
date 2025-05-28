from aiogram import F, Router, Bot, html
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, LabeledPrice, PreCheckoutQuery


import keyboards.keyboard as kb
import database.requests as rq


router = Router()
global_game = None


@router.message(Command(commands='accounts'))
async def command_start_acc(message: Message, bot: Bot):
    if(await rq.proverka_accounts() == None):
        await bot.send_message(message.from_user.id, text='Пока аккаунтов нет')
    else:
        await bot.send_message(message.from_user.id, text='Аккаунты: ', reply_markup=await kb.select_acc())


@router.message(F.data.startswith('accounts'))
async def select_keyboard_accounts(message: Message, bot: Bot):
    if(await rq.proverka_accounts() == None):
        await bot.send_message(message.from_user.id,text='Пока аккаунтов нет')
    else:
        await bot.send_message(message.from_user.id, text='Аккаунты: ', reply_markup=await kb.select_acc())
        

@router.callback_query(F.data.startswith('select_'))
async def get_time_for_game(callback: CallbackQuery):
    await callback.answer('')
    take_game = callback.data.split('_')[1]
    global global_game
    global_game = take_game
    get_game = await rq.get_game(global_game)
    for game in get_game:
        await callback.message.answer(f'{html.bold('Игра:')} {game.game}\n{html.bold('Описание аккаунта:')} {game.description}', reply_markup=kb.choosing_the_time)


@router.callback_query(F.data.startswith('one_hour'))
async def hand_one(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Отлично!', reply_markup=kb.payment_keyboard_one)


@router.callback_query(F.data.startswith('two_hour'))
async def hand_two(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Отличный выбор!', reply_markup=kb.payment_keyboard_two)


@router.callback_query(F.data.startswith('three_hour'))
async def hand_three(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('У вас есть вкус!', reply_markup=kb.payment_keyboard_three)


@router.callback_query(F.data.startswith('stars_one'))
async def buy_game_one(callback: CallbackQuery):
    get_game = await rq.get_game(global_game)
    for game in get_game:
        name_game = game.game
        decription = game.description
        pricestar = "1"

    await callback.message.answer_invoice(
            title=name_game,
            description=decription,
            provider_token='',
            currency="XTR",
            payload='game',
            prices=[LabeledPrice(label="XTR", amount=pricestar)]
    )
    await callback.answer()


@router.callback_query(F.data.startswith('stars_two'))
async def buy_game_two(callback: CallbackQuery):
    get_game = await rq.get_game(global_game)
    for game in get_game:
        name_game = game.game
        decription = game.description
        pricestar = "1"

    await callback.message.answer_invoice(
            title=name_game,
            description=decription,
            provider_token='',
            currency="XTR",
            payload='game',
            prices=[LabeledPrice(label="XTR", amount=pricestar)]
    )
    await callback.answer()


@router.callback_query(F.data.startswith('stars_three'))
async def buy_game_three(callback: CallbackQuery):
    get_game = await rq.get_game(global_game)
    for game in get_game:
        name_game = game.game
        decription = game.description
        pricestar = "1"

    await callback.message.answer_invoice(
            title=name_game,
            description=decription,
            provider_token='',
            currency="XTR",
            payload='game',
            prices=[LabeledPrice(label="XTR", amount=pricestar)]
    )
    await callback.answer()

@router.pre_checkout_query()
async def pre_checkout_querygame(event: PreCheckoutQuery) -> None:
    await event.answer(ok=True)


@router.message(F.successful_payment.invoice_payload == 'game')
async def successful_payment(message: Message, bot: Bot) -> None:
    get_game = await rq.get_game(global_game)
    for game in get_game:
        await bot.send_message(message.from_user.id, text=f'{html.bold('Email:')} {game.email}\n{html.bold('Password:')} {game.password}')
    await bot.refund_star_payment(message.from_user.id, message.successful_payment.telegram_payment_charge_id)