# Chatbot with LangChain, Weather API, and Knowledge Base Integration

This script creates a conversational chatbot using LangChain, OpenAI, and a PostgreSQL database. It allows users to interact with the chatbot via the command line interface (CLI), where the chatbot can provide answers by querying a knowledge base (database) or fetching information from an external weather API.

## Features:
- Access a PostgreSQL database for information retrieval.
- Fetch weather information from an external weather API (e.g., OpenWeatherMap).
- Use OpenAI's GPT model to generate responses.
- CLI-based conversation with an interactive agent.

---

## Requirements

To run this script, ensure you have the following:

1. **Python 3.x** installed on your machine.
2. **Dependencies**: The following Python packages are required:
   - `requests`
   - `psycopg2`
   - `langchain`
   - `openai`

You can install the dependencies by running: `pip install requests psycopg2 langchain openai`


## API Keys

**OpenAI API Key:**

You need to set up an OpenAI account and obtain an API key to use GPT models. Refer to the OpenAI documentation for instructions on creating an account and obtaining an API key: [OpenAI API Documentation](https://beta.openai.com/docs/api-reference/introduction)

**Weather API Key:**

For weather data, you can use any external weather API service like OpenWeatherMap. Obtain an API key from the chosen weather API service and use it in the script.

**PostgreSQL Database:**

Ensure you have access to a PostgreSQL database (or modify the script for another type of database). Create a database with appropriate data for queries, or use any existing database for knowledge base queries. Update the database connection details (name, user, password, host, port) in the script.

## Setup

1. Clone this repository (or save the script locally):
2. Add Your API Keys in the placeholders and configure Db connection in the script
3. CD to gitfolder enclosing this script and run: `python chatbot.py`

## Example Usage

Once the script is running, you can interact with the chatbot in the terminal:
Example Dialogue:

```
Hello! I am your chatbot. You can ask me anything. Type 'exit' to end the conversation.
You: What's the weather in Paris?
Agent: The current temperature in Paris is 15°C with clear sky.
You: What is the capital of France?
Agent: The capital of France is Paris.
You: exit
Goodbye!
```
To end the conversation, simply type exit at any time.
