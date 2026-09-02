import os
from dotenv import load_dotenv

from basics.textsummariser import summarizer

load_dotenv()

def main():
    summarizer()


if __name__ == "__main__":
    main()
