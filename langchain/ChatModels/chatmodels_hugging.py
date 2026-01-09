# from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
# from dotenv import load_dotenv

# load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task = "text-generation"
# )

# model = ChatHuggingFace(llm = llm)

# re = model.invoke("what is capital of india")

# print(re)



from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    max_new_tokens=256,
    temperature=0.7,
)

chat = ChatHuggingFace(llm=llm)
print(chat.invoke([("human", "What is the capital of India?")]).content)
