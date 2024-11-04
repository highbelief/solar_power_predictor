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

    # 예측 후 다시 520 배율로 조정하여 kW 단위로 변환
    predicted_power = model.predict(data)[0] * 520.0
    print(f"Predicted Power for {observation_hour} hour: {predicted_power}")
    return predicted_power

# 예측 결과 저장
def save_prediction(observation_time, predicted_power, predicted_battery_level=80, predicted_status="정상"):
    engine = get_db_engine()

    # 날짜 형식 명시적으로 지정
    observation_time = observation_time.strftime('%Y-%m-%d %H:%M:%S')

    query = text("""
        INSERT INTO predictions (observation_time, predicted_power_generated, predicted_battery_level, predicted_equipment_status)
        VALUES (:observation_time, :predicted_power, :predicted_battery_level, :predicted_status)
    """)

    # 명시적으로 커넥션을 열고 트랜잭션 처리
    with engine.connect() as conn:
        try:
            # 트랜잭션 시작
            conn.execute(query, {
                'observation_time': observation_time,
                'predicted_power': predicted_power,
                'predicted_battery_level': predicted_battery_level,
                'predicted_status': predicted_status
            })
            # 커밋
            conn.commit()
            print(
                f"Data inserted for {observation_time}: Power - {predicted_power}, Battery - {predicted_battery_level}, Status - {predicted_status}")
        except Exception as e:
            print(f"Error inserting data: {e}")
            conn.rollback()
