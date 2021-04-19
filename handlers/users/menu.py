from aiogram.types import Message

from decorators import auth
from utils import utils
from loader import dp

@dp.message_handler(lambda w: 'меню' in w.text.lower())
@auth
async def send_menu(message: Message):
    text = message.text.strip().lower()
    if text == 'меню':
        result = utils.generate_menu()
    else:
        result = utils.generate_menu(set(text.split()))

    if not result:
        result = 'Неверные данные. Используйте команду /help для справки 📜'
    await message.answer(result)