import sys
import copy


# 글로벌 변수 선언
global_a = 1
global_b = "Global"

# 사용자 정의 함수
def myfunc():
    local_a = 2
    local_b = "Local"
    print(locals())  # 로컬 심볼 테이블 확인


# 사용자 정의 클래스
class MyClass:
    x = 10
    y = 20


def symbol_table():
    print(globals(), type(globals()))

    print("global_a:", globals().get("global_a"))
    print("global_b:", globals().get("global_b"))

    myfunc()

    myfunc.dynamic = "Dynamic"
    print(myfunc.__dict__)

    # 인스턴스 객체
    o = MyClass()
    o.dynamic = "Dynamic"
    print(o.__dict__)


def ref_count():
    x = object()
    print(x, type(x))

    print(sys.getrefcount(x), "번 참조")
    y = x
    print(sys.getrefcount(x), "번 참조")
    del y
    print(sys.getrefcount(x), "번 참조")


def object_id():
    i1 = 10
    i2 = int(10)
    print(hex(id(i1)), hex(id(i2)))   # immutable

    s1 = "Hello"
    s2 = str("Hello")
    print(hex(id(s1)), hex(id(s2)))   # immutable

    lst1 = [1, 2, 3]
    lst2 = list([1, 2, 3])
    print(hex(id(lst1)), hex(id(lst2)))   # mutable

    # == : 동등성의 비교, is : 동일성의 비교
    print(i1 == i2, i1 is i2)
    print(s1 == s2, s1 is s2)
    print(lst1 == lst2, lst1 is lst2)

    # 아래 두 연산은 같다.
    print(id(lst1) == id(lst2), lst1 is lst2)


def object_copy():
    # 참조 복제
    a = [1, 2, 3]
    b = a
    print(b, "a is b?", a is b)
    a[0] = 4
    print(b)

    # immutable 자료형은 깊은 복사를 해도 같은 값을 참조한다.
    c = 1
    d = copy.deepcopy(c)
    print(c is d)  # True!

    # 얕은 복사
    c = a[:]  # copy.copy와 같다.
    print(a, "a is c?", a is c)
    a[1] = 5
    x = [a, b, c]
    y = copy.copy(x)
    print(y)
    a[1] = 100
    print(y)  # 얕게 복사되어 있는 것을 볼 수 있다.

    # 깊은 복사
    y = copy.deepcopy(x)
    print(y)
    a[1] = 314748
    print(y)



if __name__ == "__main__":
    # symbol_table()
    # ref_count()
    # object_id()
    object_copy()