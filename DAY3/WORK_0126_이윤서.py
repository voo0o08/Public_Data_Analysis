import platform
import	csv
import	matplotlib.pyplot as plt
import koreanize_matplotlib
import math

def draw_pie_chart(gender_dict):
    '''
    gender_dict.key = 대구광역시 중구, 동구, ...
    gender_dict.val = [남성, 여성]
    '''
    keys = list(gender_dict.keys())
    idx = 0
    for i in range(9):
        plt.rc("font", size=7)
        plt.subplot(3, 3, idx+1)
        #plt.pie(pop_list, labels=label_list, autopct="%.1f%%", startangle=90)
        plt.pie(gender_dict[keys[idx]], labels=["남성", "여성"], autopct="%.1f%%", startangle=90)
        plt.title(keys[idx])
        idx += 1
    plt.suptitle("대구광역시 구별 남녀 인구 비율", fontsize = 15)
    plt.tight_layout()
    plt.show()

def del_comma(str_num):
    str_num = str_num.replace(",", "")
    return str_num

def gender_ratio():
    # 남자는 3~
    # 여자는 남자+103
    # ['행정기관', '총 인구수', '연령구간인구수 ...]
    f = open('gender.csv', encoding='utf-8-sig')
    data = csv.reader(f)
    # next(data)  # header pass

    gender_dict = {}
    # 군위는 빼기
    for row in data:
        if "대구광역시" in row[0]:
            # print(row[0])
            # print(del_comma(row[104])) # 남자
            # print(row[207]) # 여자

            male_num = del_comma(row[104])
            female_num = del_comma(row[207])

            gender_dict[row[0]] = [male_num, female_num]
    f.close()
    draw_pie_chart(gender_dict)





gender_ratio()