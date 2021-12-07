import requests

from epam.settings import API_KEY


class Weather:
    """
    Class for weather. For initialization put city as string into Weather and get current weather temperature in kelvin
    """
    KELVIN_DISTINCTION_CELSIUS = 273.15
    KELVIN_DISTINCTION_FAHRENHEIT = 255.372

    def __init__(self, city: str, fahrenheit=False):
        self.city = city
        self.fahrenheit = fahrenheit if fahrenheit else False
        self._weather = self.get_weather_temperature()

    @property
    def weather(self):
        return self._weather

    def get_weather_temperature(self):
        """
        Method to get weather in kelvins,
        :returns: float or tuple
        :returns  temperature in kelvins or tuple(error code and message)
        """

        url = f'https://api.openweathermap.org/data/2.5/weather?q={self.city}&APPID={API_KEY}'
        response = requests.get(url=url, ).json()

        try:
            current_weather = response['main']['temp']
            if self.fahrenheit:
                current_weather = current_weather - self.KELVIN_DISTINCTION_FAHRENHEIT
            else:
                current_weather = current_weather - self.KELVIN_DISTINCTION_CELSIUS
        except KeyError:
            error_code = response['cod']
            error_message = response['message']
            return error_code, error_message

        return float(current_weather)

    def to_dict(self) -> dict:
        """
        Serializer. Return dict {temperature: 33.222222, city: london} or error dict
        {'code': 404, 'message': some message}
        :return: dict
        """

        if isinstance(self.weather, tuple):
            return {'code': self.weather[0],
                    'message': self.weather[1]}

        elif isinstance(self.weather, float):
            return {'temperature': self.weather,
                    'city': self.city}
