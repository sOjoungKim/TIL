# Time series data

#### Time series in Pandas
- 시간에 특화된 Groupby 기능이 필요함
  예: 데이터 중 주말 통계만 필요함
- Time lag 또는 Moving Average는 계산

#### datatime 모듈을 활용
- DataTime Index 만들기
  - 대부분의 데이터는 str으로 되어 있음
    - 호출 후 DateTime index로 변환이 필요함
```python
    df['datetime'] = pd.to_datetime(df['date'])
```
```python
    df = pd.read_csv("abc.txt", encoding="cp949", sep="Wt").T[1:].reset_index()
    df = df. rename(columns={"index":"date", 0:"지표", 1:"수치"})
    df["date"] = df["date"].str.split(".").map(rename_date)
```

#### datatime 형식 변경
```python
    df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
```

#### + 값 type 변경
```python
    df["수치"].astype(float)
```
