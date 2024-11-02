from sqlalchemy import create_engine

# 데이터베이스 연결 설정
def get_db_engine():
    user = 'solar_user'
    password = 'password'
    host = 'localhost'
    db_name = 'SolarDB'
    engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{db_name}")
    return engine
