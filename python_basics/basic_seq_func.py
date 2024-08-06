def using_range():
    """
    range의 경우, 범위 정보만 가지고 있다가 요청할 때 조건을 계산한 후 결과를 반환한다.
    때문에 커다란  range를 생성해도 메모리가 증가하지 않는다: Generator
    """
    print(range(10))
    print(list(range(1, 10, 2)))
    
    seq2 = range(2, 10, 3)

    
def using_enumerate():
    """
    enumerate() 함수는 반복 가능한(iterable) 객체에 카운터를 추가하고 enumerate 객체로 반환합니다.
    이 enumerate 객체는 바로 for 루프에서 사용할 수 있거나 list() 함수를 사용하여 튜플의 리스트로 변환할 수 있습니다.
    """
    en = enumerate("Python")
    print(list(enumerate('abc')))
    print(list(enumerate([1,2])))
    print(list(enumerate(("Python", 3))))
    for i, v in en:
        print(f"{i} : {v}")


def using_zip():
    eng = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    kor = ["일요일", "월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
    
    engkor = zip(eng, kor)
    print(engkor, type(engkor))

    for e, k in engkor:
        print(f"{e} : {k}")


if __name__ == '__main__':
    # using_range()
    # using_enumerate()
    using_zip()