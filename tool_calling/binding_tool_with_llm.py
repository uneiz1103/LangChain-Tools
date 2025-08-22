from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

# tool creation
@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

# Tool binding

llm = ChatOpenAI()

llm_with_tools =  llm.bind_tools([multiply])

# Tool calling

query = HumanMessage('can you multiply 3 with 10')

messages = [query] 
# It will give human message

result = llm_with_tools.invoke(messages)

messages.append(result)
# it will give human message + AI message

print(result.tool_calls[0]['args'])
# we get this:
    # 'args': {'a': 3, 'b': 10}


# tool execution
tool_result = multiply.invoke(result.tool_calls[0])

messages.append(tool_result)
# It will give Human message + AI message + tool message


# we get this:
# multiply.invoke({
#     'name': 'multiply',
#     
#     'id': 'call_Mn0aMG6dPrW4memyAbaBYj8j',
#     'type': 'tool_call'
# })

# result will be 30


# we will get:
# ToolMessage(content:'30', name: 'multiply', tool_call_id: 'call_Mn0aMG6dPrW4memyAbaBYj8j')


llm_with_tools.invoke(messages)