'''
Это модуль, который меняет форматы данных, если по тем или иным
причинам использовать DTO не получается
В данном случае, я перевожу pydantic объект из запроса в список, так как
модуль модели МЛ работает со списком, а подкапотный метод иначе не умеет.
Переопределять эту историю я не решился
'''


from Backend.shema import WeatherData


class Serializer:
    @staticmethod
    def json_to_list(features: WeatherData) -> list:
        list_instance = [
            features.wind_average,
            features.wind_max,
            features.temp,
            features.visibility,
            features.show_depth,
            features.rainfall,
            features.rainfall_per_month,
            features.wind_drifting,
            features.total_wind_drifting,
            features.slope,
            features.volume,
        ]

        return list_instance
