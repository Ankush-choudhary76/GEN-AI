

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
    model="google/gemma-3-12b-it:free"

)


response = llm.invoke("capital of india ?")
print(response.content)
