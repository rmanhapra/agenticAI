from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama


def summarizer():
    information = """
    Donald Trump is an American politician, businessman, and media personality who serves as the 47th President of the United States, having also served as the 45th President from 2017 to 2021.Early Life and EducationDonald Trump was born on June 14, 1946, in Queens, New York City, as the fourth of five children of real estate developer Fred Trump and Mary MacLeod.-- [Britannica].He attended Fordham University before transferring to the Wharton School of the University of Pennsylvania, where he graduated with a bachelor's degree in economics in 1968.Business and Media CareerHe joined his father's real estate firm and took control in 1971, renaming it the Trump Organization.He expanded the business into skyscrapers, luxury hotels, casinos, and golf courses, most notably constructing Trump Tower on Fifth Avenue in Manhattan.From 2004 to 2015, he hosted the reality television show The Apprentice, bolstering his reputation as a wealthy tycoon.-- [Wikipedia].Political Career and PresidencyTrump entered national politics and won the 2016 presidential election as the Republican nominee, defeating Democratic candidate Hillary Clinton.His first presidential term (2017–2021) focused on conservative judicial appointments, tax cuts, deregulation, and a nationalist trade and foreign policy.After losing the 2020 election to Joe Biden, he ran again and secured a historic nonconsecutive second term, taking office as the 47th President in January 2025.
    """

    summary_template = """
    Summarise the following information:
    {information} and tell me 1. A short summary 2. 2 interestign facts
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)
   # llm = ChatOpenAI(model="gpt-5", temperature=0)
    llm = ChatOllama(model="gemma3:270m", temperature=0)
    chain = summary_prompt_template | llm
    response = chain.invoke({"information": information})
    print(response.content)