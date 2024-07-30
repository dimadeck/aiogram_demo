from telegram_bot.components.user.schema import UserSchema


class AdminMessages:
    @staticmethod
    def show_users(users: list[UserSchema]) -> str:
        return "\n".join([f"{user.name} ({user.id})\n" for user in users])
