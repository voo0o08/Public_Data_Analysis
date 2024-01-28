def user_input():
    while True:
        size = int(input("홀수차 배열의 크기를 입력하세요: "))
        if size%2 == 0:
            print("짝수를 입력하였습니다. 다시 입력하세요.")
            continue
        else:
            return size

def print_square(size, square):
    print(f"Magic Square ({size}x{size})")
    for row in square:
        for val in row:
            print(val, end=" ")
        print()

# main
size = user_input()
square = [[0 for i in range(size)]for j in range(size)]
# print(square)
num = 1
row = 0
col = size//2

while True:
    # 칸을 넣을 숫자가 다 찼으면 끝
    if num == size*size+1:
        print_square(size, square)
        break

    if square[row][col] != 0:
        row += 1
        square[row][col] = num
        num += 1
        row -= 1
        col += 1
    if square[row][col] == 0:
        square[row][col] = num
        print_square(size, square)
        num += 1
        row -= 1
        col += 1
    # 이미 숫자가 있는 경우 아래로 이동

    if row<0:
        row = size-1
    elif row>size-1:
        row = 0

    if col<0:
        col = size-1
    elif col>size-1:
        col = 0




