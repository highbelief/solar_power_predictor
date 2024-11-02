from sklearn.ensemble import GradientBoostingRegressor


# 모델 학습
def train_model(data):
    features = data[['temperature', 'solar_irradiance', 'humidity', 'cloud_coverage', 'hour']]
    target = data['power_generated']

    model = GradientBoostingRegressor()
    model.fit(features, target)
    return model
