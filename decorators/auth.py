from loader import sql


def auth(func):
    async def wrapper(message):
        if not sql.is_exists(message['from']['id']):
            return await message.reply('Для <u>доступа</u> к функционалу бота <b>авторизуйтесь</b> командой /auth')
        return await func(message)
    return wrapper