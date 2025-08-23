from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
import requests

search_tool = DuckDuckGoSearchRun()
results = search_tool.invoke('who has win ipl this year in india')
# print(results)

@tool
def get_weather_data(city: str) -> str:
    """
    This function fetches the current weather data for a given city
    """

    url = f'https://api.weatherstack.com/current?access_key=4d1d8ae207a8c845a52df8a67bf3623e&query={city}'

    response = requests.get(url)

    return response.json()


llm = ChatOpenAI()

# step 2: pull the ReAct prompt from LangChain Hub
prompt = hub.pull("hwchase17/react") #pulls the standard ReAct agent prompt


# step 3: Create the ReAct agent manually with the pulled prompt
agent = create_react_agent(
    llm=llm,
    tools=[search_tool, get_weather_data],
    prompt=prompt
)
# step 4: Wrap it with AgentExecutor
agent_executor = AgentExecutor(
    agent=agent,
    tools=[search_tool, get_weather_data],
    verbose=True
)

response = agent_executor.invoke({"input": "3 ways to reach goa from delhi"})
# print(response)
# print(response['output'])
# Thought , action, observation

# Entering new AgentExecutor chain...
# Thought: The user is asking two related questions.
# Action: Use knowledge to find the capital of France.
# Observation: The capital of France is Paris.
# Thought: Now I need the population of Paris.
# Action: Search API[ "population of Paris 2025" ]
# Observation: Around 2.1 million people (city proper).
# Thought: I now have both answers.




