# Resampling

- 시간 기준으로 데이터 Aggregation
- Groupby와 유사
    - 훨씬 간단하고 다양한 기능 제공

- 고정적인 시계열 데이터 문제
  - 시각화와 전처리에 용이함

#### Data 불러오기
```python
    df = pd.read_csv(
        os.path.join(DATA_DIR, "train.csv"),
        parse_dates = ['datatime']
    )
    df.set_index("datetime", inplace=True)
    df.head()
```

#### GroupBy로 월별 데이터 불러오기
```python
    df["month"] = df.index.month
    df["year"] = df.index.year
    df.groupby(["year", "month"])["count"].sum().reset_index
```

#### Resampling
```python
    df["count"].resample('Q').sum()
    df["count"].resample('M').sum()
    df["count"].resample("D").sum()
    df["count"].resample("W").sum()
```
-> groupby보다 쉬운 방법

#### Resampling - Filter
- something_range 함수로 기간 생성
```python
    period = pd.date_range(
        start = '2011-01-01', end='2011-05-31', freq='M'
        df['count'].resample('M').sum()[period]
    )
```
-> 다른 방법으로
1. timedelta_rnge
2. period_range
3. interval_range
