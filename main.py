from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from config import API_TOKEN, BOT_TOKEN
from scripts.get_weather import get_weather_spb
from scripts.get_vacancy_python import get_random_vacancy
import json

# токен вашего бота, полученный у @BotFather
TOKEN: str = BOT_TOKEN

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=TOKEN)
dp: Dispatcher = Dispatcher()

# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут бот-помощник!\nНапиши мне что-нибудь')

# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer('Напиши мне что-нибудь и в ответ я пришлю тебе твое сообщение')

# Этот хэндлер будет срабатывать на команду "/weather"
@dp.message(Command(commands=['weather']))
async def get_weather_command(message: Message):
    weather = get_weather_spb()
    date = weather[0]
    night = f'\n{weather[1]["weather_day"]}  {weather[1]["temperature"]}, {weather[1]["tooltip"]}\n'
    day = f'{weather[2]["weather_day"]}  {weather[2]["temperature"]}, {weather[2]["tooltip"]}\n'
    evenin = f'{weather[3]["weather_day"]}  {weather[3]["temperature"]}, {weather[3]["tooltip"]}'
    await message.answer(date+night+day+evenin)

# Этот хэндлер будет срабатывать на команду "/vacancy"
@dp.message(Command(commands=['vacancy']))
async def get_vacancy_command(message: Message):
    vacancies = get_random_vacancy()
    text = "Три случайные вакансии Python\n"
    first_vc = f"{vacancies[1]['name']}\nЗарплата -{ vacancies[1]['salary']}\n{vacancies[1]['url']}\n"
    second_vc = f"{vacancies[2]['name']}\n{vacancies[2]['salary']}\n{vacancies[2]['url']}\n"
    third_vc = f"{vacancies[3]['name']}\n{vacancies[3]['salary']}\n{vacancies[3]['url']}\n"

    await message.answer(first_vc)
    await message.answer(second_vc)
    await message.answer(third_vc)


# Этот хэндлер будет срабатывать на отправку боту любого сообщения
@dp.message()
async def send_echo(message: Message):
    #await message.reply(text=message.text)
    await message.answer("Введите команду из меню, либо /help для справки")

if __name__ == '__main__':
    dp.run_polling(bot)
