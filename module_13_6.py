import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Рассчитать'),
            KeyboardButton(text='Информация')
        ],
    ],
    resize_keyboard=True
)
gen = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Муж'), KeyboardButton(text='Жен')]],resize_keyboard=True)
calk = InlineKeyboardMarkup()
b1=InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
b2=InlineKeyboardButton(text='Формулы расчета', callback_data='formulas')
calk.add(b1)
calk.add(b2)
calk.resize_keyboard=True

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    gender = State()

    def set_gender(self, g):
        self.gender=int(g)


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)

@dp.message_handler(text=['Информация'])
async def info(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
    await message.answer('Выберите опцию.', reply_markup=calk)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('Оптимальное количество калорий в день высчитывается по формуле:\n'
                              '10*вес+6.5*рост-5*возраст-161 для женщин\n'
                              'и\n'
                              '10*вес+6.5*рост-5*возраст+5 для мужчин')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await call.answer()
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
        norm = 10*data['weight']+6.5*data['growth']-5*data['age']-151
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
