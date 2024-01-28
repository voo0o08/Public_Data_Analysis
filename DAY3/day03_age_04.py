import	csv
import	matplotlib.pyplot as plt
import	platform
import	matplotlib.font_manager as fm
import koreanize_matplotlib

def print_population(population):
    '''
    특정 지역의 인구 현황을 화면에 출력함
    '''
    for i in range(len(population)):
        print(f"{i:3d}세: {population[i]:6d}명", end=" ")
        if (i+1)%10==0:
            print()

def draw_population(district_name, population_list):
    '''
    특정 지역에 대한 인구 분포를 그래프로 나타냄(plot)
    :param district_name: 지역 이름
    :param population_list: 0~100세 이상까지 인구수 리스트
    :return:
    '''

    # 그래프 출력
    plt.style.use("ggplot")
    plt.title("{}인구 현황".format(district_name))
    plt.xlabel("나이")
    plt.ylabel("인구수")

    plt.bar(range(101), population_list)
    plt.xticks(range(0, 101, 10))

    plt.plot(population_list)

def get_population(city):
    f = open('age.csv', encoding='utf-8-sig')
    data = csv.reader(f)
    next(data) # header pass

    pop_list = []
    district_name = ""
    for row in data:
        district_name = row[0]
        for data in row[3:]:
            if "," in data:
                data = data.replace(",", "") # 숫자에 콤마제거
            pop_list.append(int(data))
        break

    f.close()
    print_population(pop_list)
    draw_population(district_name, pop_list)

# main
city = input("지역 입력")
get_population(city)
plt.show()