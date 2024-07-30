class WeatherMessages:
    @staticmethod
    def show_temperature(city: str, temperature: float) -> str:
        return f"Сейчас в <b>{city}</b>: <b>{temperature}℃</b>!"
