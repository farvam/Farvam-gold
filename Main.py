# کد ساده‌شده مخصوص موبایل
import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("✅ ربات فعال شد!")

executor.start_polling(dp)
