from telegram_bot.components.user.schema import UserSchema


class AdminMessages:
    @staticmethod
    def show_users(users: list[UserSchema]) -> str:
        return "\n".join([f"[{user.id}] {user.name}, Возраст: {user.age or 'Неизвестно'}\n" for user in users])
