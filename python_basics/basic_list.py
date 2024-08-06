def lst_delete():
    a = [1, 12, 123, 1234]
    a[0:1] = []
    print(a)
    a.pop(1)
    print(a)

def define_list():
    """
    리스트 생성 관련 샘플 코드
    """
    lst1 = list()
    print(lst1, type(lst1))
    lst2 = [0] * 5
    print(lst2, type(lst2))
    print(lst2[:])
    lst3 = [0] * 5 + ["Python"]    # 리스트 확장
    print(lst3[:])
    lst4 = list("Python")  # 리스트 자료형으로 변환
    print(lst4)

def list_oper():
    """
    리스트 연산 연습
    """
    lst = [1, 2, "Python"]
    print(lst, "length: ", len(lst))  # 길이 확인
    print(lst[0], lst[1], lst[2])  # 정방향 인덱싱
    print(lst[-1], lst[-2], lst[-3]) # 역방향 인덱싱

    # 슬라이스
    print(lst[0:2])
    print(lst[:1], lst[-3:])
    print(lst[::2])
    print(lst[::-1])

    # 리스트 카피
    cp = lst[:]
    print(cp)
    print(id(lst), id(cp))
    print(lst is cp)  # False
    print(lst == cp)  # True

    # append vs extend
    print(cp)
    cp.append(["Java", True, 3.141592])
    print(cp)
    cp.extend(["Java", True, 3.141592])
    print(cp)
    cp.insert(2, [1, 2, 3])   # 인덱스 2에 [1, 2, 3] 추가
    print(cp)

    print("Python" in cp)
    print(3 in cp)
    
    print("Index:", cp.index("Python"))
    print("Index:", cp.index("Java"))
    
    # 요소의 개수 확인
    print(cp.count("Python"))

    # 요소의 삭제
    print(cp)
    cp.remove("Python")
    print(cp)

    #slicing의 활용
    lst2 = ["apple", "banana", "orange", 10, 20]
    print("lst2:", lst2)
    lst2[0:2] = lst2[3:5]
    print("lst2:", lst2)
    lst2[:2] = [10]
    print("lst2:", lst2)
    lst2[1:2] = [20]
    print("lst2:", lst2)
    lst2[2:] = [30]
    print("lst2:", lst2)


    # 슬라이싱을 이용한 삽입(insert)
    lst3 = [1, 12, 123, 1234]
    print("lst3:", lst3)

    lst3[1:1] = ['a']
    print("lst3:", lst3)
    lst3[len(lst3):] = [12345]
    print("lst3:", lst3)
    lst3[:0] = [0]
    print("lst3:", lst3)

    # 기초 산술 연산자 활용
    lst4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(lst4 + [4])
    print(lst4 * 5)
    print(len(lst4))
    print(max(lst4))
    print(min(lst4))
    print(sum(lst4))
    print("avg:", sum(lst4) / len(lst4))

def list_methods():
    lst = [4, 2, 666, 234, -6435]
    lst_copy = lst.copy()
    print("lst:", lst)
    lst.sort()
    print(lst)
    lst.reverse()
    print(lst)

    # sorted vs sort
    print("lst_copy:", lst_copy)

    print("lst_copy sorted:", sorted(lst_copy))
    print("lst_copy:", lst_copy)
    print("lst_copy sorted descending:", sorted(lst_copy, reverse=True))
    print("lst_copy:", lst_copy)

    # key 함수
    print("lst_copy sorted key=int", sorted(lst_copy, key=int))
    print("lst_copy sorted key=str", sorted(lst_copy, key=str))
    print("lst_copy 10 mod desc:", sorted(lst_copy, reverse=True, key=lambda x : x % 10))

def stack_ex():
    """
    리스트를 활용한 stack 자료형 흉내
    """
    stack = []
    stack.append(1)
    stack.append(2)
    stack.append(3)
    print("stack:", stack)

    print("popped:", stack.pop())
    print(stack)
    

def queue_ex():
    queue = []
    queue.append(1)
    queue.append(2)
    queue.append(3)
    print("queue:", queue)

    print("popped:", queue.pop(0))
    print(queue)


def loop():
    words = "Life is too short, you need Python.".replace(",", "").replace(".", "").split()
    print(words)
    for word in words:
        print(word)


if __name__ == '__main__':
    # define_list()
    # list_oper()
    # list_methods()
    # stack_ex()
    # queue_ex()
    # loop()
    a = {1, 2, 3}
    print(a, type(a))