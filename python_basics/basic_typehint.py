# 변수 타입 힌트
age: int = 30
name: str = "홍길동"

age = "장길산"

def greet(name:str) -> None:  # 문제없이 실행됨
    return f"{name}님 안녕하세요."

print(greet("김철수"))


# 복잡한 타입힌트
from typing import List, Tuple, Set, Dict, Optional, Union, Any, Callable

numbers: List[int] = []
person: Tuple[str, int] = ("홍길동", 30)
user: Dict[str, str] = {"name": "김철수"}
unique_names: Set[str] = {"홍길동", "박영희", "김철수"}

# 옵션 타입 힌트
def find_user(user_id: str) -> Optional[str]:
    if user_id == "1":
        return "홍길동"
    else:
        return None
    
# 유니온 타입 힌트
def process_value(value: Union[int, float]) -> str:
    return str(value)

# 함수 데이터 타입 힌트
def execute_op(op: Callable[[int, int], int], a: int, b: int) -> int:
    return op(a,b)