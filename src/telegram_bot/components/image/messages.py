class ImageMessages:
    @staticmethod
    def photo_info(size, height, width, downloaded):
        return f"Размер изображения: <b>{size}</b>\n" \
               f"Ширина: <b>{width}</b>\n" \
               f"Высота: <b>{height}</b>\n" \
               f"Изображение скачано: {'Да' if downloaded else 'Нет'}"

    @staticmethod
    def need_photo():
        return 'Необходимо к сообщению прикрепить изображение!'
