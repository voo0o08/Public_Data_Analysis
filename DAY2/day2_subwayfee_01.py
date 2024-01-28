import csv

f = open("subwayfee.csv", encoding="utf-8-sig")
data = csv.reader(f)
header = next(data)
print(header)
i = 1
for row in data:
    print(row) # 숫자도 문자열로 들어와 있음을 주목
    if i>5:
        break
    i+=1 # 5줄만 일단 보자
f.close()

# ['사용월', '호선명', '역ID', '지하철역', '유임승차', '유임하차', '무임승차', '무임하차']