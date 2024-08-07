def dummy():
    pass

def times(a, b):
    return a * b

def none():
    return


print(none())

fun = times
print(fun, type(fun))

if callable(fun):
    print(fun(42, 42))