from telegram_bot.components.user.schema import UserSchema


class UserMessages:
    @staticmethod
    def welcome_message(user):
        return f"Добро пожаловать в наш бот, {user.name}!"

    @staticmethod
    def me(user: UserSchema):
        return f"""Данные вашего аккаунта: 
Username: @{user.username}
Имя: {user.name}
ID: {user.id}
Дата регистрации: {user.created_at}
Активен: {'Да' if user.is_active else 'Нет'}
Админ: {'Да' if user.is_admin else 'Нет'}
"""

    @staticmethod
    def help():
        return "Доступные команды: /start, /help, /echo, /photo"

    @staticmethod
    def admin_status(is_admin):
        return f"Статус администратора: {'+ Включен' if is_admin else '- Выключен'}"
