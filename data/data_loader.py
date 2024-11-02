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
    return data


# 데이터 전처리
def preprocess_data(data):
    data = data.dropna()
    data['hour'] = data['observation_time'].dt.hour
    return data
