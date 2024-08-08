import pickle

def write_file():
    f = open("./sample/test.txt", "wt", encoding="utf-8")
    txtlength = f.write("hello world")
    print(txtlength)
    f.close()


def write_file2():
    f = open("./sample/multilines.txt", "wt", encoding="utf-8")
    for i in range(1, 11):
        f.write("hello world, this is {}\n".format(i))
    f.close()


def read_file():
    f = open("./sample/multilines.txt", "rt")
    text = f.read()
    print(text, end="")
    f.close()


def read_file_by_line():
    with open("./sample/multilines.txt", "rt") as f:
        while True:
            line = f.readline()
            if not line:
                break
            print(line, end="")


def copy_binary_file():
    with open("./sample/rose-flower.jpeg", "rb") as f:
        data = f.read()
        with open("./sample/rose-flower-copy.jpeg", "wb") as cf:
            cf.write(data)
        print("copy success")


def serialize():
    with open("./sample/players.bin", "wb") as f:  # 총 3개의 객체 적재
        pickle.dump({"baseball", 9}, f, 1)
        pickle.dump({"basketball", 5}, f, pickle.HIGHEST_PROTOCOL)
        pickle.dump({"football", 11}, f)


def deserialize():
    lst = []
    try:
        with open("./sample/players.bin", "rb") as f:
            while True:
                lst.append(pickle.load(f))
    except EOFError:
        pass
    print(lst)


# 연습문제

# sangbuk.csv 읽어서, 기준으로 분할한 후 dict로 저장. 직렬화, 역직렬화. name, backno, height, position
# 읽기, 직렬화 따로
def read_sangbuk() -> list[dict]:
    result = []
    with open("./sample/sangbuk.csv", "r") as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            result.append(dict(zip(["name", "backno", "height", "position"], line.split(", "))))
    return result

def serialize_sangbuk():
    my_data = read_sangbuk()
    with open("./sample/sangbuk.bin", "wb") as f:
        pickle.dump(my_data, f)


# 읽기, 직렬화 같이
def read_serialize_sangbuk():
    with open("./sample/sangbuk.csv", "r") as f:
        with open("./sample/sangbuk.bin", "wb") as bf:
            while True:
                line = f.readline().strip()
                if not line:
                    break
                pickle.dump(dict(zip(["name", "backno", "height", "position"], line.split(", "))), bf)


# 역직렬화
def deserialize_sangbuk():
    try:
        with open("./sample/sangbuk.bin", "rb") as f:
            while True:
                print(pickle.load(f))
    except EOFError:
        pass


if __name__ == "__main__":
    # write_file()
    # write_file2()
    # read_file()
    # read_file_by_line()
    # copy_binary_file()
    # serialize()
    # deserialize()

    # serialize_sangbuk()  # 직렬화, 읽기 따로
    read_serialize_sangbuk()  # 직렬화, 읽기 같이
    deserialize_sangbuk()