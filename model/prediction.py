import pandas as pd
from datetime import datetime, timedelta
from config.database_config import get_db_engine
from sqlalchemy import text

# 예측 수행
def predict_next_day(model, observation_hour):
    data = pd.DataFrame({
        'temperature': [25],
        'solar_irradiance': [300],
        'humidity': [50],
        'cloud_coverage': [20],
        'hour': [observation_hour]
    })
    predicted_power = model.predict(data)[0]
    print(f"Predicted Power for {observation_hour} hour: {predicted_power}")
    return predicted_power

# 예측 결과 저장
def save_prediction(observation_time, predicted_power, predicted_battery_level=80, predicted_status="정상"):
    engine = get_db_engine()
    query = text("""
        INSERT INTO predictions (observation_time, predicted_power_generated, predicted_battery_level, predicted_equipment_status)
        VALUES (:observation_time, :predicted_power, :predicted_battery_level, :predicted_status)
    """)
    with engine.begin() as conn:
        conn.execute(query, {
            'observation_time': observation_time,
            'predicted_power': predicted_power,
            'predicted_battery_level': predicted_battery_level,
            'predicted_status': predicted_status
        })
    print(f"Data inserted for {observation_time}: Power - {predicted_power}, Battery - {predicted_battery_level}, Status - {predicted_status}")
