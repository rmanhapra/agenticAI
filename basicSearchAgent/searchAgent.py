from typing import List
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain.agents import create_agent
from tavily import TavilyClient
from langchain_tavily import TavilySearch
from pydantic import BaseModel, Field





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
    llm = ChatOpenAI(model="gpt-5")
    tools = [TavilySearch()]
   # tools = [webSearch_tavily]
   
   # agent = create_agent(llm, tools)
    agent = create_agent(llm, tools, response_format=AgentResponse)
    response = agent.invoke({"messages":[HumanMessage(content="get me 5 jobs for databricks lakebase in singapore?")]})
    print(response)

class Source(BaseModel):
    """ Schema for a source used by agent"""
    url:str = Field(description="url of the source")


class AgentResponse(BaseModel):
    """ Schema for Agents response with answer and the sources it checked"""

    answer:str = Field("Agents answer to the query")
    sources: List[Source] = Field(default_factory=list, description="List of sources to generate the answer")





