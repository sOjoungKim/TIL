# seaborn
: 기초통계에서 배우는 기초 기법들을 visualization 하기 좋음
- matplotlib를 더 쉽게 사용할 수 있음
- matplotlib에 기본 설정을 추가
- 복잡한 그래프를 간단하게 만들 수 있는 warraper
- 간단한 코드 + 예쁜 결과

#### seaborn - basic plots
- matplotlib와 같은 기본적인 plot
- 손쉬운 설정으로 데이터 산출
- lineplot, scatterplot, countplot 등

- lineplot
    ```python
      sns.lineplot(x="timepoint", y="signal", data=fmri)
     ```
    + hue : 카테고리컬 데이터 표현

- scatterplot
    ```python
        sns.scatterplot(x="total_bill", y="tip", data=tips)
    ```
  - regplot: scatterplot에 직선형 그래프가 더해진 것

- countplot
    ```python 
    sns.countplot(x="smoker", data=tips)
    ```
    - estimator : 데이터의 분포 값을 표현

#### predefined plots
: matplotlib에 존재하지않음

- viloinplot : boxplot에 distribution을 함께 표현
- stripplot : scatter와 category 정보를 함께 표현
- swarmplot : 분포와 함께 scatter를 함께 표현
- pointplot : categor 별로 numeri의 평균, 신뢰구간 표시
- FacetGrid : 기본적인 그리드(판)이 생성됨

### + Seaborn과 Matplotlib의 차이
#### 1. 목적 및 사용 용도
- Matplotlib:
  - 기본적인 그래프 생성: Matplotlib은 다양한 유형의 그래프를 만들 수 있는 기본 도구입니다. 세부 조정이 가능하고, 고도로 맞춤화된 시각화를 만들 수 있습니다.
  - 유연성: 그래프의 거의 모든 요소를 세밀하게 제어할 수 있으며, 사용자 정의가 가능합니다.

- Seaborn:
  - 고급 통계적 그래프: Seaborn은 통계적 시각화를 더 쉽게 만들기 위해 Matplotlib 위에 구축되었습니다. 복잡한 데이터 분석과 시각화를 위한 고급 도구를 제공합니다.
  - 간단한 스타일링: 기본적으로 세련되고 일관된 스타일의 그래프를 생성할 수 있으며, 스타일을 통일하여 시각적으로 일관된 결과물을 만듭니다.

#### 2. 기능 및 특징
- Matplotlib:
  - 다양한 그래프 유형: 라인 플롯, 바 플롯, 히스토그램, 파이 차트 등 거의 모든 유형의 그래프를 그릴 수 있습니다.
  - 세부 조정 가능: 그래프의 각 요소 (축, 레이블, 색상 등)를 개별적으로 조정할 수 있습니다.

- Seaborn:
  - 통계적 그래프: 박스 플롯, 바이올린 플롯, 페어 플롯 등 통계적 데이터 분석에 유용한 그래프를 쉽게 생성할 수 있습니다.
  - 기본 통계 기능: 평균, 분산, 회귀선 등 통계적 분석 기능이 내장되어 있습니다.