'''
Это главный модуль бэка, он запускает веб сервер и контролирует апи
'''


from uvicorn import run
from fastapi import FastAPI
from Backend.shema import WeatherData
from Backend.service import Service


app = FastAPI()  # создание объекта приложения на веб сервере


@app.get('/', summary='Получить прогноз')  # endpoint. http uri к нему
def get_forecast(data: WeatherData):  # Это принимает запросы, обрабатывает их и возвращает ответ
    """
    Обрабатывает HTTP GET запрос для получения прогноза на основе входящих данных о погоде.

    Параметры:
    - data (WeatherData): Объект с данными о погоде, включая средний ветер, максимальный ветер,
      температуру, видимость и другие параметры.

    Возвращает:
    dict: Словарь с вероятностью лавины.
    """
    forecast_value: float = Service.get_forecast(data)
    response: dict = {"Avalanche probability": forecast_value}
    return response


if __name__ == '__main__':  # Вход в программу
    run('main:app', reload=False)
