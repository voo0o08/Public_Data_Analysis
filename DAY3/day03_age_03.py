import csv
import matplotlib.pyplot as plt
import platform
import koreanize_matplotlib

f = open("age.csv", encoding="utf-8-sig")
data = csv.reader(f)
result = [] # 연령별 인구 수
city = ""

for row in data:
    if "산격3" in row[0]:
        city = row[0]
        for data in row[3:]:
            if "," in data:
                data = data.replace(",", "")
            result.append(int(data))

f.close()
print(result)

plt.title(f"{city} 인구현황")
plt.xlabel("나이")
plt.ylabel("인구수")
plt.plot(result)
plt.show()