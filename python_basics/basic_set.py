evens = {2, 4, 6, 8, 10}
odds = {1, 3, 5, 7, 9}
numbers = evens.union(odds) # union: 합집합
mthree = {3, 6, 9}

def define_set():
    """
    집합 정의
    """
    empty_set = set()  # 빈 집합: {}

    # 주의
    print(type(empty_set), type({}))  # 빈 중괄호를 선언하면 집합이 아닌 dict로 인식한다.

    print(numbers, "length:", len(numbers))
    print(2 in numbers, 2 in evens, 2 in odds, 2 in mthree)

    # 자료구조 변경
    # 순차자료형의 중복값을 제거할 때 유용하다.
    s = "Python Programming"
    s = set(s)   # 문자열을 집합으로 변환: set(문자열)
    print(s, "length:",len(s))

    lst = "Python Programming Java Programming HTML Programming".split()
    print(lst)
    print(list(set(lst)))


def set_methods():
    """
    set 메소드들
    """
    print("numbers: ", numbers, "length:", len(numbers))
    numbers.add(10)   # 집합에 새로운 원소 추가: add(원소)
    print("numbers: ", numbers, "length:", len(numbers))

    print("evens: ", evens, "length:", len(evens))
    evens.remove(4)
    # evens.remove(4)  # error
    evens.discard(4)


def set_oper():
    """
    set 집합 연산
    """
    # 합집합
    print(odds | evens)
    # 교집합
    print(odds & mthree)
    # 차집합
    print(odds - mthree)
    # 부분집합?
    print(odds <= mthree)
    print(odds.issubset(numbers))
    # 모집합?
    print(evens >= numbers)
    print(evens.issuperset(numbers))



if __name__ == "__main__":
    # define_set()
    # set_methods()
    set_oper()