# 5-4 Pivot table & Crosstab

#### pivot table
- 우리가 Excel에서 보던 그 것!
- Index 축은 groupby와 동일함
- Column에 추가로 labelling 값을 추가하여, 
- Value에 numeric type 값을 aggregation 하는 형태

```python
df_phone.pivot_table(["duration"],
                     index=[df_phone.month,df_phone.item], 
                     columns=df_phone.network, aggfunc="sum", fill_value=0)
```
-> duration을 가로축으로 기준잡고 정렬 & month를 세로축으로

#### Crosstab
- 특히 두 칼럼에 교차 빈도, 비율, 덧셈 등을 구할 떄 사용
- Pivot table의 특수한 형태
- User-Item Rating Matrix 등을 만날 때 사용가능함

```python
df_movie.pivot_table(["rating"], index=df_movie.critic, columns=df_movie.title,
                     aggfunc="sum", fill_value=0)
```
-> pivot table, groupby 명령어로도 가능
- pivot table
```python
df_movie.pivot_table(["rating"], index=df_movie.critic, columns=df_movie.title,
                     aggfunc="sum", fill_value=0)
```

- gruopby
```python
df_movie.groupby(["critic","title"]).agg({"rating":"first"}).unstack().fillna(0)
```

--> 이 세개는 사실상 비슷하지만 용도에 따라 다르게 쓰임