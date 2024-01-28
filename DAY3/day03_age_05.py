# 투표 가능 인구수 분석
import	csv
import	matplotlib.pyplot as plt
import koreanize_matplotlib

def draw_piechart(city_name, city_pop, voting_pop):
    '''
    전체 인구수 대비 투표 가능 인구의 파이차트 작성

    :param city_name:
    :param city_pop:
    :param voting_pop:
    :return:
    '''

    non_voting_pop = city_pop - voting_pop
    pop = [non_voting_pop, voting_pop] # pie chart 전달용

    color = ["tomato", "blue"]
    plt.pie(pop, labels=["18세 미만", "투표가능인구"], autopct="%.1f%%", colors=color, startangle=90)
    plt.legend(loc=1)
    plt.title(city_name+"투표 가능 인구 비율")
    plt.show()

def	get_voting_pop(city):
    '''
    투표 가능 인구수 분석 row[21:]
    전체 인구수 : row[1]
    :param city:
    :return:
    '''
    f = open('age.csv', encoding='utf-8-sig')
    data = csv.reader(f)
    next(data)  # header pass

    voting_num_list = []
    city_name = ""
    city_pop = 0
    voting_pop = 0
    for row in data:
        if city in row[0]:
            city_pop = row[1]
            if "," in city_pop:
                city_pop = city_pop.replace(",", "")
            city_pop = int(city_pop)

            city_name = row[0]
            for data in row[21:]:
                if "," in data:
                    data = data.replace(",","")
                voting_num = int(data)

                voting_num_list.append(voting_num)

                voting_pop += voting_num
            break
    f.close()
    print(f'{city_name}전체 인구수:{city_pop:,}명,투표 가능 인구수: {voting_pop:,}명')
    draw_piechart(city_name, city_pop, voting_pop)


city = input('투표 가능 인구수를 확인할 도시이름을 입력하시오: ')
get_voting_pop(city)