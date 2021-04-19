from aiogram.types import Message

from utils import utils
from decorators import auth
from loader import dp, sql


@dp.message_handler(regexp=r'^(расписание)$|^(расписание \d{1,2})|^расписание общее$')
@auth
async def send_timetable(message: Message):
    text = message.text.strip().lower()
    user_id = message.chat.id

    category = sql.get_category(user_id)
    if text == 'расписание' and category=='scholar':
        class_ = str(sql.get_scholar(user_id)[-1][-1])
        timetable = utils.get_timetable(class_)

    elif text == 'расписание' or text=='расписание общее':
        timetable = utils.get_timetable()

    else:
        timetable = utils.get_timetable(text.replace('расписание', '').strip())

    if not timetable:
        await message.answer('Неверные данные. Используйте команду /help для справки 📜')
    else:
        await message.answer_photo(timetable)