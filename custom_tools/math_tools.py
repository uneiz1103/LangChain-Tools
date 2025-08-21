from langchain_core.tools import tool

@tool
def multiply(a: int , b: int) -> int:
    """Multiply two numbers"""
    return a * b

result = multiply.invoke({"a" : 10, "b": 20})

print(result)