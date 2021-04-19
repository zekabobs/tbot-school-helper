from aiogram.types import Message

from decorators import auth
from loader import dp, sql


@dp.message_handler(commands='unsubscribe')
@auth
async def set_unsubscribe(message: Message):
    sql.unsubscribe(message.from_user.id)
    await message.answer('Вы отписались от рассылки.')