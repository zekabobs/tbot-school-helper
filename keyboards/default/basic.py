from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

basic_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

for item in ('меню', 'мероприятия','расписание'):
    button = KeyboardButton(text=item)
    basic_keyboard.row(button)