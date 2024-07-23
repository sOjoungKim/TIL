# 4-2 pandas - series

#### Pandas의 구성
- DataFrame : Data Table 전체를 포함하는 Object
- Series : DataFrame 중 하나의 Column에 해당하는 데이터의 모음 Object
  - index name
    ```python
        list_data = [1,2,3,4,5]
        list_name = ["a","b","c","d","e"]
        example_obj = Series(data = list_data, index=list_name)
        example_obj
    ```

  - 값 리스트만
    ```python
        example_obj.values
        >>>> array([1, 2, 3, 4, 5])
    ```

  - 인덱스 리스트만
  ```python 
        example_obj.index
        >>>> Index(['a','b','c'], dtype = 'object')
  ```

  - 인덱스 라인 네임 지정
  ```python
    example_obj.index.name = "alphabet"
  ```