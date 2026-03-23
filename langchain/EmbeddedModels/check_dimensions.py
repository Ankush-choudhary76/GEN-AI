from langchain_huggingface import HuggingFaceEmbeddings

# Load the model
embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

# Test with very different text lengths
text_short = "Hi"
text_long = "Delhi is the capital of India. It has a rich history and culture. " * 10

vector_short = embedding.embed_query(text_short)
vector_long = embedding.embed_query(text_long)

print(f"Short text length: {len(text_short)} chars")
print(f"Short vector dimension: {len(vector_short)}")
print("-" * 20)
print(f"Long text length: {len(text_long)} chars")
print(f"Long vector dimension: {len(vector_long)}")
print("-" * 20)
print(f"Are dimensions equal? {len(vector_short) == len(vector_long)}")
