import pandas as pd
from config.database_config import get_db_engine
from datetime import datetime


# 하루치 데이터 로드
def load_daily_data():
    engine = get_db_engine()
    start_time = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    end_time = datetime.now().replace(hour=18, minute=0, second=0, microsecond=0)

    query = f"""
    SELECT * FROM simulation_data
    WHERE observation_time BETWEEN '{start_time}' AND '{end_time}'
    """

    data = pd.read_sql(query, engine)

    # 로드된 데이터의 길이 출력
    print(f"Data loaded: {len(data)} rows")

    return data

# 데이터 전처리
def preprocess_data(data):
    # observation_time 열을 datetime 형식으로 강제 변환
    data['observation_time'] = pd.to_datetime(data['observation_time'], errors='coerce')

    # 결측값 제거
    data = data.dropna(subset=['observation_time'])

    # hour 열 추가
    data['hour'] = data['observation_time'].dt.hour

    # 최종 데이터 길이 출력
    print(f"Data after preprocessing: {len(data)} rows")

    return data
