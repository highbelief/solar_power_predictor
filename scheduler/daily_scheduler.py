import logging
import schedule
import time
from datetime import datetime, timedelta
from data.data_loader import load_daily_data, preprocess_data
from model.train_model import train_model
from model.prediction import predict_next_day, save_prediction

# 로그 설정
logging.basicConfig(filename='predictor.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


# 매일 예측 작업
def daily_prediction_task():
    logging.info("Starting daily prediction task...")
    try:
        data = load_daily_data()
        processed_data = preprocess_data(data)

        # 학습 데이터 길이 출력
        print(f"Processed data length: {len(processed_data)}")

        if processed_data.empty:
            logging.error("No data available for training.")
            return

        model = train_model(processed_data)

        # 예측 시간대
        prediction_times = [6, 9, 12, 15, 18]
        next_day = datetime.now() + timedelta(days=1)

        for hour in prediction_times:
            observation_time = next_day.replace(hour=hour, minute=0, second=0, microsecond=0)
            predicted_power = predict_next_day(model, hour)
            save_prediction(observation_time, predicted_power)

        logging.info("Daily prediction task completed successfully.")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

    finally:
        # 여기에서 리소스 정리 작업 또는 추가 로그를 수행할 수 있습니다.
        logging.info("Daily prediction task finished.")


# 스케줄 시작
def start_scheduler():
    schedule.every().day.at("18:00").do(daily_prediction_task)
    while True:
        schedule.run_pending()
        time.sleep(60)
