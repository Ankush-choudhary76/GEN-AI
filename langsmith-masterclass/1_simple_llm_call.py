from dotenv import load_dotenv
import os 
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
 
# Simple one-line prompt
prompt = PromptTemplate.from_template("{question}")

model = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

parser = StrOutputParser()

# Chain: prompt → model → parser
chain = prompt | model | parser

# Run it
result = chain.invoke({"question": "What is the capital of Peru?"})
print(result)
