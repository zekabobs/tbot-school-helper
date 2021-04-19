from aiogram.types import Message

from decorators import auth
from loader import dp, sql


@dp.message_handler(commands='subscribe')
@auth
async def set_subscribe(message: Message):
    sql.subscribe(message.from_user.id)
    await message.answer('Вы подписались на рассылку.')