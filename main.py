import asyncio
import logging
import os
import warnings


from dotenv import load_dotenv
from aiogram.filters import Command
from aiogram import Bot, Dispatcher, F
from handlers.starthandler import router
from database.models import async_main
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from utils.commands import set_commands
from handlers.outputhandler import command_start_acc, select_keyboard_accounts, get_time_for_game, hand_one, hand_two, hand_three, buy_game_one, buy_game_two, buy_game_three, pre_checkout_querygame, successful_payment


load_dotenv()
token = os.getenv("TOKEN")

bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher()


dp.message.register(command_start_acc, Command(commands='accounts'))
dp.callback_query.register(select_keyboard_accounts, F.data.startswith('accounts'))
dp.callback_query.register(get_time_for_game, F.data.startswith('select_'))
dp.callback_query.register(hand_one, F.data.startswith('one_hour'))
dp.callback_query.register(hand_two, F.data.startswith('two_hour'))
dp.callback_query.register(hand_three, F.data.startswith('three_hour'))
dp.callback_query.register(buy_game_one, F.data.startswith('stars_one'))
dp.callback_query.register(buy_game_two, F.data.startswith('stars_two'))
dp.callback_query.register(buy_game_three, F.data.startswith('stars_three'))
dp.pre_checkout_query.register(pre_checkout_querygame)  
dp.message.register(successful_payment, F.successful_payment.invoice_payload == 'game')


async def main() -> None:
    await async_main()
    dp.include_router(router)
    await set_commands(bot)
    await bot.delete_webhook(True)
    await dp.start_polling(bot, skip_updates=False)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO)
        warnings.filterwarnings("error", category=RuntimeWarning)
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')