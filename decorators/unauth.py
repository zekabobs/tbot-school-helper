from loader import sql

def unauth(func):
    async def wrapper(call):
        if sql.is_exists(call['message']['chat']['id']):
            await call.message.delete()
            await call.message.answer('Ошибка. Вы уже авторизованы 😤😤😤')
            return await call.answer('Ошибка. Вы уже авторизованы 😤😤😤')
        return await func(call)
    return wrapper