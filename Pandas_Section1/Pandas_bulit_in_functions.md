# 4-7 pandas - Pandas builit-in functions

#### describe 
- Numeric type 데이터의 요약 정보를 보여줌
  -> count, ment, std, min, 25% 등

#### unique
: 유일한 값(고유한 값) 찾기
-> 데이터의 종류들을 알고 싶을 때 주로 사용
ex) 성씨 column에서 존재하는 성의 종류 빼내기

```python
df.race.unique()
```
```python
dict(enumerate(sorted(df["race"].unique())))
```
```python
value = list(map(int, np.array(list(enumerate(df["race"].unique())))[:, 0].tolist()))
key = np.array(list(enumerate(df["race"].unique())), dtype=str)[:, 1].tolist()

value, key
```

#### sum
- 기본적인 column 또는 row 값의 연산을 지원
- sub, mean, min, max, mad, var 등
- axis로 축 정할 수 있음
- cumsum : 점점 증가하는 표현, (2col+3col, 3col+4col)

#### isnull
- column 또는 row 값의 NaN(null) 값의 index를 반환함
-> 결측치 확인 시 사용
``` df.isnull() ```

#### sort_values
- column 값을 기준으로 데이터를 sorting
  - ascending -> 오름차순

#### Correlation & Covariance
- 상관계수와 공분산을 구하는 함수
- corr, cov, corrwith
