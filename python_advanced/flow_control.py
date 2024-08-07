def if_statement():
    try:
        cost = int(input("얼마 있으세요?: "))
        if cost >= 10000 :
            print("택시 타입니다.")
        elif cost >= 2000 :
            print("버스 타입니다.")
        else :
            print("걸어 가라.")
    except:
        print("숫자를 입력해주세요.")


def cond_expr():
    try:
        cost = int(input("얼마 있으세요?: "))
        print("택시 타입니다." if cost >= 10000 else "버스 타입시다." if cost >= 2000 else "걸어 가라.")
    except:
        print("숫자를 입력해주세요.")



def for_ex():
    for i in range(3):
        print(i)
    
    for animal in ["dog", "cat", "pig"]:
        print(animal, end = " ")
    else:
        print()

    r1 = [1, 3, 5, 7, 9, 11]
    r2 = r1 + [12, 13, 15]
    for i in r1:
        if i % 2 == 0 :
            print("짝수를 찾았습니다.", i)
            break
    else:
        print("짝수를 못찾았습니다.")


# 구구단
def googoodan():
    for i in range(2, 10):
        for j in range(1, 10):
            print("{} * {} = {}".format(i, j, i*j))


# star 피라미드
def star_pyramid():
    for i in range(1, 6):
        print("*" * i)



if __name__ == "__main__":
    # if_statement()
    # cond_expr()
    # for_ex()
    googoodan()
    star_pyramid()
