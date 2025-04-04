from aiogram import Dispatcher, Bot
from aiogram.types import Message
from aiogram.filters import Command

from config_bot import My_Bot

my_bot = My_Bot()

dp = Dispatcher()
bot = Bot(token=my_bot.token)


@dp.message(Command(commands=["start"]))
async def start(message=Message):
    await message.answer(my_bot.start)


@dp.message(Command(commands=["help"]))
async def help(message=Message):
    await message.answer(my_bot.help)


@dp.message()
async def text_mess(message=Message):
    await message.answer(message.text)


if __name__ == "__main__":
    dp.run_polling(bot)
    print("Бот запущен")
