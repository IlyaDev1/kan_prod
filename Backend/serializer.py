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
