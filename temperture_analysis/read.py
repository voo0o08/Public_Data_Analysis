import csv
f = open("seoul.csv", encoding="cp949")
data = csv.reader(f, delimiter=",")
for row in data:
    print(data)
f.close()

import	csv

