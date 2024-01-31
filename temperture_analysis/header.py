import csv
f = open("seoul.csv")
data = csv.reader(f)
header = next(data)
print(header)
header = next(data)
print(header)

# next는 파일 포인터(한줄한줄)을 이동시켜 줌!!