# 유임 승차 비율이 50% 이하인 역
import csv
import matplotlib.pyplot as plt
import platform

f=open("subwayfee.csv", encoding="utf-8-sig")
data = csv.reader(f)
header = next(data)
print(header)

max_rate = 100
max_row = []
max_total_num = 0

for row in data:
    # ['사용월', '호선명', '역ID', '지하철역', '유임승차', '유임하차', '무임승차', '무임하차']
    for i in range(4, 8):
        row[i] = int(row[i])
    total_count = row[4] + row[6]
    if (row[6] != 0) and (total_count>100000):
        rate = row[4] / total_count
        if rate > max_rate:
            max_rate = rate
            max_row = row
            max_total_num = total_count
            print(f"호선명: {max_row[1]}, 역이름:	{max_row[3]}, 전체 인원: {max_total_num:,}명," 
            f"유임승차인원:	{max_row[4]:,}명, 유임승차 비율: {round(max_rate * 100, 2):,}%")

f.close()