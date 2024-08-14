# Feature Engineering

#### Feature Engineering
: 가장 적합한 특성을 찾는 것

1. Generation
   1. Binarization, Quantization
   2. Scaling ...
2. Selection
   1. Univariate statics
   2. Model-based selection

#### 1. Generation - Log transformation
   1. 데이터의 분포가 극단적으로 모였을 때
   2. 선형 모델은 데이터가 정규분포 때 적합
   3. Poisson -> Normal distribution
-> np.log 사용 
```X_test_log = np.log(X_test + 1)```
