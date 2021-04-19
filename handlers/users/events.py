from aiogram.types import Message

from decorators import auth
from utils import utils
from loader import dp


@dp.message_handler(regexp=r'^мероприяти[я,е]$')
@auth
async def send_events(message: Message):
    data = utils.generate_events()
    if data:
        await message.answer('<b>Грядущие мероприятия</b>')
        await message.answer_photo(data)
    else:
        await message.answer('На ближайшее время ничего не запланировано.')