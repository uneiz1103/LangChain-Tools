from langchain.tools import StructuredTool
from pydantic import Field, BaseModel

class MultiplyInput(BaseModel):
    a: int = Field(required = True, description="first number to multiply")
    b: int = Field(required = True, description="second number to multiply")

def multiply_func(a: int , b: int) -> int:
    return a * b

multiply_tool = StructuredTool.from_function(
    name='multiply',
    description="Multiply two numbers",
    args_schema=MultiplyInput,
    func=multiply_func
)

result = multiply_tool.invoke({'a': 20, 'b': 10})

print(result)
print(multiply_tool.name)
print(multiply_tool.description)
print(multiply_tool.args)