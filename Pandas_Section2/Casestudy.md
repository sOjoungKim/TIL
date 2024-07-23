# 5-3 Casestudy

#### 응용
- 
```python
df_phone.groupby(['month', 'item']).agg({'duration': [min],      # find the min, max, and sum of the duration column
                                     'network_type': "count", # find the number of network type entries
                                     'date': [min, 'first', 'nunique']}
 ```

- 
```python
grouped.add_prefix("duration_")
```
-> rename 방법