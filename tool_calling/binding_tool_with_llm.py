from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

# tool creation
@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

# Tool binding

llm = ChatOpenAI()

llm_with_tools =  llm.bind_tools([multiply])

# Tool calling

result = llm_with_tools.invoke('can you multiply 3 with 10')

print(result.tool_calls[0]['args'])

# tool execution
multiply.invoke(result.tool_calls[0])
# result will be 30

# multiply.invoke({
#     'name': 'multiply',
#     'args': {'a': 3, 'b': 10},
#     'id': 'call_Mn0aMG6dPrW4memyAbaBYj8j',
#     'type': 'tool_call'
# })

# we will get:
# ToolMessage(content:'30', name: 'multiply', tool_call_id: 'call_Mn0aMG6dPrW4memyAbaBYj8j')




