import pandas as pd

# CSV 파일에서 데이터 읽기
df = pd.read_csv('employee_data.csv')
#print(df.head())  # 데이터의 처음 5행을 출력
# 데이터프레임의 정보 확인
#print(df.info())

# 통계 요약 정보
print(df.describe())
print(df.head())

names = df['이름']
print(names.head())

sorted_df = df.sort_values(by='나이',ascending=False) #내림 차순으로 정렬(나이가 많은 것부터 정렬)
print(sorted_df.head())











