from langchain_core.tools import tool
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import requests
from langchain_core.tools import InjectedToolArg
from typing import Annotated
from langchain_core.messages import HumanMessage
import json

load_dotenv()

@tool
def get_conversion_factor(base_currency: str, target_currency: str) -> float:
    """
    This function fetches the currency conversion factor between a given base currency and a target currency
    """
    url = f'https://v6.exchangerate-api.com/v6/YOUR-API-KEY/pair/{base_currency}/{target_currency}'
    # url = f'https://v6.exchangerate-api.com/v6/YOUR-API-KEY/pair/EUR/GBP'

    response = requests.get(url)    
    return response.json()

result = get_conversion_factor.invoke({'base_currency': 'USD', 'target_currency': 'INR'})
# print(result)

@tool
def convert(base_currency_value: int, conversion_rate: Annotated[float, InjectedToolArg]) -> float:
    """
    Given a currency conversion rate this function calculates the target currency value from a given base currency value
    """

    return base_currency_value * conversion_rate


answer = convert.invoke({'base_currency_value': 10, 'conversion_rate': 87.23})
# print(answer)

# tool binding
llm = ChatOpenAI()

llm_with_tools =  llm.bind_tools([get_conversion_factor, convert])

messages = [HumanMessage('what is the conversion factor between USD and INR, and based on that can you convert 10 usd to inr')]

# print(messages)

ai_message = llm_with_tools.invoke(messages)
# print(ai_message.tool_calls)


for tool_call in ai_message.tool_calls:
    # execute the 1st tool and get the value of conversion rate
    if tool_call['name'] == 'get_conversion_factor':
        tool_message1 = get_conversion_factor.invoke(tool_call)
    # fetch conversion rate
        conversion_rate = json.loads(tool_message1.content)['conversion_rate']
    # append this tool message to messages list
    messages.append(tool_message1)
    # execute the 2nd tool using the conversion rate from tool 1
    if tool_call['name'] == 'convert':
    # fetch the current argument
        tool_call['args'] ['conversion_rate'] = conversion_rate
        tool_message2 = convert.invoke(tool_call)
        messages.append(tool_message2)


llm_with_tools.invoke(messages).content


