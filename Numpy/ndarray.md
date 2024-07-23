# 3-2 numpy - ndarray

### Array creation
``` test_array = np.array([1,4,5,8], float) ```
- numpy는 np.array 함수를 활용하여 배열을 생성함 -> ndarray
- numpy는 하나의 데이터 type만 배열에 넣을 수 있음
- List와 가장 큰 차이점, Dynamic typing not supported
- C의 Aarry를 사용하여 배열을 생성함

### Array shape
+ type: tuple

#### vector
```python
    vector = np.array([1,4,5,"8"], float)
    vector
    >>> (4,)
```

#### matrix
```python
    matrix = [[1,2,4,8],[1,2,5,8],[1,2,5,8]]
    np.array(matrix, int).shape
    >>> (3,4)
```

#### 3rd order tensor
```python
    tensor  = [[[1,2,5,8],[1,2,5,8],[1,2,5,8]], 
               [[1,2,5,8],[1,2,5,8],[1,2,5,8]], 
               [[1,2,5,8],[1,2,5,8],[1,2,5,8]], 
               [[1,2,5,8],[1,2,5,8],[1,2,5,8]]]
    np.array(tensor, int).shape
    >>> (4, 3, 4)
```

### ndim & size
```python
    tensor  = [[[1,2,5,8],[1,2,5,8],[1,2,5,8]], 
               [[1,2,5,8],[1,2,5,8],[1,2,5,8]], 
               [[1,2,5,8],[1,2,5,8],[1,2,5,8]], 
               [[1,2,5,8],[1,2,5,8],[1,2,5,8]]]

    #1. ndim
    np.array(tensor, int).ndim
    >>> 3
    #2. size
    np.array(tensor, int).size
    >>> 48
```
- ndim : number of dimension
- size : data의 개수

### Array dtype
``` python
    np.array([1,2,3],[4.5,5,6], dtype=int)
```

- Ndarray의 single element가 가지는 data type
- 각 element가 차지하는 memory의 크기가 결정됨
- C의 data type과 compatible
