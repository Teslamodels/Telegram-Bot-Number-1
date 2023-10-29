import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from button import main_markup
from register import router
from register_2 import router_2
from register_3 import router_3
from register_4 import router_4
from register_5 import router_5
from register_6 import router_6
from register_7 import router_7
from config import bot_token
dp = Dispatcher(storage = MemoryStorage())
bot = Bot(token=bot_token, parse_mode = ParseMode.MARKDOWN_V2)
# from db import create_new_table
# create_new_table()




@dp.message(CommandStart())
async def let_it_to_start(message: types.Message):
    await message.answer("😄 Hello", reply_markup = main_markup())



async def main():
    dp.include_routers(router, router_2, router_3, router_4, router_5, router_6, router_7)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        logging.basicConfig(level = logging.INFO, stream = sys.stdout)
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Error")