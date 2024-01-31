'''
내 생일의 기온 변화를 그래프로 그리기
05-08
'''
import csv
f = open("seoul_clean.csv")
data = csv.reader(f)
header = next(data)
for row in data:
    if "05-08" in row[0]:
        print(f"row[-1] {row[-1]}")

