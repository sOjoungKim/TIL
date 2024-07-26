# 2-1 The concepts of a feature

### 모델
``` y = ax + b ```

y : 종속변수   
x : 독립변수(feature)   
a,b : 알고리즘을 통해 찾은 최적값

### Feature
- 머신러닝에서 데이터의 특징을 나타내는 변수
- 독립변수, input 변수 등으로도 불림
- Table 상의 Data에서 Column(세로)을 의미
- data instance(실제 데이터)는 feature vector로 표현 -> 하나의 가로줄 데이터

### 표현법
| X 1 | X 2 | X 3 |
|--------|--------|--------|
| Y 1-1 | Y 1-2 | Y 1-3 |
| Y 2-1 | Y 2-2 | Y 2-3 |
| Y 3-1 | Y 3-2 | Y 3-3 |

- row 하나가 하나의 data instance -> feature vector로 표현
- col 하나가 하나의 feature 

#### 1. ``` y = w1x1 + w2x2 + w0*1 ```
: 위의 table의 모델 식

-> 이는 복잡하기 때문에 보통 벡터 형식으로 표현

$$
\vec{v^(1)} = \begin{pmatrix}
  1 \\
  0.00632 \\
  18
\end{pmatrix}
$$

$$
\vec{w} = \begin{pmatrix}
  w0 \\
  w1 \\
  w2
\end{pmatrix}
$$

+ 상수항은 항상 1로 써준다

#### 2. 

$$
x^{(i)}
$$

$$
x_{(j)}
$$
i: row의 index(num)
j: col의 index(num)

### 차원의 저주 (curse of dimensionality)
- 데이터의 차원이 증가할 수록(= feature가 증가할 수록) 데이터를 표현하는 공간이 증가함
  - 희박한 벡터가 증가(값이 없는 feature)
  - 샘플 데이터가 급속도로 늘어남
- 데이터 분포나 모델 추정의 어려움이 생김
    
