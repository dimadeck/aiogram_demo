class ScheduleMessages:
    @staticmethod
    def daily_message():
        return "Не забудьте проверить уведомления!"

    @staticmethod
    def welcome_message(username):
        return f"Привет, {username}! Как ты сегодня?"

    @staticmethod
    def remind_message():
        return "Вы забыли ответить!"

    @staticmethod
    def cancel_waiting():
        return "Спасибо за ваш ответ!"
