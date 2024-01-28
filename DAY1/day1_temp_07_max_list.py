# 데이터를 리스트에 저장하기

import csv
import matplotlib.pyplot as plt

f = open("daegu-utf8.csv", encoding="utf-8-sig")
data = csv.reader(f)

header = next(data)
result = []

for row in data:
    if row[4] != "":
        result.append(float(row[4]))

print(len(result))
f.close()
plt.figure(figsize=(10, 2))
plt.plot(result, "r")
plt.show()