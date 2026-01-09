from langchain_openai import OpenAIEmbeddings 
from dotenv import load_dotenv 

load_dotenv()

embedding = OpenAIEmbeddings(model = 'text-embedding-3-lager' , dimension = 32)


result = embedding.embed_documents("capital of india ")

print(str(result))
