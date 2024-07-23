# 5-1 Groupby I

#### Groupby
- SQL groupby 명령어와 같음
- split -> apply -> combine 
- 과정을 거쳐 연산함
  
  ``` df.groupby("Team")["Points"].sum() ```

   - 한 개 이상의 column을 묶을 수 있음
  ``` h_index = df.groupby(["Team", "Year"])["Points"].sum() ```

#### Hierarchical index
- 위의 한 개 이상의 col을 묶었을 때를 의미하는 것
- Groupby 명령의 결과물도 결국은 dataframe
- 두 개의 column으로 groupby를 할 경우, index가 두 개 생성

  - ** unstack()
    - Group으로 묶여진 데이터를 matrix 형태로 전환해줌
        ``` h_index.unstack() ```

  - swaplevel
    - index level을 변경할 수 있음
  
  - index level을 기준으로 기본 연산 수행 가능
        ``` h_index.sum(level = 0) ```
