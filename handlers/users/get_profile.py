from aiogram.types import Message

from decorators import auth
from loader import dp, sql


@dp.message_handler(commands='get_profile')
@auth
async def send_user_info(message: Message):
    user_id = message.chat.id
    user = sql.get_user_info(user_id)

    result = ''
    for item in user:
        id = 'ID: ' + str(item[0]) + '\n'
        username = 'Псевдоним: ' + item[1] + '\n'
        category = 'Категория: ' + item[2] + '\n'
        fio = 'ФИО: ' + item[3] + '\n'
        result = id + username + category + fio

    await message.answer(f'<u>Информация о вас</u>:\n<b>{result}</b>')