---

# Solar Power Plant Generation Prediction AI

## 프로젝트 개요
이 프로젝트는 **대학교 캡스톤 디자인** 과목을 위한 태양광 발전소 발전량 예측형 AI 시스템입니다. 이 시스템은 태양광 발전소의 하루치 발전 데이터를 바탕으로, 다음 날 특정 시간대(오전 6시, 9시, 12시, 오후 3시, 6시)의 발전량을 예측하여 효율적인 에너지 관리와 운영 계획에 도움을 주는 것을 목표로 합니다.

> **⚠️ 주의사항**
> - 본 프로젝트는 **교육 목적 및 공익 목적 외의 사용을 금지**합니다.
> - 본 프로젝트의 사용으로 발생하는 모든 책임은 **사용자 본인**에게 있으며, 제작자는 이에 대해 책임지지 않습니다.

## 주요 기능
- 하루치 태양광 발전소 데이터를 활용하여 다음 날 발전량을 예측
- 매일 오후 6시에 자동으로 데이터를 수집하고 모델을 학습하여 예측값을 생성
- 예측된 발전량과 상태 정보를 데이터베이스에 저장

## 설치 방법

### 1. 의존성 설치
프로젝트를 실행하기 위해 필요한 패키지를 설치합니다.

```bash
pip install -r requirements.txt
```

### 2. 데이터베이스 설정
MySQL 데이터베이스를 설정하고, 아래의 SQL을 통해 `solar_user` 계정과 `SolarDB` 데이터베이스를 생성하세요.

```sql
CREATE USER 'solar_user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON SolarDB.* TO 'solar_user'@'localhost';
FLUSH PRIVILEGES;
```

### 3. 테이블 생성
다음 SQL을 통해 `simulation_data` 및 `predictions` 테이블을 생성합니다.

```sql
CREATE TABLE simulation_data (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    observation_time TIMESTAMP NOT NULL,
    temperature DOUBLE,
    solar_irradiance DOUBLE,
    humidity DOUBLE,
    cloud_coverage DOUBLE,
    equipment_status VARCHAR(255),
    power_generated DOUBLE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE predictions (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    observation_time TIMESTAMP NOT NULL,
    predicted_power_generated DOUBLE,
    predicted_battery_level DOUBLE,
    predicted_equipment_status VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 사용 방법

1. **데이터 수집**: `simulation_data` 테이블에 발전 데이터를 수집하여 입력합니다.
2. **모델 학습 및 예측**: 매일 오후 6시에 스케줄러가 작동하여 그날 수집된 데이터를 바탕으로 모델을 학습하고, 다음 날 발전량을 예측합니다.
3. **결과 확인**: 예측된 발전량은 `predictions` 테이블에 저장되며, 각 예측 시간대별 예측 발전량, 배터리 상태 및 장비 상태가 기록됩니다.

## 파일 구조
```plaintext
solar_power_predictor/
├── config/
│   └── database_config.py       # 데이터베이스 연결 설정
├── data/
│   └── data_loader.py           # 데이터 수집 및 전처리
├── model/
│   ├── train_model.py           # 모델 학습
│   └── prediction.py            # 예측 수행
├── scheduler/
│   └── daily_scheduler.py       # 스케줄 설정 및 실행
├── main.py                      # 프로젝트의 메인 실행 파일
└── requirements.txt             # 필요한 라이브러리 목록
```

## 주의사항
- 이 프로젝트는 **교육 목적**과 **공익 목적**을 위해 제작되었으며, 그 외의 사용을 금합니다.
- 본 프로젝트의 사용으로 발생하는 모든 책임은 **사용자 본인**에게 있으며, 제작자는 이에 대해 **책임을 지지 않습니다**.

---
