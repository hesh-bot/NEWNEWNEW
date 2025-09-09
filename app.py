# app.py
# Telegram anonymous complaints bot (aiogram v3)
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message

BOT_TOKEN = "PUT_YOUR_BOT_TOKEN_HERE"
ADMIN_CHAT_ID = -1001234567890

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("👋 Отправьте жалобу, и я передам её анонимно администраторам.")

@dp.message()
async def complaint(message: Message):
    await bot.send_message(ADMIN_CHAT_ID, f"⚠️ Новая анонимная жалоба:\n{message.text}")
    await message.answer("✅ Жалоба отправлена!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
