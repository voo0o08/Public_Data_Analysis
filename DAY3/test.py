import csv
f = open("age.csv", encoding="utf-8")
data = csv.reader(f, delimiter=",")
for row in data:
    print(data)
f.close()