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
