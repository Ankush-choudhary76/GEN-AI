from langchain_openai import ChatOpenAI
import os 
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

os.environ['LANGCHAIN_PROJECT']= 'Sequential LLM app'
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

# model = ChatOpenAI()
model = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)
config={
    'run name': 'squential chain'
    'tags':['llm_app','report generation','summarization'],
    'metadata':{'model':'model','model_temp':0.7,'parser':'stroutputparser'}
}
parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser


result = chain.invoke({'topic': 'Unemployment in India'}, config = config)

print(result)
