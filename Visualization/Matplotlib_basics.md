# Visualization - Matplotlib_basics

## Matplotlib
- 데이터가 어떻게 생겼는지 보여주기 위함
- 파이썬의 대표적인 시각화 도구
- Graph는 원래 figure 객체에 생성됨
- pyplot 객체 사용시, 기본 figure에 그래프가 그려짐 -> 적층이 되는 구조

#### 기본 사용법
- pyplot 객체를 사용하여 데이터를 표시
- pyplot 객체에 그래프들을 쌓은 다음 flush

```python
    # 1. plt로 불러오기
    import matplotlib.pyplot as plt
```

- 단점
    - 최대 단점 argument를 kwargs 받음
    - 고정된 argument가 없어서 alt+tab으로 확인이 어려움

#### Figure & Axes
- Matplotlib는 Figure 안에 Axes로 구성
- Figure 위에 여러 개의 Axes를 생성
  - Figure은 도화지, Axes는 그림판

```python
    fig = plt.figure() # figure 반환
    fig.set_size_inches(10,5) # 크기지정
    ax_1 = fig.add_subplot(1,2,1) # 두개의 plot 생성 (n번째 줄에, z개의 칸이 있는데, 그 중 x번째 칸이다.)
    ax_2 = fig.add_subplot(1,2,2) # 두개의 plot 생성

    ax_1.plot(X_1, Y_1, c="b") # 첫번째 plot
    ax_2.plot(X_2, Y_2, c="g") # 두번째 plot
    plt.show() # show & flush
```

#### Set color
- Color 속성을 사용
- Float -> 흑백, rgb, predefined color 사용
``` python
    plt.plot(X_2, Y_2, color="#0000")
```

#### Set linestyle
- ls 또는 linestyle 속성 사용
``` python
    plt.plot(X_2, Y_2, linestyle="dashed")
    plt.plot(X_2, Y_2, ls="dotted")
```

#### Set title
- Latex 타입의 표현도 가능 (수식 표현 가능)
```python
    plt.title('$y = ~~')
```

#### Set legend
- Legend 함수로 범례를 표시함, loc 위치 등 지정

#### Set grid & xylim
- Graph 보조선을 긋는 grid와 xy축 범위 한게를 지정
```python
    plt.grid(True, lw=0.4, ls="--", c=".90")
```
