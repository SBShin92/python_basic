class MyString(str):
    pass


s = MyString()
print(s, "type:", type(s))

s = MyString("My Class")
print(MyString.__bases__)  # (str,)
print(MyString.__bases__[0].__bases__)  # (object,)

# s는 str의 모든 메소드를 사용할 수 있다.
print(s.lower())

# 부모가 여럿..?
class MyObj:
    pass


class Chimera(str, MyObj):
    pass


print(type(Chimera))
print(Chimera.__bases__)   # (str, MyObj)

# 하위클래스 확인
print(issubclass(Chimera, str), issubclass(Chimera, MyObj))

from point import Point
p = Point()

p.set_x(10)
p.set_y(20)
print(p, type(p),
      "x:", p.get_x(),
      "y:", p.get_y())