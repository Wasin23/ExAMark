import os
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
load_dotenv()

# Get environment variables directly from Streamlit secrets
openai_key = os.environ["OPENAI_API_KEY"]
serper_key = os.environ["SERPER_API_KEY"]

# Setup memory
memory = ConversationBufferMemory(memory_key="chat_history")

# Setup search tool
search_tool = SerperDevTool(api_key=serper_key)

# Define chatbot agent
chatbot = Agent(
    role="Exabits Chatbot",
    goal="Respond to user questions conversationally using real data and memory.",
    backstory="An AI trained to answer FAQs and provide intelligent responses about the company Exabits.",
    verbose=True,
    memory=memory,
    allow_delegation=False,
    tools=[search_tool],
    llm=ChatOpenAI(openai_api_key=openai_key, model="gpt-4", temperature=0)
)

def run_chatbot(user_input: str) -> str:
    task = Task(
        description=f"Respond to the user's message: '{user_input}'",
        agent=chatbot,
        expected_output="A thorough and professional response to the user's message."
    )
    crew = Crew(
        agents=[chatbot],
        tasks=[task],
        verbose=False
    )
    return crew.kickoff()

