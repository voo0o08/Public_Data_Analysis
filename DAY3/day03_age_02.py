import	csv

f	=	open('age.csv',	encoding='utf-8-sig')
data	=	csv.reader(f)
header	=	next(data)

# row = 행정기관 / 총 인구수 / 연령 구간 인구수 / 0 ... 100
#         0         1             2            3:
result = []
for	row	in	data:
    if "산격3동" in row[0]: # 산격3동이 포함된 자료만 출력 row[0]=행정기관
        for data in row[3:]: # 0~100세 이상까지 자료를 리스트에 추가
            result.append(data)
print(result)
f.close()