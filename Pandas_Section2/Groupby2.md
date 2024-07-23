# 5-2 Groupby II

#### Grouped
: Groupby에 의해 Split된 상태를 추출 가능함
-> Tuple 형태로 그룹의 key 값 Value값이 추출됨

``` python
grouped = df.groupby("Team")
```
```python
for name,group in grouped:
    print (type(name))
    print (type(group))
```

- 특정 key값을 가진 그룹의 정보만 추출 가능
  ``` grouped.get_group("Riders") ```

- 추출된 group 정보에는 세 가지 유형의 apply가 가능함
  - 1. Aggregation: 요약된 통계 정보를 추출해 줌
  - 2. Transformation: 해당 정보를 변환해줌
  - 3. Filtration: 특정 정보를 제거하여 보여주는 필터링 기능
  
   1. Aggregation
    ``` grouped['Points'].agg([np.sum, np.mean, np.std]) ```

    2. Transformation
    - Aggregation과 달리 key값 별로 요약된 정보가 아님
    - 개별 데이터의 변환을 지원함
    ```python
    score = lambda x: (x - x.mean()) / x.std()
    grouped.transform(score)
    ```

    3. filter
    - 특정 조건으로 데이터를 검색할 때 사용
      - 안에 boolean 조건이 존재해야함
      - len(x)는 grouped된 dataframe 개수
  
  ```df.groupby('Team').filter(lambda x: len(x) >= 3)```

  