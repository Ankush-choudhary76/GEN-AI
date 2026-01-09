from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
import requests
from langchain_community.tools import DuckDuckGoSearchRun
import sys
from langchain.agents import create_agent
from dotenv import load_dotenv
import os 
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise SystemExit("ERROR: OPENROUTER_API_KEY not set in environment or .env")
os.environ['LANGCHAIN_PROJECT']= '  agent  LLM app'
try:
    search_tool = DuckDuckGoSearchRun()
except Exception as e:
    print("DuckDuckGoSearchRun requires the 'ddgs' package. Install with: pip install -U ddgs")
    print("Alternatively, create and use a virtualenv with the project's dependencies")
    sys.exit(1)

@tool
def get_weather_data(city: str) -> str:
  """
  This function fetches the current weather data for a given city
  """
  url = f'https://api.weatherstack.com/current?access_key=f07d9636974c4120025fadf60678771b&query={city}'

  response = requests.get(url)

  return response.json()

llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

# Minimal system prompt (avoids needing LangChain Hub pull)
prompt_text = (
    "You are a ReAct-style agent. Answer using available tools when needed. "
    "If you must call a tool, do so; otherwise answer directly from the model."
)

# Step 3: Create the agent with the factory
agent_graph = create_agent(
    model=llm,
    tools=[search_tool, get_weather_data],
    system_prompt=prompt_text,
)

# What is the release date of Dhadak 2?
# What is the current temp of gurgaon
# Identify the birthplace city of Kalpana Chawla (search) and give its current temperature.

# Step 5: Invoke
result = agent_graph.invoke({"input": "What is the current temp of gurgaon"})
print(result)
try:
    print(result.get('output') if isinstance(result, dict) else result)
except Exception:
    pass
