# Feature_scaling

#### 두 변수 중 하나의 값의 크기가 너무 크다면?

### Feature scaling 전략
1. Min-Max Normalization
   - 기존 변수에 범위를 새로운 최대-최소로 변경
   - 일반적으로 0과 1사이 값으로 변경
![Alt text](image.png)

2. Standardization (Z-score Normalization)
   - 기존 변수에 범위를 정규 분포로 변환
   - 실제 Min-Max의 값을 모를 때 활용 가능
  ![Alt text](<../img/스크린샷 2024-08-08 오후 8.23.28.png>)

### Feature scaling with sklearn
- Label encoder와 마찬가지로, sklearn도 feature scale 지원
- MinMaxScaler와 StandardScaler 사용
 ```python
 from sklearn import preprocessing
 std_scale = preprocessing.StandardScaler().fit(
    df[['Alcohol', 'Malic acid']])
 df_std = std_scale.transform(df[['Alcohol', 'Malic acid']])
 df_std[:5]
 ```

- Preprocessing은 모두 fit -> transform의 과정
- 이유는 label encoder와 동일함
- 단, scaler는 한번에 여러 column을 처리 가능