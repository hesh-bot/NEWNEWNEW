# app.py
# Telegram anonymous complaints bot (aiogram v3)
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message

BOT_TOKEN = "8488177555:AAEGwmER1kJ5zEDrI-8t9njxrX33rGkNhgQ"
ADMIN_CHAT_ID = -1002933914421

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(" Максимально подробно опишите проблему. Чем больше информации - тем быстрее отработают соответствующие органы! Отправьте жалобу, и я полностью передам её анонимно администраторам. В случае если вы хотите - можете оставить контакты для связи и конкретизации информации. Быть добру!")

@dp.message()
async def complaint(message: Message):
    await bot.send_message(ADMIN_CHAT_ID, f"⚠️ Новая анонимная жалоба:\n{message.text}")
    await message.answer("✅ Жалоба отправлена!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
