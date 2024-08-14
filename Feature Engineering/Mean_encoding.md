# Mean encoding

- Category 데이터는 항상 One-hot encoding
  - X, 다양한 인코딩 기법이 있음
-  대표적인 방법으로 Y값에 대한 분포를 활용한 Mean Encoding이 사용됨

- Label 인코딩은 그 자체로 정보가 존재하지 않음
  - 분포의 값을 취할 수 있음

1. Regression Task는 단순 평균값욿 입력
2. Overfitting을 제거하기 위해 smoothing을 사용


# Interaction features
- 기존 feature들의 조합으로 새로운 feature 생성
- Data에 대한 사전 지식과 이해가 필요
- Polynomial feature를 사용한 자동화 가능 -> 높은 비용
- 실험적으로 접근할 요소들은 있음 -> 자동화 코드
- weight + time-period, sensor1 + sensor2

Etc
- Feature 끼리 더하기, 곱하기, 나누기 등등
- 왜 잘 되는지 모르는데 잘 되는 경우가 있음
- 도메인 지식과 EDA로 좋은 Feature들을 생성
  