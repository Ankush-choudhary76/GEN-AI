import os
from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path=os.path.join(os.path.dirname(__file__), 'Social_Network_Ads.csv'))

docs = loader.load()

print(len(docs))
print(docs[1])