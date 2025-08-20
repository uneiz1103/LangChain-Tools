from langchain_community.tools import DuckDuckGoSearchResults
from langchain_community.utilities.duckduckgo_search import DuckDuckGoSearchAPIWrapper

api = DuckDuckGoSearchAPIWrapper(source="news", time="d", max_results=5)
news_tool = DuckDuckGoSearchResults(api_wrapper=api, output_format="list")  
print(news_tool.invoke("rainfall India today"))
