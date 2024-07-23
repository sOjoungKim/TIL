# pandas matplotlib
- matplotlib를 사용한 그래프 지원
- Dataframe, series 별로 그래프 작성 가능

- 데이터간의 상관관계를 볼 때 scatter graph 사용 가능
```python
    fig = plt.figure()
    ax = []
    for i in range(1,5):
        ax.append(fig.add_subplot(2,2,i))
    ax[0].scatter(df_data["CRIM"], df_data["MEDV"])
    ...
```

- matplotlib의 꾸미기 함수 그대로 사용함

#### plot function
- plot 함수를 사용하면 전체 데이터의 graph를 그림
  - kind : plot 종류
  - x: x축 컬럼
  - y: y축 컬럼
```python
    df.plot(kind="scatter", x="num_c", y="num_p", color="red")
    plt.show()
```
-> 일반적으로 "쉽게" 데이터를 보여주는 방법

#### Scaled boxplot
  - 스케일링 후 적용
#### Scatter matrix 
  - diagonal = "kde"
    - 데이터의 상관관계를 보여줌(분포)

#### matshow
: matrix show, hit map 보여줌
