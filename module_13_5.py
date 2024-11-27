import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
kb = ReplyKeyboardMarkup()
b1 = KeyboardButton(text='Рассчитать калории')
b2 = KeyboardButton(text='Информация')
kb.row(b1, b2)
kb.resize_keyboard
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler(text=['Информация'])
async def info(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler(text=['Рассчитать калории'])
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    try:
        await state.update_data(age=int(message.text))
        await message.answer('Введите свой рост:')
        await UserState.growth.set()
    except ValueError:
        await message.answer("Пожалуйста, используйте цифры.")
        await UserState.age.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    try:
        await state.update_data(growth=int(message.text))
        await message.answer('Введите свой вес:')
        await UserState.weight.set()
    except ValueError:
        await message.answer("Пожалуйста, используйте цифры.")
        await UserState.growth.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    try:
        await state.update_data(weight=int(message.text))
        data = await state.get_data()
        norm = 10*data['weight']+6.5*data['growth']-5*data['age']-161
        await message.answer(f'Оптимальное количество каллорий за день: {norm}')
        await state.finish()
    except ValueError:
        await message.answer("Пожалуйста, используйте цифры.")
        await UserState.weight.set()


@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
