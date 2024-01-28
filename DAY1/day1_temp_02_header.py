import csv
f = open("daegu.csv", "r", encoding="utf-8")
data = csv.reader(f)
count=0
for row in data: # 1줄 씩 읽어옴 / data는 객체 
    if count > 5:
        break
    else:
        print(row)
    count += 1

f.close()