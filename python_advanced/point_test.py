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
    p1.set_x([])
    p1.set_y(60)
    print(p1.get_x(), p1.get_y(), p1.instance_count)

    p2 = Point()
    p2.set_x([])
    p2.set_y(60)
    print(p2.get_x(), p2.get_y(), p2.instance_count)

    print(p1.x is p2.x)
    print(p1.instance_count is p2.instance_count)


if __name__ == '__main__':
    # bound_instance_method()
    # unbound_instance_method()
    class_member_test()