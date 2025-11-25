from langchain import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_experimental.sql import SQLDatabaseChain
from sqlalchemy import create_engine
import sqlite3

llm = ChatOpenAI(temperature=0.0)

db = SQLDatabaseChain.from_uri("sqlite:///retail.db", llm=llm)

while True:
    q = input("Ask a retail sales question: ")
    if q.lower() == "exit": break
    response = db.run(q)
    print("\nAI Response:\n", response)
