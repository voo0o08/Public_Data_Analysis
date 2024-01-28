# 최대 무임 승차 비율 확인
import csv

f=open("subwayfee.csv", encoding="utf-8-sig")
data = csv.reader(f)
header = next(data)
rate = 0
max_rate = 0

for row in data:
    for i in range(4, 8):
        row[i] = int(row[i])

    if row[6] != 0:                   # 무임승차 0인 애들 출력
        rate = row[6] * 100 / (row[6] + row[4]) # 무임승차 0이면 그냥 1이 rate
        if rate > max_rate:
            max_rate = rate
            print(row, round(rate, 2), "%")

f.close()