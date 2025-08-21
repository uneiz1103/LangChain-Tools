from langchain_core.tools import tool

@tool
def mul(a: int , b: int) -> int:
    """mul two numbers"""
    return a * b

@tool
def add(a: int , b: int) -> int:
    """Add two numbers"""
    return a + b

@tool
def sub(a: int, b: int) -> int:
    """sub two numbers""" 
    return a - b

class MathToolKit:
    def get_tools(self):
        return [add, sub, mul]
    
toolkit = MathToolKit()

tools = toolkit.get_tools()

result = add.invoke({'a': 10, 'b': 20})
print(add.name,": " , result)

for tool in tools:
    print(tool.name, "=>" , tool.description)


