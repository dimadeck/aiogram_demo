class WeatherInitException(Exception):
    """Ошибка, выбрасываемая при исключениях во время инициализации класса Weather."""
    pass


class WeatherTemperatureException(Exception):
    """Ошибка, выбрасываемая при исключениях во время получении погоды - Weather.get_temperature()"""
    pass
