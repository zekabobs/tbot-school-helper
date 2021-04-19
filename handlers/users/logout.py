from aiogram.types import Message, ReplyKeyboardRemove

from decorators import auth, log
from loader import dp, sql


@dp.message_handler(commands=['logout'])
@auth
@log('Выход их сессии')
async def logout(message: Message):
    user_id = message.chat.id
    sql.delete_data(user_id)
    await message.answer('Успешно вышли из сессии', reply_markup=ReplyKeyboardRemove())