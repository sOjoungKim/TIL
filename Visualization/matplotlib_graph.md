# matplotlib_graph

#### scatter
- 산점도
    - marker : scatter 모양지정
```python
  plt.scatter(data_1[:,0],data_1[:,1], c="b", marker="x")
```

#### bar chart
```python
    plt.bar(X, data[i], bottom = np.sum(data[:i], axis=0), color = color_list[i], label=data_label[i])
```
-> X만 입력시 위로 쌓임, X=0.5 등 간격 설정 시 옆으로 나열

#### barh chart
- horizontal bar 형식
```python
    plt.barh(X, women_pop, color="r")
    plt.barh(X, -men_pop, color="b")
```

#### hisrogram
```python
    plt.hist(X, bins=100)
```

#### boxplot
```python
    plt.boxplot(data)
```
