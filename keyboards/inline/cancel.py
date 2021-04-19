from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

calcel_button = InlineKeyboardMarkup()
calcel_button.insert(InlineKeyboardButton(text='Отмена ❌', callback_data='cancel'))