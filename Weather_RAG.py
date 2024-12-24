import requests
from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from langchain.agents import Tool
from langchain.chains import SQLDatabaseChain
from langchain.sql_database import SQLDatabase
import psycopg2
import openai

# Initialize OpenAI model (ensure you have your OpenAI API key)
openai.api_key = "your-openai-api-key"

# System prompt to guide the agent's behavior
system_prompt = """
You are a helpful assistant with access to a knowledge base and an external weather API. You should answer the user's questions accurately and clearly. 
When the user asks about specific weather information, retrieve it using the weather API. If the user asks for information available in the knowledge base, query the database.
Be polite, concise, and informative in your responses. 
"""

# Initialize the language model with the system prompt
llm = ChatOpenAI(
    model="gpt-4", 
    system_message=system_prompt  # Set the system prompt to guide behavior
)

# Connect to PostgreSQL (or other database of choice)
conn = psycopg2.connect(
    dbname="your_db", 
    user="your_user", 
    password="your_password", 
    host="your_host", 
    port="your_port"
)

# Create SQLDatabase instance
db = SQLDatabase(conn)

# Initialize the SQLDatabaseChain (handles querying the database)
db_chain = SQLDatabaseChain(llm=llm, database=db)

# Define a function to call an external API (for example, a weather API)
def get_weather(city: str) -> str:
    api_key = "your-weather-api-key"  # Replace with your weather API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        main = data["main"]
        weather_description = data["weather"][0]["description"]
        temperature = main["temp"]
        return f"The current temperature in {city} is {temperature}°C with {weather_description}."
    else:
        return "Sorry, I couldn't retrieve the weather information right now."

# Define an API tool that calls the weather API
weather_tool = Tool(
    name="WeatherAPI",
    func=get_weather,
    description="Use this tool to get the current weather of a city."
)

# Initialize a SQLDatabaseChain (handles querying the database)
tools = [
    Tool(
        name="KnowledgeBaseDB",
        func=db_chain.run,  # Calls the database query function
        description="Use this tool to query the knowledge base in the database."
    ),
    weather_tool  # Add the weather API tool to the list of tools
]

# Initialize the agent with both tools and the language model
agent = initialize_agent(
    tools=tools, 
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,  # This agent uses descriptions to determine which tool to use
    llm=llm, 
    verbose=True
)

# CLI Loop to interact with the agent
def start_conversation():
    print("Hello! I am your chatbot. You can ask me anything. Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        response = agent.run(user_input)
        print(f"Agent: {response}")

# Start the conversation
if __name__ == "__main__":
    start_conversation()
