import os
from dotenv import load_dotenv

from basics.textsummariser import summarizer
from basicSearchAgent.searchAgent import run_agent

load_dotenv()

def main():
    #summarizer()
    run_agent()

if __name__ == "__main__":
    main()
