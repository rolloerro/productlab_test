import asyncio
import os
from fastapi import FastAPI
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv
import uvicorn

# === Настройки ===
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = FastAPI(
    title="ProductLab Test API",
    version="1.0.0",
    description="Демо API для ProductLab (FastAPI + aiogram)"
)

@app.get("/")
def root():
    return {"message": "API работает 🚀", "docs": "/docs"}

@app.get("/health")
def health():
    return {"status": "ok"}

# === Telegram Bot ===
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_command(message: Message):
    await message.answer("✅ Бот ProductLab01 запущен и готов к работе!")

async def start_fastapi():
    """Запуск FastAPI-сервера"""
    config = uvicorn.Config(app, host="0.0.0.0", port=8080, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()

async def main():
    """Запуск бота и API в одном event loop"""
    task_bot = asyncio.create_task(dp.start_polling(bot))
    task_api = asyncio.create_task(start_fastapi())
    await asyncio.gather(task_bot, task_api)

if __name__ == "__main__":
    asyncio.run(main())
