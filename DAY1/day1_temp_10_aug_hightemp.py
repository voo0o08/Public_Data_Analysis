# 8월의 최고 기온 히스토그램
# row = > '날짜', '지점', '평균기온(℃)', '최저기온(℃)', '최고기온(℃)’
import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

f = open("daegu-utf8.csv", encoding="utf-8-sig")
data = csv.reader(f)
next(data)
aug = []

for row in data:
    month = row[0].split("-")[1]
    if row[-1] != "": # 최고 기온이 공백이 아니면서
        if month == "08": # 8월일 것
            aug.append(float(row[-1])) # 적합하다면 추가

f.close()
plt.hist(aug, bins=100, color="tomato")
plt.title("대구 8월의 최고 기온 히스토그램")
plt.show()
