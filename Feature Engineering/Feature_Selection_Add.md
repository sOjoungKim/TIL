# Feature_Selection
: 가장 적합한 특성을 선택하는 방법

- 모든 festure 들이 반드시 model 학습에 필요치 않음
- 어떤 feature들은 성능을 오히려 나쁘게 함
- 너무 많은 feature -> overfitting의 원인
- 모델에 따라서 필요한 feature를 선택함
- 필요없는 feature 제거 -> 학습 속도와 성능 향상
- 다양한 기법과 코드에 대해 공부

#### feature 선택의 주의 사항들
- prediction time에도 쓸 수 있는 feature인가?
- 실시간 예측이 필요할 때, 생성이 너무 고비용이 아닌가?
- scale은 일정한가? 또는 비율적으로 표현 가능한가?
- 새롭게 등장하는 caregory data는? 가장 비슷한가
- 너무 극단적인 분포 -> threshold(한계점) 기반으로 binarization

#### 이런 feature들은 삭제하자!
- Correlation이 너무 높은 Feature들은 삭제
  - 서로 연관된 두개의 feature 중 하나는 제거**
- 전처리가 완료됨 str feature들
- ID와 같은 성향을 가진 Feature들

# Model & Trainning
- 적합한 모델을 선정한다(실험)
- 모델에 적합한 하이퍼 파라메터를 선정한다(실험)
- 다양한 전처리 경우의 수를 입력한다(실험)
- 학습을 실행한다
- 성능을 평가한다
