# 4-6 pandas - lambda, map apply

#### Lambda 함수
- 한 줄로 함수를 표현하는 익명 함수 기법
- Lisp 언어에서 시작된 기법으로 오늘날 현대언어에 많이 사용
  
  ``` python
    def f(x,y):
        return x + y
  ```
  ->
     ```python
        f = lambda x,y : x + y
        f(1,4)
     ```

#### map 함수
- 함수와 sequence형 데이터를 인자로 받음
- 각 element마다 입력받은 한수를 적용하여 list로 반환
- 일반적으로 함수를 lambda형태로 표현함
- + python3 부터는 list 붙여줘야함
``` map(function, sequence) ```

- 두 개 이상의 argument가 있을 때는 두 개의 sequence형을 써야함
  ```python 
   f = lambda x, y : x + y
   list(map(f, ex, ex))
  ```

- 익명 함수 그대로 사용할 수 있음
  ``` list(map(lambda x: x+x, ex)) ```

#### map for series
- pandas의 series type의 데이터에도 map 함수 사용가능
- sunction 대신 dict, sequence형 자료등으로 대체 가능

``` python
    sl = Series(np.arange(10))
    sl.head(5)
```

``` python
    sl.map(lambda x: x**2).head(5)
```

- 할당 방법
1. dict 사용
``` python
   z = {1: 'A', 2: 'B'}
   sl.map(z).head(5)
```

1. 같은 위치의 데이터를 s2로 전환
```python
   s2 = Series(np.arange(10,20))
   sl.map(s2).head(5)
```

#### Replace function
- Map 함수의 기능 중 데이터 변환 기능만 담당
- 데이터 변환시 많이 사용하는 함수
``` python
df.sex.replace(
    {"male":0, 'female':1}
).head()
```
```python
df.sex.replace(
    ['male', 'female'],
    [0,1], inplace=True)
df.head(5)
```

+ inplace: 데이터 변환결과를 적용

#### apply for dataframe
- map과 달리, series 전체(column)에 해당 함수를 적용
- 입력값이 series 데이터로 입력받아 handling 가능

```python
f = lambda x : x.max() - x.min()
df_info.apply(f)
```
-> 각 column 별로 결과값 반환

- scalar 값 이외에 series값의 반환도 가능함
    (요약 정보를 위한 데이터 프레임 볼 수 있음)

#### applymap for dataframe
- series 단위가 아닌 element 단위로 함수를 적용함
- series 단위에 apply를 적용시킬 때와 같은 효과

-> series 단위에서는 map을/ dataframe 단위에서는 applymap을 주로 사용
