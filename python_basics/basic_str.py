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



if __name__ == '__main__':
    # define_str()
    string_oper()