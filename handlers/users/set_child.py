from aiogram.types import Message

from keyboards.inline.category import scholar_class_keyboard

from decorators import auth
from loader import dp

@dp.message_handler(commands='set_child')
async def set_child(message: Message):
    await message.answer('В каком классе учится ваш ребенок?', reply_markup=scholar_class_keyboard)
