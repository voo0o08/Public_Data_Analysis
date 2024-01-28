import csv

def get_minmax_temp(data):
    '''
    최고 기온 및 최고 기온의 날짜 구하기
    '''
    header = next(data)

    min_temp = 100 # 최저 기온 값은 ㅈㄴ 크게 설정해야 비교 연산이 가능
    min_date = ""

    max_temp = -999
    max_date = ""

    for row in data:
        if row[3] == '':
            row[3] = 100
        row[3] = float(row[3])

        if row[4] == '':
            row[4] = -999
        row[4] = float(row[4])

        # 최저 기온 계산
        if row[3] < min_temp:
            min_temp = row[3]
            min_date = row[0]

        # 최고 기온 계산
        if row[4] > max_temp:
            max_temp = row[4]
            max_date = row[0]

    print('-' * 50)
    print(f'대구 최저 기온 날짜:	{min_date},	온도:	{min_temp}')
    print(f'대구 최고 기온 날짜:	{max_date},	온도:	{max_temp}')

def main():
    f = open('daegu-utf8.csv', encoding='utf-8-sig')
    data = csv.reader(f)
    get_minmax_temp(data)
    f.close()

main()