from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain.agents import create_agent
from tavily import TavilyClient





@tool
def webSearch(query:str) -> str:
    """
    Tool that search on the internet for the query provided
    Args:
        query: The query to search in the web
    Returns:
        The search results
    """
    print (f"searching fro {query}")
    return "Todays is very hot in singpaore"

@tool
def webSearch_tavily(query:str) -> str:
    """
    Tool that search on the internet for the query provided using tavily api
    Args:
        query: The query to search in the web
    Returns:
        The search results
    """
    tavily = TavilyClient()
    return tavily.search(query)


def run_agent():
    llm = ChatOpenAI()
    tools = [webSearch_tavily]
    agent = create_agent(llm, tools)
    response = agent.invoke({"messages":[HumanMessage(content="What is the weather in singapore?")]})
    print(response)



