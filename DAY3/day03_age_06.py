# 투표 가능 인구수 분석
import	csv
import	matplotlib.pyplot as plt
import koreanize_matplotlib

def draw_pie_chart(city, pop_list, label_list):
    '''
    pop_list = [120339, 63568, 64874, 90608, 2035571] -> 알아서 비율 쳐주는
    label_list = ['초등학생', '중학생', '고등학생', '대학생', '비학령인구']
    '''
    # print(pop_list)
    # print(label_list)
    plt.pie(pop_list, labels=label_list, autopct="%.1f%%", startangle=90)
    plt.legend(loc=1)
    plt.title(city + "학령 인구 비율")
    plt.show()

def	get_pop(row, start, end): # 초 중 고 대 => 4번 호출 됨
    '''

    '''

    pop = 0
    for num in row[start:end+1]:
        if "," in num:
            num = num.replace(",", "")
        num = int(num)
        pop += num
    return pop

def school_age_pop(city):
    city_pop = 0
    non_school_pop = 0
    school_age_pop = 0

    label_list = ['초등학생', '중학생', '고등학생', '대학생', '비학령인구']
    pop_list = []

    f = open('age.csv', encoding='utf-8-sig')
    data = csv.reader(f)
    next(data)  # header pass

    for row in data:
        if city in row[0]:
            city_pop = row[1]
            if "," in city_pop:
                city_pop = city_pop.replace(",", "")
            city_pop = int(city_pop)

            # 각 구간별 인구 계산
            elementary_pop = get_pop(row, 9, 14)
            pop_list.append(elementary_pop)

            middle_pop = get_pop(row, 15, 17)
            pop_list.append(middle_pop)

            high_pop = get_pop(row, 18, 20)
            pop_list.append(high_pop)

            university_pop = get_pop(row, 21, 24)
            pop_list.append(university_pop)

            school_age_pop = (elementary_pop + middle_pop + high_pop + university_pop)

            non_school_pop = city_pop - school_age_pop
            pop_list.append(non_school_pop)
            break
    f.close()
    print(f'전체 인구수:{city_pop:,}명, 학령인구 비율: {round((school_age_pop*100)/city_pop,1)}%')
    draw_pie_chart(city, pop_list, label_list)


city = input('학령인구를 분석할 도시 이름 : ')
school_age_pop(city)