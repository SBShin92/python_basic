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
    f = open("./sample/multilines.txt", "rt")
    while True:
        line = f.readline()
        if not line:
            break
        print(line, end="")
    f.close()


if __name__ == "__main__":
    # write_file()
    # write_file2()
    # read_file()
    read_file_by_line()