from aiogram.types import Message
from aiogram.dispatcher.filters.builtin import CommandHelp

from utils.utils import get_info
from loader import dp


@dp.message_handler(CommandHelp())
async def send_help(message: Message):
    info = get_info()
    await message.answer(info, parse_mode='HTML')