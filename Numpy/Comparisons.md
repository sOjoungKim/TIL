# 3-8 numpy - comparisons
: 넘파이의 값들을 비교하는 것

#### All & Any
: Array의 데이터 전부 또는 일부가 조건에 만족하는지 여부를 판단

``` python
    a = np.arange(10)
    a<0
    >>>> array([False, False, False, False, False, False, False, False, False, False], dtype=bool)
```
-> broadcasting처럼 작동

#### Comparison operation #1 - Elment-wise operations과 비슷하다
: Numpy는 배열의 크기가 동일 할 때
      element간 비교의 결과를 Booleam type으로 반환하여 돌려줌

``` python
    test_a = np.array([1, 3, 0], float)
    test_b = np.array([5, 2, 1], float)
    test_a > test_b 
    >>> array([False,  True, False], dtype=bool)
```

#### Comparison operation #2
``` python
    a = np.array([1, 3, 0], float)
    np.logical_and(a > 0, a < 3) # and 조건의 condition
    >>>> array([ True, False, False], dtype=bool)
```

#### np.where
1.
```python
    np.where(a > 0, 3, 2) # where(condition, TRUE, FALSE)
    >>>> array([3, 3, 2])
```

2. 조건을 안적을 경우 - True인 값의 index값 출력
```python
    np.where(a>10)
    >>>> (array([6, 7, 8, 9]),)
```

#### argmax & argmin
    : array내 최대값 또는 최소값의 index를 반환함

```python
    a = np.array([1,2,4,5,8,78,23,3])
    np.argmax(a) , np.argmin(a)
    >>>> (5, 0)
```

- axis 기반의 반환
````python 
    a=np.array([[1,2,4,7],[9,88,6,45],[9,76,3,4]])
    np.argmax(a, axis=1) , np.argmin(a, axis=0)
    >>>> (array([3, 1, 1]), array([0, 0, 2, 2]))
````
