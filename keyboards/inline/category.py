from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .callback_data import category_data

category_keyboard = InlineKeyboardMarkup()
for x in category_data:
    button = InlineKeyboardButton(text=x, callback_data=category_data[x])
    category_keyboard.add(button)

scholar_class_keyboard = InlineKeyboardMarkup()
for x in range(1, 10):
    button = InlineKeyboardButton(text=x, callback_data=x)
    scholar_class_keyboard.add(button)