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

    # 특정 문자열로 시작하는 지 여부
    url = "http://www.python.org/"
    surl = "https://www.python.org/"
    ftp = "ftp://www.python.org/"

    print("=====================================")
    # 문자열이 특정 문자열로 시작하는지 여부를 반환
    print(url.startswith("http://"))  
    print(surl.startswith(("http://", "https://")))

    # 특정 문자열로 끝나는 지 여부
    print(url.endswith((".org", ".com")))

def modify_replace_methods():
    """
    문자열 수정, 치환 관련 메소드 연습
    """
    s = "           Alice and the Heart of the Coding World             "
    print("strip:[", s.strip(), "]", sep="")  # 문자열의 양쪽 공백을 제거
    print("lstrip:[", s.lstrip(), "]", sep="")  # 문자열의 왼쪽 공백을 제거
    print("rstrip:[", s.rstrip(), "]", sep="")  # 문자열의 오른쪽 공백을 제거

    s = "------Alice and the Heart of the Coding World------"
    print("strip:[", s.strip("-"), "]", sep="")  # 문자열의 양쪽에 있는 특정 문자를 제거

    s = "I Like Pythons. I Like Python Programming. I Like Python Games."
    print(s.replace("Pythons", "Python"))  # 문자열 내의 특정 문자열을 다른 문자열로 치환
    print(s.replace("Python", "Java", 2))  # 문자열 내의 특정 문자열을 다른 문자열로 치환 (치환할 개수를 지정 가능)
    print(s.replace("Python", "Java").replace("Java", "C++"))  # 문자열 내의 특정 문자열을 다른 문자열로 치환 (연속적으로 치환 가능)

def align_methods():
    """
    문자열 정렬 관련 메소드
    """
    s = "Alice and the Heart of the Coding World"
    print("CENTER: [", s.center(60), "]", sep="")  # 문자열을 가운데 정렬하고 나머지 공간을 공백으로 채움
    print("CENTER: [", s.center(60, "*"), "]", sep="")  # 문자열을 가운데 정렬하고 나머지 공간을 특정 문자로 채움
    print("LJUST: [", s.ljust(60, "*"), "]", sep="")  # 문자열을 왼쪽 정렬하고 나머지 공간을 특정 문자로 채움
    print("RJUST: [", s.rjust(60, "*"), "]", sep="")  # 문자열을 오른쪽 정렬하고 나머지 공간을 특정 문자로 채움
    print("ZFILL: [", "1234".zfill(10), "]", sep="")  # 문자열을 오른쪽 정렬하고 나머지 공간을 0으로 채움


import re


def spilt_join_methods():
    """
    문자열 분할과 합치기 관련 메소드
    """
    s = "Ham and Cheese and Breads and Ketchup"
    print(s.split())  # 문자열을 공백을 기준으로 분할

    ingr = re.split(r"\s*and\s*", s, 2)  # 문자열을 특정 문자열을 기준으로 분할
    print(ingr)

    lines = """\
    Java Programming
    Python Programming
    HTML Coding    
    """
    print(lines.split())  # 문자열을 공백을 기준으로 분할
    print(lines.splitlines(True))  # 문자열을 줄바꿈 문자를 기준으로 분할 (줄바꿈 문자를 포함)
    print(lines.splitlines(False))  # 문자열을 줄바꿈 문자를 기준으로 분할 (기본값, 줄바꿈 문자를 포함하지 않음)

def check_methods():
    """
    str 데이터의 형태 판별
    """
    print("1234".isdigit())  # 문자열이 숫자로만 이루어져 있는지 판별
    print("abcd".isalpha())  # 문자열이 알파벳으로만 이루어져 있는지 판별
    print("abcd1234".isalnum())  # 문자열이 알파벳과 숫자로만 이루어져 있는지 판별

    print("abcd efgh".islower())  # 문자열이 소문자로만 이루어져 있는지 판별
    print("ABCD EFGH".isupper())  # 문자열이 대문자로만 이루어져 있는지 판별
    print(" ".isspace())  # 문자열이 공백으로만 이루어져 있는지 판별

    print("Title Title!".istitle())  # 문자열이 타이틀 형식인지 판별
    print("Title Title!".isidentifier())  # 문자열이 식별자로 사용할 수 있는지 판별
    print("Title Title!".isprintable())  # 문자열이 출력 가능한지 판별
    print("Title Title!".isdecimal())  # 문자열이 10진수로 이루어져 있는지 판별
    print("Title Title!".isnumeric())  # 문자열이 숫자로 이루어져 있는지 판별
    print("Title Title!".isascii())  # 문자열이 ASCII 코드로만 이루어져 있는지 판별

def string_format():
    """
    문자열 포맷팅 연습
    """
    # c 스타일 문자열 포맷
    	# %s: 문자열, %d: 정수, %f: 실수, %c: 문자, %o: 8진수, %x: 16진수, %%: % 문자
    	# %[맞춤]s: 문자열 맞춤, %[맞춤]d: 정수 맞춤, %[맞춤]f: 실수 맞춤
        	# -: 왼쪽 정렬, +: 양수일 때 + 표시, 0: 빈 공간을 0으로 채움, 숫자: 빈 공간을 숫자만큼 공백으로 채움
    	# %.[자리수]f: 실수 자리수 지정
        	# .[자리수]f: 실수 자리수 지정, .[자리수]g: 실수 자리수 지정 (소수점 이하가 0이면 소수점 생략)
    	# %[전체자리수].[소수점이하자리수]f: 실수 전체 자리수와 소수점 이하 자리수 지정
    fmt = "%d개의 %s 중에서 %d개를 먹었다."
    print(fmt % (3, "사과", 2))

    # named formatting
    fmt = "%(number)d개의 %(fruit)s 중에서 %(eat)d개를 먹었다."
    print(fmt % {'number': 3, 'fruit':'사과', 'eat':2})

    # format method
    fmt = "{}개의 {} 중에서 {}개를 먹었다."
    print(fmt.format(3, "사과", 2))

    # format method with name parameter
    fmt  = "{number}개의 {fruit} 중에서 {eat}개를 먹었다."
    print(fmt.format(number=3, fruit="사과", eat=2))

    # format_map method
    fmt  = "{number}개의 {fruit} 중에서 {eat}개를 먹었다."
    print(fmt.format_map({'number':3, 'fruit':'사과', 'eat':2}))

    # f-string
    total, fruit, eat = 10, "apple", 3
    print(f"{total}개의 {fruit} 중에서 {eat}개를 먹었다.")
    # 연산
    print(f"{total}개의 {fruit.upper()} 중에서 {eat}개를 먹어서, {total - eat}개가 남았다..")





if __name__ == '__main__':
    # define_str()
    # string_oper()
    # transform_methods()
    # search_methods()
    # modify_replace_methods()
    # align_methods()
    # spilt_join_methods()
    # check_methods()
    string_format()
