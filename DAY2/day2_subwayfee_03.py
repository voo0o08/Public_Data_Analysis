# 무임승차 인원이 0인 역 찾기

import csv

f=open("subwayfee.csv", encoding="utf-8-sig")
data = csv.reader(f)
header = next(data)
rate = 0

for row in data:
    # ['사용월', '호선명', '역ID', '지하철역', '유임승차', '유임하차', '무임승차', '무임하차']
    for i in range(4, 8): # 유임승차부터만 사용
        row[i] = int(row[i])
    rate = row[4] / (row[6] + row[4]) # 무임승차 0이면 그냥 1이 rate

    if row[6] == 0:                   # 무임승차 0인 애들 출력
        print(row)

f.close()