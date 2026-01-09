from langchain_openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

model = OpenAI(model="gpt-4")
response = model.invoke("Explain LangChain in one sentence.")
print(response.content)
