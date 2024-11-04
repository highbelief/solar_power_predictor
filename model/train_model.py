from sklearn.ensemble import GradientBoostingRegressor


# 모델 학습
def train_model(data):
    features = data[['temperature', 'solar_irradiance', 'humidity', 'cloud_coverage', 'hour']]
    target = data['power_generated']

    # 발전량을 520에 맞게 스케일링
    target = target / 520.0  # 학습 데이터를 0~1 범위로 스케일링

    model = GradientBoostingRegressor()
    model.fit(features, target)
    return model