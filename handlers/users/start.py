from aiogram.types import Message
from aiogram.dispatcher.filters.builtin import CommandStart

from utils.utils import get_sticker_hello
from loader import dp


@dp.message_handler(CommandStart())
async def send_welcome(message: Message):
    sticker = get_sticker_hello()
    await message.answer_sticker(sticker)
    await message.answer(f'Привет, {message.from_user.username}')