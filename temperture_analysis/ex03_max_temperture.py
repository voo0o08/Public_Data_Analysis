'''
서울의 최고 기온과 날짜를 알아보자
['날짜', '지점', '평균기온(℃)', '최저기온(℃)', '최고기온(℃)']
'''
import csv
f = open("seoul_clean.csv")
data = csv.reader(f)
head = next(data)
print(head)
max_temp = -999
max_day = ""
for row in data:
    if row[-1] == "":
        row[-1] = -999 # 최고 기온 구할거니까 낮은 값 아무거나!
    row_tmep = float(row[-1])
    if row_tmep > max_temp:
        max_temp = row_tmep
        max_day = row[0]
f.close()
print(f"서울의 최고 기온은 {max_day} {max_temp}입니다.")


