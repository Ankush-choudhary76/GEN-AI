

# from openai import OpenAI
# client = OpenAI(
#   base_url="https://openrouter.ai/api/v1",
#   api_key="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",
# )
# completion = client.chat.completions.create(
#   extra_headers={
#     "HTTP-Referer": "<YOUR_SITE_URL>", 
#     "X-Title": "<YOUR_SITE_NAME>", 
#   },
#   model="meta-llama/llama-3.3-70b-instruct:free",
#   messages=[
#     {
#       "role": "user",
#       "content": "capital of india ?"
#     }
#   ]
# )
# print(completion.choices[0].message.content)


# from langchain_openai import ChatOpenAI


# llm = ChatOpenAI(
#     base_url="https://openrouter.ai/api/v1",
#     api_key="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",
#     model="meta-llama/llama-3.3-70b-instruct:free"
# )


# response = llm.invoke("capital of india ?")
# print(response.content)



from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    model="meta-llama/llama-3.3-70b-instruct:free"
)


response = llm.invoke("capital of india ?")
print(response.content)
