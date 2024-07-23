# 3-10 numpy data i/o

#### loadtxt & savetxt
: Text type의 데이터를 읽고, 저장하는 기능

1. 파일 호출
```python
    a = np.loadtxt("./populations.txt")
```
-> dtype로 type 설정 가능

2. int type 변환
```python
    a_int = a.astype(int)
```

3. int_data.csv로 저장
```python
    np.savetxt('int_data.csv',a_int, delimiter=",")
```
-> fmt : 프린트 포맷
-> delimiter : 구분자 설정

#### numpy object - npy
- Numpy object (pickle) 형태로 데이터를 저장하고 불러옴
- Binary 파일 형태로 저장함(이진)

```python
np.save("npy_test", arr=a_int)
```

```python
npy_array = np.load(file="npy_test.npy")
npy_array[:3]
```