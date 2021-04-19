import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.environ.get('TOKEN')
FILES_DIR = 'files/'
LOG_DIR = FILES_DIR + '/docs/log.log'