from langchain_openai import OpenAIEmbeddings 
from dotenv import load_dotenv 

load_dotenv()

embedding = OpenAIEmbeddings(model = 'text-embedding-3-lager' , dimension = 32)

documents = [

    "Delhi is the  capital of india",
    "Kolkata is the capital of west Bengal",
    "paris is the capital of france "
]

result = embedding.embed_documents(documents)

print(result)
