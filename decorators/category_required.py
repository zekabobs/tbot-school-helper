from loader import sql


def category_req(func):
    async def wrapper(message):
        if sql.get_category(message['from']['id']) != 'teacher':
            return await message.reply('<u>Доступ</u> к параметрам мероприятий имеет только <b>Учитель</b>.')
        return await func(message)
    return wrapper