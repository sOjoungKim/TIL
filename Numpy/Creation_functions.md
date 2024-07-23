# 3-5 numpy - creation functions

#### arange
- array의 범위를 지정하여, 값의 list를 생성하는 명령어
``` np.arange(30) ```
``` np.arange(0, 5, 0.5) ``` -> floating point도 표시 가능

#### zeros
    : 0으로 가득 찬 ndarray 생성

#### ones
    : 1로 가득찬 ndarray 생성

#### empty
    : shape만 주어지고 비어있는 ndarray 생성 (memory initialization이 되지 않음)

``` np.empty(shpae=(10,), dtype=np.int8) ```

#### something_like
    : 기존 ndarray의 shape 크기 만큼 1,0 또는 empty array를 반환

``` np.ones_like(test_matrix) ```

#### identity
    : 단위 행렬을 생성

#### eye
    : 대각선이 1인 행렬 (k값의 시작 index의 변경 가능)

#### diag
    : 대각 행렬의 값을 추출함 (k값의 시작 index의 변경 가능)

#### random sampling
    : 데이터의 분포에 따른 sampling으로 array를 생성

1. 균등분포
   ``` np.random.uniform(0,1,10).reshape ```

2. 정규분포
   ``` np.random.normal(0,1,10).reshape(2,5) ```
