import pandas as pd

# CSV 파일에서 데이터 읽기
df = pd.read_csv('employee_data.csv')
#print(df.head())  # 데이터의 처음 5행을 출력
# 데이터프레임의 정보 확인
#print(df.info())

# 통계 요약 정보
print(df.describe())