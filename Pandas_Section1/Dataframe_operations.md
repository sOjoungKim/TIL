# 4-5 pandas - Dataframe operations

#### Series operation
: series는 numpy에 index를 넣어준 꼴

#### dataframe operation
: numpy의 matrix
index에 더불어 column도 존재

#### Series + Dataframe
```python
df = DataFrame(
    np.arange(16).reshape(4,4), 
    columns=list("abcd"))
df
```
```python
s = Series(
    np.arange(10,14), 
    index=list("abcd"))
s
```
```
df + s
```
-> column을 기준으로 broadcasting이 발생함

- index가 맞지 않는 등 기본적이지않은 경우
  -> axis를 기준으로 row broadcasting 실행
  ``` df.add(s2, axis=0) ```

