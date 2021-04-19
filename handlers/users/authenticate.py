from aiogram.types import Message
from aiogram.types import CallbackQuery

from keyboards.inline.category import category_keyboard
from keyboards.inline.category import scholar_class_keyboard
from keyboards.default.basic import basic_keyboard
from decorators import log, unauth
from loader import dp, sql


@dp.message_handler(commands='auth')
async def authenticate(message: Message):
    await message.answer('<b><i>Кто вы?</i></b>', reply_markup=category_keyboard)


@dp.callback_query_handler(text='scholar')
@log('Попытка авторизации', 'школьник')
@unauth
async def set_scholar(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer('<b>Выберите класс:</b>', reply_markup=scholar_class_keyboard)


@dp.callback_query_handler(text='teacher')
@log('Попытка авторизации', 'учитель')
@unauth
async def set_adult(call: CallbackQuery):
    user_id = call.message.chat.id
    username = call.message.chat.username
    await call.message.delete()

    sql.insert_data('teacher', username, user_id, 'Null')

    await call.message.answer(f"Вы авторизовались как 'Учитель'", reply_markup=basic_keyboard)
    await call.answer(f"Вы авторизовались как 'Учитель'")


@dp.callback_query_handler(text='parent')
@log('Попытка авторизации', 'родитель')
@unauth
async def set_adult(call: CallbackQuery):
    user_id = call.message.chat.id
    username = call.message.chat.username

    await call.message.delete()


    sql.insert_data('parent', username, user_id, 911)
    await call.message.answer("Вы авторизовались как 'Родитель'", reply_markup=basic_keyboard)
    await call.answer("Вы авторизовались как 'Родитель'")


@dp.callback_query_handler(lambda call: call.data.isdigit() and int(call.data) in range(1,10), state=Scholar)
@unauth
async def scholar_auth(call: CallbackQuery):
    await call.message.delete()
    user_id = call.message.chat.id
    username = call.message.chat.username
    class_ = int(call.data)

    sql.insert_data('scholar', username, user_id, 'Null', class_)
    await call.message.answer(f"Вы авторизовались как 'Ученик' {call.data} класса", reply_markup=basic_keyboard)
    await call.answer("Вы авторизовались как 'Ученик'")

