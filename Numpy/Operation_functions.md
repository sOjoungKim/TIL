# 3-6 numpy - operation functions

#### axis
    : 모든 operation function을 실행할 떄 기준이 되는 dimension 축

```python 
    test_array.sum(axis=1), test_array.sum(axis=0)
    >>>> (array([10, 26, 42]), array([15, 18, 21, 24]))
```
+ 차원이 증가할수록 기존 차원에 할당되는 axis의 값이 밀린다 (증가한다)

#### mean & std
    : ndarray의 element들 간의 평균 또는 표준 편차를 반환

#### concatenate
    : Numpy array를 합치는 함수
#####  1. vstack  : 수직적으로 합치기
``` python
    a = np.array([1,2,3])
    b = np.array([2,3,4])
    np.vstack((a,b))
    >>>> array([[1, 2, 3],
                [2, 3, 4]])
```

##### 2. hstack : 수평적으로 합치기

##### 3. concatenate : 한 번에 합치기

``` python 
    a = np.array([[1, 2, 3]])
    b = np.array([[2, 3, 4]])
    np.concatenate( (a,b) ,axis=0)
```
