def define_tuple():
    tp1 = (1,)
    tp2 = tuple()
    t = 1, 2, 3, 4, 5
    print(t, type(t))


def tuple_oper():
    t = (1,)
    print(type(t), len(t))

    t = 1, 2, 3, 4, 5
    t = (1,) + t[1:]
    print(t)
    t = (1,) * 5
    print(t)


def tuple_assign():
    """
    튜플의 할당
    """
    t = 1, 2, 3, 4, 5
    print(t, type(t))

    a, *b, c = t
    print(a, b, c)

    a, c = c, a  # 치환
    print(a, c)


def tuple_method():
    """
    튜플의 메소드들
    """
    t = 20, 30, 10, 20
    print("count:", t.count(20))
    print("index:", t.index(20))
    print("index", t.index(20, 1))


def tuple_unpacking():
    """
    튜플 패킹, 언패킹
    """
    t = 10, 20, 30, "Python"
    print(t, type(t))
    a, b, c, d = t
    print(a, b, c, d)
    


if __name__ == "__main__":
    # define_tuple()
    # tuple_oper()
    # tuple_assign()
    # tuple_method()
    tuple_unpacking()