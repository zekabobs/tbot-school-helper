from config import LOG_DIR
from datetime import datetime


def log(title: str, cat=None):
    def outer(func):
        async def wrapper(message):
            new_title = title
            user_id = message['from']['id']
            date = datetime.now().strftime("%d-%m-%Y %H:%M")
            if cat:
                new_title += ' под учетной записью ' + cat
            row = '{} --- {} : {}\n'.format(new_title, user_id, date)
            open(LOG_DIR, 'a', encoding='utf-8').write(row)
            return await func(message)
        return wrapper
    return outer