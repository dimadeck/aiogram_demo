class InlineMessages:
    @staticmethod
    def make_choice() -> str:
        return "Сделайте свой выбор!"

    @staticmethod
    def first_button() -> str:
        return "Вы сделали <b>Выбор 1</b>!"

    @staticmethod
    def second_button() -> str:
        return "Вы сделали <b>Выбор 2</b>!"

    @staticmethod
    def error_choice() -> str:
        return "Я не знаю, что вы выбрали :("
