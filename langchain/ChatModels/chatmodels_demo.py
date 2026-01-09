from langchain_openai import ChatOpenAI
from dotenv import load_dotenv


load_dotenv()

model  =ChatOpenAI(model="gpt-4o-mini" , temperature = 1.5 , max_completion_tokens = 10 )
response = model.invoke("Explain LangChain in one sentence.")
print(response.content)
