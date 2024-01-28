import csv
fin = open("daegu.csv", "r", encoding="utf-8-sig")
data = csv.reader(fin, delimiter=",")

# newline="" : 한 라인씩 건너 뛰며 저장되는 현상 없앰
fout = open("daegu-utf8.csv", "w", newline="", encoding="utf-8-sig")
wr = csv.writer(fout)

for row in data:
    for i in range(len(row)):
        row[i] = row[i].replace("\t", "")
        if row[0] == "1959-08-15":
            print("dddddddddddddd")
    print(row)
    wr.writerow(row)

fin.close()
fout.close()
print("파일 저장 환료")