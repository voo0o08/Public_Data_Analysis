'''
['\t1907-10-01', '108', '13.5', '7.9', '20.7']
날짜 앞 tab키를 제거하고 새로 저장해보자
'''
import csv
f = open("seoul.csv")
data = csv.reader(f)
# header = next(data)

fout = open("seoul_clean.csv", "w", newline="",encoding="cp949")
wr = csv.writer(fout)
for row in data:
    print(row)
    row[0] = row[0].replace("\t", "")
    print(row)
    wr.writerow(row)
# 맨 밑에 공백 뜨길래 파일 자체에서 제거 해줌
f.close()
fout.close()