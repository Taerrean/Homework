from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from module_14.admin import *
from module_14.crud_functions import *
products = get_all_products('Products')

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

api = ''
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

kb = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = 'Инфо'), KeyboardButton(text = 'Рассчитать')],
    [KeyboardButton(text = 'Купить')],
    [KeyboardButton(text = 'Регистрация')]],
    resize_keyboard = True)

kb2 = InlineKeyboardMarkup()
ibutton = InlineKeyboardButton(text = 'Рассчитать норму калорий', callback_data = 'calories')
ibutton2 = InlineKeyboardButton(text = 'Формулы расчёта', callback_data = 'formulas')
kb2.row(ibutton, ibutton2)

buy_menu = InlineKeyboardMarkup()
b1 = InlineKeyboardButton(text = 'Heheheha', callback_data = 'product_purchase')
b2 = InlineKeyboardButton(text = 'Houhouhouhoi', callback_data = 'product_purchase')
b3 = InlineKeyboardButton(text = 'Haha', callback_data = 'product_purchase')
b4 = InlineKeyboardButton(text = 'Grrr', callback_data = 'product_purchase')
buy_menu.row(b1, b2)
buy_menu.row(b3, b4)

admin_panel = InlineKeyboardMarkup(
    inline_keyboard = [
        [InlineKeyboardButton(text = 'Пользователи', callback_data = 'users')],
        [InlineKeyboardButton(text = 'Статистика', callback_data = 'stat')],
        [
        InlineKeyboardButton(text = 'Блокировка', callback_data = 'block'),
        InlineKeyboardButton(text = 'Разблокировка', callback_data = 'unblock')
        ]
    ]
)

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
@dp.callback_query_handler(text = 'product_purchase')
async def purchase(call):
    await call.message.answer('Вы успешно приобрели продукт!')


@dp.message_handler(text = 'Инфо')
async def info(message):
    await message.answer('Бот был создан учеником Urban University и до сих пор в разработке. Ожидайте новых версий!')
@dp.message_handler(text = 'Регистрация')
async def sign_up(message):
    await message.answer(text = "Введите имя пользователя (Только на латинице):")
    await RegistrationState.username.set()
@dp.message_handler(state = RegistrationState.username)
async def username_stage(message, state):
    if not is_included(message.text):
        await state.update_data(username = message.text)
        await message.answer('Введите ваш почтовый адрес:')
        await RegistrationState.email.set()
    else:
        await message.answer('Пользователь существует, введите другое имя.')
        await RegistrationState.username.set()
@dp.message_handler(state = RegistrationState.email)
async def email_stage(message, state):
    await state.update_data(email = message.text)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()
@dp.message_handler(state = RegistrationState.age)
async def age_stage(message, state):
    await state.update_data(age = message.text)
    data = await state.get_data()
    add_user(data['username'], data['email'], data['age'])
    await message.answer(text = 'Аккаунт успешно создан!')
    await state.finish()
@dp.message_handler(text = ['Рассчитать'])
async def menu(message):
    await message.answer(text = 'Выберите опцию:', reply_markup = kb2)
@dp.message_handler(text = 'Купить')
async def get_selection(message):
    for i in range(len(products)):
        await message.answer(f'Название: {products[i][1]} | Описание: Описание {products[i][2]} | Цена: {products[i][3]}\n')
        with open(f'pics/img{i + 1}.png', 'rb') as img:
            await message.answer_photo(img)
    await message.answer('Выберите продукт:', reply_markup = buy_menu)
@dp.message_handler(commands = ['start'])
async def start_message(message):
    await message.answer(f'Привет, {message.from_user.username}! Я бот, помогающий твоему здоровью!', reply_markup = kb)
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
@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение!')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)