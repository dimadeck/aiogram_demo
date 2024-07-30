class ScheduleMessages:
    @staticmethod
    def daily_message() -> str:
        return "Не забудьте проверить уведомления!"

    @staticmethod
    def welcome_message(username: str) -> str:
        return f"Привет, {username}! Как ты сегодня?"

    @staticmethod
    def remind_message() -> str:
        return "Вы забыли ответить!"

    @staticmethod
    def cancel_waiting() -> str:
        return "Спасибо за ваш ответ!"
