# main.py
def greet(name: str) -> str:
    return f"Hi {name}, welcome!"

def farewell(name: str) -> str:
    return f"Goodbye, {name}!"

def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

print(greet("World"))
print(farewell("World"))
print(add(5, 3))
print(subtract(10, 4))
