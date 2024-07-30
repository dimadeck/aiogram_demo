class WeatherInitException(Exception):
    """Ошибка, выбрасываемая при исключениях во время инициализации класса Weather."""
    pass


class CalculateTemperatureException(Exception):
    """Ошибка, выбрасываемая при исключениях во время получении погоды - Weather.get_temperature()"""
    pass
