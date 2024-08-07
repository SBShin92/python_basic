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
    print("\n".join(["{} * {} = {}".format(i, j, i*j) for i in range(2, 10) for j in range(1, 10)]))


# star 피라미드
def star_pyramid():
    for i in range(1, 6):
        print("*" * i)


# 연습문제: 구구단, 피라미드
def exercise01():
    googoodan()
    star_pyramid()


def list_comprehension():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    result = []
    for num in data:
        result.append(num*2)
    print(result)

    print([num * 2 for num in data])  # 위의 결과와 같다.
    print("===================")
    strings = ["a", "as", "bat", "car", "dove", "python"]
    result = [s.upper() for s in strings if len(s) >= 3]
    print(result)

    # 1 ~ 100 정수 중 3의 배수의 리스트
    result = [num for num in range(1, 101) if num % 3 == 0]
    print(result)


def set_comprehension():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = {num % 3 for num in data}
    print(result)


def dict_comprehension():
    strings = ["a", "as", "bat", "car", "dove", "python"]
    result = {s.upper() : len(s) for s in strings}
    print(result)



if __name__ == "__main__":
    # if_statement()
    # cond_expr()
    # for_ex()
    # exercise01()
    # list_comprehension()
    # set_comprehension()
    dict_comprehension()
