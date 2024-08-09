def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def main():
    print("Welcome to calculator!, 이 모듈은 최상위 모듈입니다.")


if __name__ == "__main__":
    main()
else:
    print("이 모듈은 다른 곳에서 불러와 쓰기 위한 용도로 사용됩니다. 모듈:", __name__)