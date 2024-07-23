# Time shifting

#### Time shifting
- 시간의 차(Time Lag) 분석 필요
    - 예) 30일전에 비해 주가는 상승세인가?
- Pandas내 Time shifting 기능으로
  - time window를 기준으로 기간간 차이

```python
    monthly_avg.shift(periods=2, fill_value=0)
```
-> 데이터를 두 칸씩 밀어라 !

#### Moving average
- 시계열 데이터는 노이즈 발생
  - 노이즈를 줄이면서 추세보기, 이동평균법

- rolling
```python
    monthly_mean_shift = monthly_mean.rolling(
        window=30, ).mean()
```
-> 30일 치 평균으로 추세선을 그랴라

#### Cumsum
- 시계열 데이터를 window 마다 합침
- rolling(window=10).sum()과 다름

```python
    monthly_mean = df["count"].resample('M').mean()
    cumsum = monthly_mean.cumsum()
```
-> 적층해서 쌓는것, rolling이랑 다름

#### Secondary axis
```python
ax = df_monthly.plot(y='count', use_index=True)
df_monthly.plot(
    y='cumsum', secondary_y=True,
    ax=ax, use_index=True, figsize=(20,10)
)
```
