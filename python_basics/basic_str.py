def define_str():
    # 문자열의 정의
    # 한 줄 문자열: 큰 따옴표(")나 작은 따옴표(')를 사용
    str1 = "Hello, World!"
    str2 = 'Python is fun!'
    str3 = str(1234567890)  # 숫자를 문자열로 변환
    print(str1, type(str1))
    print(str2, type(str2))
    print(str3, type(str3))

    print("str1은 str?", isinstance(str1, str))

    # 여러 줄 문자열: 큰 따옴표 3개(""")나 작은 따옴표 3개(''')를 사용 
    str4 = """Life is too short,
    You need python."""
    str5 = '''파이썬은 데이터 처리가 가능한 시대에서
    가장 널리 사용되는 언어입니다.'''
    print(str4, type(str4))
    print(str5, type(str5))

def string_oper():
    """
    문자열 연산
    """
    str1 = "First String"
    str2 = "Second String"
    print(len(str1), len(str2)) 

    # 인덱싱
    print(str1[0], str1[1], str1[2], "...", str1[10], str1[11])
    # 역방향 인덱싱
    print(str1[-1], str1[-2], str1[-3], "...", str1[-11], str1[-12])

    # 문자열른 immutable하기 때문에 치환이 불가능하다.
    # str1[0] = 'f'  # TypeError: 'str' object does not support item assignment

    # 슬라이싱
    # [시작경계:끝경계:스텝] 시작경계는 포함, 끝경계는 미포함, 스텝은 생략가능(기본값 1)
    print(str1[0:5], str1[5:12], str1[0:12:2])  # 0~4, 5~11, 0~11 짝수번째
    print(str1[:5], str1[5:], str1[::2])  # 시작경계 생략, 끝경계 생략, 스텝 2
    print(str1[5:0:-1], str1[::-1])  # 음수 스텝


def transform_methods():
    """
    대소문자 변환 관련 연습
    """
    str1 = "Hello, World!"
    print(str1.upper())  # 모두 대문자로 변환
    print(str1.lower())  # 모두 소문자로 변환
    print(str1.swapcase())  # 대문자는 소문자로, 소문자는 대문자로 변환
    print(str1.capitalize())  # 문자열의 첫 글자를 대문자로 변환
    print(str1.title())  # 문자열의 각 단어의 첫 글자를 대문자로 변환
    print(str1.replace("World", "Python"))  # 문자열 내의 특정 문자열을 다른 문자열로 변환
    print(str1.count("l"))  # 문자열 내의 특정 문자열의 개수를 반환
    print(str1.find("World"))  # 문자열 내의 특정 문자열의 시작 인덱스를 반환
    

def search_methods():
    """
    문자열 검색 관련 예제
    """
    s = "Python is powerful. Python is easy to learn."
    print(s.startswith("Python"))  # 문자열이 특정 문자열로 시작하는지 여부를 반환
    print(s.endswith("learn."))  # 문자열이 특정 문자열로 끝나는지 여부를 반환
    print(s.count("Python"))  # 문자열 내의 특정 문자열의 개수를 반환
    idx = s.capitalize().find("Python")  # 문자열 내의 특정 문자열의 시작 인덱스를 반환
    print(idx, s[idx:idx + len("Python")])  # 문자열 내의 특정 문자열의 시작 인덱스를 이용하여 해당 문자열을 추출
    idx = idx + len("Python") + 1  # 다음 문자열의 시작 인덱스를 계산
    s.find("Python", idx)  # 문자열 내의 특정 문자열의 시작 인덱스를 반환 (시작 인덱스를 지정하여 검색 가능)

    # index로 찾기
    print(s.index("Python"))  # 문자열 내의 특정 문자열의 시작 인덱스를 반환
    # print(s.index("Java"))  # 문자열 내에 특정 문자열이 없으면 ValueError 발생
    # 예외 처리 방법?
    # 1. try-except 구문 사용
    try:
        print(s.index("Java"))
    except ValueError as e:
        print(e)
    # 2. if 구문 사용
    if "Java" in s:
        print(s.index("Java"))
    # 3. find 메서드 사용 (find 메서드는 문자열이 없으면 -1을 반환)
    if s.find("Java") != -1:
        print(s.index("Java"))
    print("=====================================")
    # 역방향 검색
    print(s.rfind("Python"))  # 문자열 내의 특정 문자열의 시작 인덱스를 반환 (오른쪽에서 왼쪽으로 검색)
    print(s.rfind("Python", 0, 20))  # 문자열 내의 특정 문자열의 시작 인덱스를 반환 (오른쪽에서 왼쪽으로 검색, 시작 인덱스와 끝 인덱스를 지정하여 검색 가능)



if __name__ == '__main__':
    # define_str()
    # string_oper()
    # transform_methods()
    search_methods()