from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
import os
load_dotenv()

# Define the model
model = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    model="google/gemma-3-12b-it:free"
)

class Person(BaseModel):

    name: str = Field(description='Name of the person')
    age: int = Field(gt=18, description='Age of the person')
    city: str = Field(description='Name of the city the person belongs to')

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='Generate the name, age and city of a fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

# prompt = template.invoke({'place':'sri lankan'})

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

# print(final_result)

# print(type(final_result))



chain = template | model | parser

final_result = chain.invoke({'place':'sri lankan'})

print(final_result)

print(type(final_result))
