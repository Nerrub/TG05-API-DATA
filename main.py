import asyncio
import aiohttp
from datetime import datetime
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
import logging

# Инициализация бота с вашим токеном
bot = Bot(token="YOUR_BOT_TOKEN")
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)


# Функция для получения информации о числе с сайта numbersapi.com
async def get_number_fact(number: int) -> str:
    url = f"http://numbersapi.com/{number}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


# Обработчик команды /start
@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Привет! Используй команду /fact чтобы получить интересный факт о сегодняшнем числе.")


# Обработчик команды /fact
@dp.message(Command("fact"))
async def fact_command(message: Message):
    # Получаем текущее число дня
    today_number = datetime.now().day

    # Получаем факт о числе с сайта
    fact = await get_number_fact(today_number)

    # Отправляем факт пользователю
    await message.answer(f"Факт о числе {today_number}: {fact}")


# Основная функция для запуска бота
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
