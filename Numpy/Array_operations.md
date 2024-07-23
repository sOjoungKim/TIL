# 3-7 numpy - array operations

#### Operations b/t arrays
: Numpy는 array간의 기본적인 사칙 연산을 지원함

#### Elment-wise operations
: Array간 shape이 같을 때 일어나는 연산

``` python
    matrix_a = np.arange(1,13).reshape(3,4)
    matrix_a * matrix_a
    >>>> array([[  1,   4,   9,  16],
                [ 25,  36,  49,  64],
                [ 81, 100, 121, 144]])
```

#### Dot product
: Matrix의 기본 연산
    -> dot 함수 사용

``` python
    test_a = np.arange(1,7).reshape(2,3)
    test_b = np.arange(7,13).reshape(3,2)
    test_a.dot(test_b)
    >>>> array([[ 58,  64],
                [139, 154]])
```

#### transpose
: transpose 또는 T attribute 사용

#### broadcasting
: Shape이 다른 배열 간 연산을 지원하는 기능
    -> 중요한 개념, 어느정도는 크기가 비슷해야함. 
       자동으로 계산함

```python
    test_matrix = np.array([[1,2,3],[4,5,6]], float)
    scalar = 3
    test_matrix + scalar # Matrix - Scalar 덧셈
    >>>> array([[ 4.,  5.,  6.],
                [ 7.,  8.,  9.]])
```

#### %timeit
: 계산 속도 확인