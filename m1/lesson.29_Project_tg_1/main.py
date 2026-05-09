import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import config


TOKEN_TG = config.token_telegram
TOKEN_OPENAI = config.token_openai

# Включаем логирование
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN_TG)
dp = Dispatcher()


# /start
@dp.message(Command('start'))
async def command_start(message: types.Message):
    await message.answer('Привет!')


# /info
@dp.message(Command('info'))
async def command_info(message: types.Message):
    await message.answer('Это бот с подключением ChatGPT!')


@dp.message(F.text)
async def echo(message: types.Message):
    await message.answer(message.text)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

