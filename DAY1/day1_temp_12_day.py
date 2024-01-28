# 매년 특정 날짜의 최고 기온 찾기
import	csv
import	matplotlib.pyplot as plt
import	koreanize_matplotlib

def draw_graph(m, d):
    f = open("daegu-utf8.csv", encoding="utf-8")
    data = csv.reader(f)
    next(data)
    result = []

    for row in data:
        if row[-1] != "":
            data_string = row[0].split("-") # 년-월-일을 -기준으로 쪼갬
            if data_string[1] == m and data_string[2] == d:
                result.append(float(row[-1]))

    f.close()
    plt.figure(figsize=(15, 3))
    plt.plot(result, "royalblue")
    plt.rc("axes", unicode_minus=False)
    plt.rc('font', family='Malgun Gothic')
    plt.title(f'매년 {m}월 {d}일 최고 기온 변화')
    plt.show()

month, date = input('날짜(월 일)를 입력하세요:	').split()
draw_graph(month, date)