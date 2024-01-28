# 최고 기온 데이터를 히스토그램으로 표현
import	csv
import	matplotlib.pyplot as plt
import koreanize_matplotlib

f	=	open('daegu-utf8.csv',	encoding='utf-8-sig')
data = csv.reader(f)
next(data)
result = []

# '날짜', '지점', '평균기온(℃)', '최저기온(℃)', '최고기온(℃)’
# -> 최고 기온 index = -1
for row in data:
    if row[-1] != "":
        result.append(float(row[-1]))
f.close()

plt.figure(figsize=(10, 2))
plt.hist(result, bins=500, color="b")
plt.rc('font',	family='Malgun Gothic')

plt.rcParams["axes.unicode_minus"] = False
plt.title("1907년 부터 2023년까지 대구 기온 히스토그램")
plt.show()