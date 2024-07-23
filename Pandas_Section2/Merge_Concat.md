# 5-5 Merge & Concat

#### Merge
- SQL에서 많이 사용하는 Merge와 같은 기능
- 두 개의 데이터를 하나로 합침

```python
pd.merge(df_a, df_b, on='subject_id')
```
-> subject_id 기준으로 합병

- 두 datafrme이 column 이름이 다를 떄
```python
pd.merge(df_a, df_b, left_on='subject_id', right_on='subject_id')
```

#### merge - join method
1. INNER JOIN
2. OUTER JOIN (FULL)
3. LEFT JOIN
4. RIGHT JOIN

#### merge - Index based join
-> key value가 없을 경우 index를 기준으로 join이 되는 것

#### Concat
- 같은 형태의 데이터를 붙이는 연산작업

