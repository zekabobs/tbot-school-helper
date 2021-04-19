from aiogram.dispatcher.filters.state import State, StatesGroup

class AuthState(StatesGroup):
    fio_check = State()