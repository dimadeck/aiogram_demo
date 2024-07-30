from pyowm import OWM

from core.weather.exceptions import WeatherInitException, CalculateTemperatureException


class Weather:
    def __init__(self, api_key: str):
        self._api_key = api_key
        self._owm = None
        self._mgr = None
        self._init_owm()

    def _init_owm(self):
        try:
            self._owm = OWM(self._api_key)
            self._mgr = self._owm.weather_manager()
        except Exception as e:
            raise WeatherInitException(str(e))

    def get_temperature(self, city: str) -> float:
        try:
            observation = self._mgr.weather_at_place(city)
            return observation.weather.temperature('celsius')['temp']
        except Exception as e:
            raise CalculateTemperatureException(str(e))
