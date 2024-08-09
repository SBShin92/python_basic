from point import Point


def bound_instance_method():
    p = Point()
    p.set_x(10)
    p.set_y(20)

    print(p.get_x(), p.get_y(), sep=",")
    print(p.get_x, p.get_y)


def unbound_instance_method():
    p = Point()
    Point.set_x(p, 30)
    Point.set_y(p, 40)
    print(Point.get_x(p), Point.get_y(p), sep=",")
    print(Point.get_x, Point.get_y)


def class_member_test():
    p1 = Point()
    p1.set_x(50)
    p1.set_y(60)
    print(p1.get_x(), p1.get_y(), p1.instance_count)

    p2 = Point()
    p2.set_x(50)
    p2.set_y(60)
    print(p2.get_x(), p2.get_y(), p2.instance_count)

    print(p1.x is p2.x)
    print(p1.instance_count is p2.instance_count)


def stringify():
    p = Point(10, 20)
    print(p)
    print(repr(p))  # 원래 객체를 재현할 수 있는 문자열 출력

    p_repr = eval(repr(p))  # 이렇게
    print(p_repr)


from point import Singleton


def singleton_test():
    s = Singleton()
    print(s)
    # s2 = Singleton()
    s2 = Singleton.get_class_instance()
    print(s2)
    s3 = Singleton.get_static_instance()
    print(s3)


# 연습문제: 산술연산자, 역이항연산자, 비교연산자 중
# 몇개 오버로딩 해보셈
def oper_overload():
    p = Point(10, 20)
    print(p + 10)
    print(p + Point(10, 20))

    print(10 + p)
    print(p)

    p1 = Point(5, 20)
    p2 = Point(10, 15)
    print(p1 == p2)

    p1 << Point(15, 25)
    print(p1 >= p2)
    print(p1 <= p2)






if __name__ == '__main__':
    # bound_instance_method()
    # unbound_instance_method()
    # class_member_test()
    # stringify()
    # singleton_test()
    oper_overload()