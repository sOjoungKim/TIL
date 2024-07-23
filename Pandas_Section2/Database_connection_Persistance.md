# 5-6 Database connection & Persistance

#### Database connection
- Data loading시 db connection 기능을 제공
  - Database 연결 코드
  ```python
  import sqlite3 #pymysql <- 설치

  conn = sqlite3.connect("./data/flights.db")
  cur = conn.cursor()
  cur.execute("select * from airlines limit 5;")
  results = cur.fetchall()
  results
  ```

#### XLS persistence
- Dataframe의 엑셀 추출 코드
- Xls 엔진으로 openpyxls 또는 XlsxWrite 사용

```python
writer = pd.ExcelWriter('./data/df_routes.xlsx', engine='xlsxwriter')
df_routes.to_excel(writer, sheet_name='Sheet1')
```

#### pickle persistence
- 가장 일반적인 python 파일 persistence
- to_pickle, read_pickle 함수 사용
``` df_routes_pickle.describe() ```

+++ pickle
: pickle 모듈은 파이썬 객체 구조의 직렬화와 역 직렬화를 위한 바이너리 프로토콜을 구현합니다. “피클링(pickling)”은 파이썬 객체 계층 구조가 바이트 스트림으로 변환되는 절차이며, “역 피클링(unpickling)”은 반대 연산으로, (바이너리 파일 이나 바이트열류 객체로 부터의) 바이트 스트림을 객체 계층 구조로 복원합니다. 피클링(그리고 역 피클링)은 “직렬화(serialization)”, “마샬링(marshalling)” [1] 또는 “평탄화(flattening)” 라고도 합니다; 그러나, 혼란을 피하고자, 여기에서 사용된 용어는 “피클링” 과 “역 피클링” 입니다.