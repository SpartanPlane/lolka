from config import TOKEN
import logging
from aiogram import Bot, Dispatcher, executor, types
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_hello(message: types.Message):
    await bot_send_message(message.from_user.id, 'Привет\nЧто будем делать')

@dp.message_handler(commands=['help'])
async def process_hello(message: types.Message):
    await bot_send_message(message.from_user.id, 'Нужна помощь?')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)