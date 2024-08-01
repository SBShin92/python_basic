import keyword


def arith_oper():
    print("==== 산술 연산")
    print(7 / 3)
    print(7 // 3)
    print(7 % 3)
    print(divmod(7, 3))


def dummy():
    pass  # 함수 구현부 없이 선언만 해두고 싶을 때 사용


def rel_oper():
    print("==== 비교 연산")
    # 복합 관계식
    a = 5
    if 1 < a < 10:
        print("1 < a < 10 ?", 1 < a < 10)  # True
    # 문자열 대소 비교
    print("abcd > dcba ?", "abcd" > "dcba")
    # 튜플 대소 비교
    print("(1, 4, 3) > (1, 3, 9) ?", (1, 4, 3) > (1, 3, 9))
    # 동질성의 비교: ==, 동일성의 비교: is
    a, b = 10, 10
    print("a == b ?", a == b)
    print("a is b ?", a is b)


def var_ex():
    print("==== 변수")
    print("예약어 목록: ", keyword.kwlist)
    print("예약어 갯수: ", len(keyword.kwlist))


def assignment_ex():
    print("==== 치환문")
    print("namespace:  ", dir())
    a = 2024
    b = a + 1
    print(a, b)
    print("namespace: ", dir())

    # 치환
    c, d = 3.5, 5.3
    c, d = d, c
    print(c, d)

    # 한번에 할당
    x = y = z = 10
    print(x, y, z)

    # 동적 타입
    a = 2024
    print(a, "is", type(a))
    a = "Hello PYTHON!!"
    print(a, "is", type(a))

    # 특정 객체인지 여부를 판단하는 함수: isinstance
    print(isinstance(a, str))

    st = "abcdef"
    print(st[-4:])


def bool_ex():
    print("==== bool 연습")
    print(bool(0), bool(2024), bool(3.14))
    print(bool("Python"), bool(""))
    a = 2024
    print(a > 0)
    print(type(a > 0))
    print(isinstance(True, bool))
    print(isinstance(True, int))
    print (True + True)
    print(bool(None))

    # Circuit Break
    print("CB 1:", [] or "logical")
    print("CB 2:", "logical" or "operator")
    print("CB 3:", "logical" and "operator")
    print("CB 4:", "" or "operator")
    print("CB 5:", "" and "operator")
    print("CB 6:", None and 1)
    print("CB 7:", None or "operator")


def type_hint():
    def add(a: int, b: int) -> int:
        return a + b
    print(add(2, 3))
    # print(add(2, "a"))  # TypeError
    print(add("py", "a"))  # ????

    def greet(name: str) -> str:
        return "Hello, " + name
    print(greet("sashin"))

if __name__ == "__main__":
    # arith_oper()
    # dummy()
    # rel_oper()
    # var_ex()
    # assignment_ex()
    # bool_ex()
    type_hint()