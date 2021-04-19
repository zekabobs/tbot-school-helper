from aiogram.types import Message
from loader import dp

@dp.message_handler()
async def send_bad_request(message: Message):
    await message.answer('Я вас не пониманию. Воспользуйтесь командой <i><b>/help</b></i> для справки')