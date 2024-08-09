class Point:
    instance_count = 0  # 클래스 멤버

    def __init__(self, x=0, y=0) -> None:
        self.x, self.y = x, y
        self.instance_count += 1

    def __del__(self):
        self.instance_count -= 1

    def set_x(self, x):
        self.x = x

    def get_x(self):
        return self.x
    
    def set_y(self, y):
        self.y = y

    def get_y(self):
        return self.y
    
    def __str__(self):
        return f"Point x = {self.x}, y = {self.y}"
    
    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"
    
    def __add__(self, other):  # Point + other
        if isinstance(other, int):
            self.x += other
            self.y += other
        elif isinstance(other, Point):  # Point + Point
            self.x += other.get_x()
            self.y += other.get_y()
        return self
    
    def __radd__(self, other):  # other + Point
        return self + other
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False


    # 연습문제: 산술연산자, 역이항연산자, 비교연산자 중
    # 몇개 오버로딩 해보셈

    def __lshift__(self, other):
        if isinstance(other, Point):
            print(f"좌항: Point({self.x}, {self.y})")
            print(f"우항: Point({other.x}, {other.y})")

    
    def __rlshift__(self, other):
        return self << other

    def __le__(self, other):
        if isinstance(other, Point):
            return self.x <= other.x
        
    
    def __ge__(self, other):
        if isinstance(other, Point):
            return self.y >= other.y



    # 싱글톤 예제

class Singleton:
    __instance = None

    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception("싱글톤 인스턴스는 이미 생성됐습니다.")
        else:
            Singleton.__instance = self
            print("싱글톤 인스턴스 생성 완료")

    @classmethod
    def get_class_instance(cls):
        if cls.__instance is None:
            cls()
        return cls.__instance
    
    @staticmethod
    def get_static_instance():
        if Singleton.get_class_instance() is None:
            Singleton()
        return Singleton.get_class_instance()
    