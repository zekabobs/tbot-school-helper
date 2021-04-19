from aiogram.types import Message
from aiogram.types import CallbackQuery
from aiogram.dispatcher.dispatcher import FSMContext

from re import match as re_match

from keyboards.inline.cancel import calcel_button
from states.fio_state import AuthState

from decorators import auth
from loader import dp, sql


@dp.message_handler(commands='set_profile', state=None)
@auth
async def set_profile_info(message: Message):
    await AuthState.fio_check.set()
    await message.answer('Введите ваши <b>фамилию имя и отчетсво</b>.\nВ <u>одну строку</u>, <u>через пробел</u>.', reply_markup=calcel_button)


@dp.message_handler(content_types='text', state=AuthState.fio_check)
async def set_fio(message: Message, state: FSMContext):
    user_data = message.text.strip().lower()
    user_id = message.chat.id

    if user_data and re_match(r'^[А-Яа-я]{2,20} [А-Яа-я]{2,20} [А-Яа-я]{2,20}$', user_data):
        result = sql.update_user_fio(user_id, user_data.title())
        if result:
            await message.answer('Данные успешно обновлены')
            await state.update_data(set_fio_check=1)
            await state.finish()

    else:
        keyboard = calcel_button
        await message.answer('<b>Ошибка. Некорректные данные.</b> Попробуйте ввести заново.', reply_markup=keyboard)


@dp.callback_query_handler(text='cancel')
async def send_cancel(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=None)
    await call.answer('Отменено.\nНо зачем это делать сейчас?')


@dp.callback_query_handler(text='cancel', state=AuthState.fio_check)
async def send_cancel(call: CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup(reply_markup=None)

    await state.finish()
    await call.answer('Отменено')

@dp.message_handler(commands='get_profile')
@auth
async def send_user_info(message: Message):
    user_id = message.chat.id
    user = sql.get_user_info(user_id)

    result = ''
    for item in user:
        id = 'ID: ' + str(item[0]) + '\n'
        username = 'Псевдоним: ' + item[1] + '\n'
        category = 'Категория: ' + item[2] + '\n'
        fio = 'ФИО :' + item[3] + '\n'
        result = id + username + category + fio

    await message.answer(f'<u>Информация о вас</u>:\n<b>{result}</b>')