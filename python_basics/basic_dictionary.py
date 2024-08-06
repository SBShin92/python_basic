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





if __name__ == '__main__':
    define_dectionary()