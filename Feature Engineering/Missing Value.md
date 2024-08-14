# Missing Value

### 결측치를 어떻게 처리할거냐?

#### Missing Value Strategy
- 데이터가 없으면 sample을 drop
- 데이터가 없는 최소 개수를 정해서 sample을 drop
- 데이터가 거의 없는 feature는 feature 자체를 drop
- 최빈값, 평균값으로 비어있는 데이터를 채우기

#### Data drop
- ``` df.dropna(how='all') ``` -> 모든 데이터가 비어 있으면 drop
- ``` df.dropna(axis=1, how='all') ``` -> column 기준으로 삭제
- ``` df.dropna(axis=1, thresh=3) ``` -> 데이터가 최소 4개 이상 없을 때 drop

### 데이터 값 채우기
- 평균값, 중위값, 최빈값을 활용
- 분포를 보고 판단(평균값과 최빈값이 일반적)
- ex. ```df['preTestScore'].fillna(df['preTestScore'].mean(), inplace=True)```
- ```df['postTestScore'].fillna(df.groupby("sex")['postTestScore'].transform('mean'), inplace=True)```

#### ++ transform() 메서드
: 입력된 객체와 동일하게 인덱스 된 객체를 반환한다.
- 사용자에게 하나하나 하기보다는 동일한 시간대에 다중연산을 가능하게 한다.
- .agg() 매서드와 꽤나 유사한면이 있으나 다음과 같은 차이가 있다.
  - agg() 메서드는 sum, mean 등 집계하는 함수 위주로 적용된다.
  - transform() 메서드는 각 요소별로 적용되는데 적용된다.
- apply와의 차이점
![Alt text](<../img/스크린샷 2024-08-08 오후 5.28.42.png>)