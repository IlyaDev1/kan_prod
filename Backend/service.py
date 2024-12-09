from ML.ml_model import ml_model_instance


class Service:
    @staticmethod
    def get_forecast(features: list) -> float:
        forecast_result = ml_model_instance.get_forecast(features)
        return forecast_result
