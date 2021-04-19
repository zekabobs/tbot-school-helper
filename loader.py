from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import logging
import config

from utils.db_connertor import Sqlliter

bot = Bot(token=config.BOT_TOKEN, parse_mode='HTML')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
sql = Sqlliter('school_db.db')
logging.basicConfig(level=logging.INFO)