from aiogram.dispatcher.filters.state import State, StatesGroup

class ScholarClassState(StatesGroup):
    class_ = State()