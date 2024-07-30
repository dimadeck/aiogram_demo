from pyowm import OWM

from core.weather.exceptions import WeatherInitException, WeatherTemperatureException


class Weather:
    """
    Минималистичный класс для получения текущей температуры в градусах Цельсия в выбранном городе.

    Используется API OpenWeatherMap.

    Notes:
        Получение API_KEY: https://home.openweathermap.org/api_keys

    Examples:
        >>> API_KEY = 'SomeKey'
        >>> Weather(API_KEY).get_temperature('Москва')
        >>> 15.73
        >>> Weather(API_KEY).get_temperature('Moscow')
        >>> 15.79
    """

    def __init__(self, api_key: str):
        """
        Инициализация менеджера OWM.

        Args:
            api_key(str): Ключ для API OpenWeatherMap.
        """
        self._api_key = api_key
        self._owm = None
        self._mgr = None
        self._init_owm()

    def _init_owm(self) -> None:
        """Инициализация менеджера OWM."""
        try:
            self._owm = OWM(self._api_key)
            self._mgr = self._owm.weather_manager()
        except Exception as e:
            raise WeatherInitException(str(e))

    def get_temperature(self, city: str) -> float:
        """
        Определение текущей температуры в городе city.

        Args:
            city(str): Город, для готорого нужно определить температуру.

        Returns:
            (float) - Текущая температура в выбранном городе.
        """
        try:
            observation = self._mgr.weather_at_place(city)
            return observation.weather.temperature('celsius')['temp']
        except Exception as e:
            raise WeatherTemperatureException(str(e))
