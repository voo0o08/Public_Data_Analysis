import	csv
import	matplotlib.pyplot as plt
import	platform
import	koreanize_matplotlib

def draw_lowhigh_graph(start_y, m, d):
    f = open("daegu-utf8.csv", encoding="utf8")
    data = csv.reader(f)
    next(data)
    high_List = []
    low_List = []
    year_List = []

    for row in data:
        if row[-1] != "":
            date_string = row[0].split("-")
            if int(date_string[0]) >= start_y:
                if int(date_string[1]) == m and int(date_string[2]) == d:
                    high_List.append(float(row[-1]))
                    low_List.append(float(row[-2]))
                    year_List.append(date_string[0])

    f.close()

    plt.figure(figsize=(20, 4))
    plt.plot(year_List, high_List, 'hotpink', marker='o', label='최고기온')  # 최고 기온 그래프


    plt.plot(year_List, low_List, 'royalblue', marker='s', label='최저기온')  # 최저 기온 그래프
    if platform.system() == 'Windows':
        plt.rc('font', family='Malgun Gothic', size=8)  # 간단히 맑은 고딕으로 설정
    else:
        plt.rc('font', family='AppleGothic', size=8)  # 한글 폰트 사용 For	Mac	OS
    plt.rcParams['axes.unicode_minus'] = False  # 음수(-)가 깨지는 것 방지
    plt.title(f"{start_y}년 이후 {m}월 {d}일의 온도 변화 그래프", size=16)
    plt.legend(loc=2)
    plt.xlabel('year')
    plt.ylabel('temperature')
    plt.show()
draw_lowhigh_graph(2000, 12, 24)