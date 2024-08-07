# Built-in scope
print(len)  # 내장 함수 len

# Global scope
x = "global"

def outer_function():
    # Enclosed scope
    x = "enclosed"
    
    def inner_function():
        # Local scope
        x = "local"
        print("Inner:", x)
    
    inner_function()
    print("Outer:", x)

outer_function()
print("Global:", x)

print(dir())
print(dir("__builtins__"))