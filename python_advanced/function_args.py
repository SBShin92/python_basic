def sum_val(a, b):
    return a + b


def incr(a, step = 1):
    return a + step


print(sum_val(20, 3))
print(incr(5))
print(incr(step = 4, a = 8))


# 가변인자
def get_total(*args):
    sum = 0
    for x in args:
        sum += x
    return sum
print(get_total(1, 3, 5, 7, 9))



# 딕셔너리 인자
def f(a, b, *args, **kwd):
    print(a, b)
    print(args)
    print(kwd)

f(10, 20, 30, 40, depth = 10, dimension = 3)


# 함수 객체 인자
def clean_strings(strings, *funcs):  # 함수 목록을 가변 파라미터로 받아보자
    results = []
    for string in strings:
        for func in funcs:
            string = func(string)
        results.append(string)
    return results
    
states = ['Alabama', ' Georgia', 'Georgia ', 'georgia', 'FlOrIda', 'south carolina', 'West virginia']
states = clean_strings(states, str.strip, str.title)
print(states)