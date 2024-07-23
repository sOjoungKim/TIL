# 4-3 pandas - DataFrame

#### DataFrame => Series의 모음

#### 데이터 추출
1. loc : index location
2. iloc : index position

-> loc은 index 이름, iloc은 index number

#### column에 새로운 데이터 할당 - 조건
```python
    df.debt = df.age > 40
    df
```

#### transpose
```python
df.T
```

#### 값 출력
```python
df.values
```

#### csv 변환
```python
df.to_csv()
```

#### column을 삭제함
```python
del df['debt']
```
