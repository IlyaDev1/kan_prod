from uvicorn import run
from fastapi import FastAPI
from Backend.shema import WeatherData
from Backend.service import Service


app = FastAPI()


@app.get('/', summary='Получить прогноз')
def get_forecast(data: WeatherData):
    forecast_value: float = Service.get_forecast(data)
    response = {"Avalanche probability": forecast_value}
    return response


if __name__ == '__main__':
    run('main:app', reload=False)
