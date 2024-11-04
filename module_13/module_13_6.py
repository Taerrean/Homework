from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

api = ''
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

kb = ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text = 'Инфо'), KeyboardButton(text = 'Рассчитать')]], resize_keyboard = True)

kb2 = InlineKeyboardMarkup()
ibutton = InlineKeyboardButton(text = 'Рассчитать норму калорий', callback_data = 'calories')
ibutton2 = InlineKeyboardButton(text = 'Формулы расчёта', callback_data = 'formulas')
kb2.row(ibutton, ibutton2)
@dp.message_handler(text = 'Инфо')
async def info(message):
    await message.answer('Бот был создан учеником Urban University и до сих пор в разработке. Ожидайте новых версий!')
@dp.message_handler(text = ['Рассчитать'])
async def menu(message):
    await message.answer(text = 'Выберите опцию:', reply_markup = kb2)
@dp.callback_query_handler(text = 'formulas')
async def formulas(call):
    await call.message.answer('Формула, используемая в вычислении - упрощённая формула Миффлина - Сан Жеора,'
                              ' и выглядит она так: 10 * вес + 6.25 * рост - 5 * возраст + 5.')
    await call.answer
@dp.callback_query_handler(text = 'calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст')
    await UserState.age.set()
    await call.answer
@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age = message.text)
    await message.answer('Введите свой рост')
    await UserState.growth.set()
@dp.message_handler(state = UserState.growth)
async def set_growth(message, state):
    await state.update_data(growth = message.text)
    await message.answer('Введите свой вес')
    await UserState.weight.set()
@dp.message_handler(state = UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight = message.text)
    data = await state.get_data()
    calories = 10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * float(data['age']) + 5
    await message.answer(f'Ваше необходимое количество калорий - {calories} в сутки!')
    await state.finish()

@dp.message_handler(commands = ['start'])
async def start_message(message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью!', reply_markup = kb)
@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение!')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)