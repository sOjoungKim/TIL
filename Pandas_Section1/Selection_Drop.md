# 4-4 pandas - Selection & Drop

#### 한개의 column 선택 시 
```df["account"].head(3)```

#### 1개 이상의 column 선택 시
```df[["account", 'street', 'state']].head(3)```
-> 대괄호 2개

#### column 이름 없이 사용하는 index number는 row 기준 표시
``` df[:3] ```

#### column이름과 함꼐 row index 사용 시, 해당 column만
``` df['account'][:3] ```

#### Index 변경
``` python
df.index = df["account"]
del df["account"]
df.head()
```

#### Basic, loc, iloc selection
1. column과 index number
   ```df[['name', 'street']][:2]```

2. column number와 index number
   ```df.iloc[:2,:2]```
    -> ```df[['name', 'street']].iloc[:10]```

3. column과 index name
   ```df.loc[[211829,320563], ['name', 'street']]```

#### Drop
- 한 개 이상의 index number로 drop 시
  ```df.drop([0,1,2,3])```

- axis 지정으로 축을 기준으로 drop -> column 중에 'city'
  ``` df.drop('city', axis=1) ```

