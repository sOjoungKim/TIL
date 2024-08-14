# Category_Data

#### 이산형 데이터를 어떻게 처리할까?
 ##### -> One-Hot Encoding !
ex. {Green, Blue, Yellow}
--> {Green} = [1,0,0]
- ```get_dummies()``` 사용

##### ++ get_dummies()
1. 모든 데이터를 수치로 변환해주는 전처리 작업은 필수적이다.
2. 하지만 수치형 데이터로만 바꾸면 서로 간의 관계성이 생기게된다. (월요일=1, 화요일=2, 1+2=3)
3. 이렇게 수치화 된 데이터를 가변수화 해주면 관계성이 없어진다.
4. 이에 pandas는 손 쉽게 더미의 가변수를 만들 수 있도록 get_dummies함수를 제공한다.
![Alt text](<../img/스크린샷 2024-08-08 오후 8.14.13.png>)

#### 데이터의 구간을 나누기
  ##### -> Data Binning ! 
  ##### Label encoding by sklearn
- scikit-learn의 preprocessing 패키지도 label, one-hot 지원
