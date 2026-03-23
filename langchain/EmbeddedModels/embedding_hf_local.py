from langchain_huggingface import HuggingFaceEmbeddings

# This will download the model locally (first time only) and run on your machine.
embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2'  )

text = "Delhi is the capital of India."

vector = embedding.embed_query(text)

print(f"Vector Length: {len(vector)}")
print(f"First 5 elements: {vector[:5]}")




