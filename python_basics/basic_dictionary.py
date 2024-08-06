def define_dectionary():
    """
    dictionary 정의
    """
    dct = dict()
    print(dct, type(dct))
    dct = {}
    print(dct, type(dct))

    dct = dict(one='1', two='2', three=3)
    print(dct)

    key = 'one', 'two', 'three'
    value = '1', '2', 3
    dct = dict(zip(key,value))
    print(dct)

def dictionary_oper():
    """
    dictionary 연산
    """
    dct = {"basketball":5, "soccer":11, "baseball":9}
    # 키 찾기
    print("baseball" in dct)
    print("volleyball" in dct)
    # 값 찾기
    print(9 in dct.values())

    print(dct.keys())
    print(dct.values())
    print(dct.items())

    dct[True] = "true"
    dct[10] = 10
    dct["eleven"] = 11
    dct[(1, 2, 3)] = 6
    print(dct)

    # dct[[1, 2, 3]] = 5  # error!!


def dictionary_method():
    """
    dictionary 메소드
    """
    dct = {"basketball":5, "soccer":11, "baseball":9}
    print(dct)

    keys = dct.keys()
    print(keys, type(keys))
    lst_keys = list(keys)
    print(lst_keys, type(lst_keys))

    values = dct.values()
    print(values, type(values))

    items = dct.items()
    print(items, type(items))
    lst_items = list(items)
    print(lst_items, type(lst_items))

    print("key:", lst_items[1][0], "value:", lst_items[1][1])

    dct.clear()
    print(dct)


def using_dictionary():
    phones = {
        "둘리": "010-3456-7890",
        "마이콜": "010-3456-7892",
        "또치": "010-3456-7893",
        "도우너": "010-3456-7894"
    }
    print(phones)

    # key vs get()
    print("둘리:", phones["둘리"])
    print("둘리:", phones.get("둘리"))

    # print("고길동", phones["고길동"])  # key error 발생
    print("고길동:", phones.get("고길동"))  # None 출력
    print("고길동:", phones.get("고길동", "사실 잘 모름"))  # default값 출력
    
    del phones["둘리"]
    print(phones)
    print(phones.pop("마이콜"), phones)


def loop():
    phones = {
        "둘리": "010-3456-7890",
        "마이콜": "010-3456-7892",
        "또치": "010-3456-7893",
        "도우너": "010-3456-7894"
    }

    for key, value in phones.items():
        print(key, ":", value)
    print("===============")
    for key in phones:
        print(key, ":", phones.get(key))
    print("===============")
    for key in sorted(phones):
        print(key, ":", phones.get(key))
    print("===============")
    for key in sorted(phones, reverse=True):
        print(key, ":", phones.get(key))
    print("===============")
    

if __name__ == '__main__':
    # define_dectionary()
    # dictionary_oper()
    # dictionary_method()
    # using_dictionary()
    loop()