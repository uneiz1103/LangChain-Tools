from langchain_community.tools import DuckDuckGoSearchResults

search_result = DuckDuckGoSearchResults()

result = search_result.invoke('What is Deep learning')

print(result)