from kan import KAN
import torch
import os


'''
Загрузка модели 

Принимает:
    filename - название pth файла с моделью
    width, grid, k - гиперпараметры модели, которую мы загружаем (у разных моделей могут отличаться)
Возвращает:
    модель
'''

'''
Применение модели 

Принимает:
    model - модель
    features - список, состоящий из чисел-параметров в таком порядке ['wind_average','wind_max','temp','visibility','snow_depth','rainfall','rainfall_per_month','wind_drifting','total_wind_drifting','slope','volume']
Возвращает:
    число-вероятность лавины
'''


class MLModel:
    def __init__(self, filename: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../ML/model.pth'), width: list = [11, 1, 1], grid: int = 10, k: int = 3):
        self.model = KAN(width=width, grid=grid, k=k)
        self.checkpoint = torch.load(filename)
        self.model.load_state_dict(self.checkpoint['model_state_dict'])
        self.model.acts = self.checkpoint['acts']
        self.model.spline_postacts = self.checkpoint['spline_postacts']
        self.model.acts_scale = self.checkpoint['acts_scale']

    def get_forecast(self, features: list) -> float:
        features[2] = (features[2] + 24.3) / 39.0
        features[3] = (features[3] - 0.0) / 172.0
        features[4] = (features[4] - 0.0) / 190.0
        features[5] = (features[5] - 0.0) / 14.3
        features[6] = (features[6] - 0.0) / 194.7
        features[7] = (features[7] - 0.0) / 21.8
        features[8] = (features[8] - 0.0) / 17621.2
        features[9] = (features[9] - 0.0) / 50.0
        features[10] = (features[10] - 0.0) / 50.0

        res = self.model(torch.tensor([features]).float()).item()  # подача нормализованных параметров модели
        if res > 1:  # защита от аномальных данных
            res = 1
        elif res < 0:
            res = 0
        return res


ml_model_instance = MLModel()
