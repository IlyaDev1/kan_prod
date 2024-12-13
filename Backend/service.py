'''
Священный модуль сервиса.
Он, как видно в себе собирает бизнес-логику.
Принимает pydantic объект с запросом, переводит в список,
запускает метод для получения прогноза и возвращает его
'''


from ML.ml_model import ml_model_instance
from Backend.shema import WeatherData
from Backend.serializer import Serializer


class Service:
    @staticmethod
    def get_forecast(features: WeatherData) -> float:
        features = Serializer.json_to_list(features)
        forecast_result = ml_model_instance.get_forecast(features)
        return forecast_result
