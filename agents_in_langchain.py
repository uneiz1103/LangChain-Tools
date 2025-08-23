from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
import requests

search_tool = DuckDuckGoSearchRun()

results = search_tool.invoke('top news in india today')

print(results)