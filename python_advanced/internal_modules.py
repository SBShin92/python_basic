import sys


def sys_module():
    print(sys.argv)
    args = sys.argv[1:]
    print(args)

    print("Platform:", sys.platform)
    print("Version:", sys.version)

    # 파이썬 모듈 검색? sys.path
    print(sys.path)
    # 찾는 모듈이 sys.path에 없을 때?
    # sys.path.append('C:\\Users\\user\\Desktop')


def regexp_ex():
    import re

    emaillist = re.findall(r'\w+@\w+\.\w+', 'aopaoi0987@naver.com')
    print(emaillist)

    phonelist = re.findall(r'\d{3}-\d{4}-\d{4}', '010-9876-5432')
    print(phonelist)


# TODO: 난수 고정 해제해야!
def random_ex():
    import random

    random.seed(42)  # 난수 고정

    print(random.random())
    print(random.randint(1, 6))
    print(random.randrange(101))
    print(random.randrange(1, 101, 3))

    seqvar = ["짬뽕", "짜장면", "짬짜면", "마라탕"]
    print("seqvar:", seqvar)
    random.shuffle(seqvar) # shuffle은 리스트 자체를 바꾸는 것이므로 return 값이 없다.
    print("shuffle:", seqvar)
    print(random.choice(seqvar))
    
    for i in range(5):
        print(random.sample(range(1, 101), 10))



if __name__ == '__main__':
    # sys_module()
    # regexp_ex()
    random_ex()