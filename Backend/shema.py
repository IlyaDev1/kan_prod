'''
Это модуль, определяющий DTO для работы сервиса с http запросами и json данными
и кодом питона.
Здесь описывается класс объекта принимаемого json, чтобы питон его понимал.
Соответствует example.json
'''


from pydantic import BaseModel


class WeatherData(BaseModel):
    wind_average: float
    wind_max: float
    temp: float
    visibility: float
    show_depth: float
    rainfall: float
    rainfall_per_month: float
    wind_drifting: float
    total_wind_drifting: float
    slope: float
    volume: float
