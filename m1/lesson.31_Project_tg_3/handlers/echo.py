from aiogram import Router, types, F
from aiogram.filters.command import Command
# from random_fox import fox


router = Router()


@router.message(F.text)
async def echo(message: types.Message):
    # print(message.text)
    # print(type(message.text))
    if message.text == '/stop':
        await message.answer('Ты точно хочешь остановиться?')
    elif 'stop' in message.text:
        await message.answer('Останавливаемя??')
    else:
        await message.answer(f'Ты написал {message.text}')