from langchain_core.tools import tool
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import requests
from langchain_core.messages import HumanMessage

load_dotenv()

@tool
def get_conversion_factor(base_currency: str, target_currency: str) -> float:
    """
    This function fetches the currency conversion factor between a given base currency and a target currency
    """
    url = f'https://v6.exchangerate-api.com/v6/f937510f42888d98a4dd7a/pair/{base_currency}/{target_currency}'
    # url = f'https://v6.exchangerate-api.com/v6/YOUR-API-KEY/pair/EUR/GBP'

    response = requests.get(url)    
    return response.json()

result = get_conversion_factor.invoke({'base_currency': 'USD', 'target_currency': 'INR'})
# print(result)

@tool
def convert(base_currency_value: int, conversion_rate: float) -> float:
    """
    Given a currency conversion rate this function calculates the target currency value from a given base currency value
    """

    return base_currency_value * conversion_rate


answer = convert.invoke({'base_currency_value': 10, 'conversion_rate': 87.23})
# print(answer)

llm = ChatOpenAI()

llm_with_tools =  llm.bind_tools([get_conversion_factor, convert])

messages = [HumanMessage('what is the conversion factor between USD and INR, and based on that can you convert 10 usd to inr')]



