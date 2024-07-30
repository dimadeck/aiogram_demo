class StateMessages:
    @staticmethod
    def wait_name_message(user):
        return f"{user.name}, Давай познакомимся! Как тебя зовут?"

    @staticmethod
    def wait_age_message():
        return f"Красивое имя! Сколько тебе лет?"

    @staticmethod
    def show_info_message(name: str, age: str):
        return f"Я понял, тебя зовут <b>{name}</b> и твой возраст: <b>{age}</b>!"
