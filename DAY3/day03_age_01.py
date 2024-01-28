# 주의 : 같은 이름의 동이 여러번 나올 수 있다는 것을 유의할 것
import	csv
f	=	open('age.csv',	encoding='utf-8-sig')
data	=	csv.reader(f)
header	=	next(data)
print(header)
#	row[0]:	행정기관
for	row	in	data:
	if	'산격3동' in	row[0]:	#산격3동'이 포함된 자료만 출력
		print(row)
f.close()