# 연령별 성별 데이터 시각화
import platform
import	csv
import	matplotlib.pyplot as plt
import koreanize_matplotlib

def print_pop(pop):
    '''
    특정 지역의 인구 현황으 화면에 출력
    :param pop:
    :return:
    '''
    for i in range(len(pop)):
        print(f"{i:3d}세: {pop[i]:4d}명", end=" ")
        if (i+1)%10 == 0:
            print()
    print()

def draw_gender_pop(title, male_list, female_list):

    if platform.system() == "Windows":
        plt.rc("font", family = "Malgun Gothic")
    else:
        plt.rc("font", family = "Malgun Gothic")
    # barh(y축 범위, data)
    plt.barh(range(len(male_list)), male_list, label="남성")
    plt.barh(range(len(female_list)), female_list, label="여성")
    plt.rcParams["axes.unicode_minus"] = False
    plt.title(title+"성별 인구 비율")
    plt.legend()
    plt.show()

def cal_pop():
    f = open('gender.csv', encoding='utf-8-sig')
    data = csv.reader(f)
    male_num_list = []
    female_num_list = []

    district = input("시군구를 입력하세요: ")
    for row in data:
        if district in row[0]:
            for male in row[106:207]:
                if "," in male:
                    male = male.replace(",", "")
                male_num_list.append(-int(male))
            for female in row[209:310]:
                if "," in female:
                    female = female.replace(",", "")
                female_num_list.append(int(female))
            break
    f.close()

    print(f'남성 총 인구수:{sum(male_num_list):,}	')
    print_pop(male_num_list)
    print('-------------------------------')
    print(f'여성 총 인구수:{sum(female_num_list):,}	')
    print_pop(female_num_list)
    draw_gender_pop(district, male_num_list, female_num_list)

cal_pop()