# 나누기를 0으로 하면 안됨 -> 무임승차 인원이 0명인 역이 존재하는지 확인 가능
# 즉, 에러가 나면 무임승차가 0인 역이 있다는 뜻!!
import csv

f=open("subwayfee.csv", encoding="utf-8-sig")
data = csv.reader(f)
header = next(data)
max_rate = 0
rate = 0

for row in data:
    for i in range(4, 8):
        row[i] = int(row[i])
    rate = row[4] / row[6]
    if rate > max_rate:
        max_rate = rate
print(max_rate)
f.close()