# agent.py
import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

MODEL = "groq/llama-3.3-70b-versatile"   # ✅ Latest working Groq model


# -------------------------
# AGENTS
# -------------------------

Requirement_Agent = Agent(
    name="Requirement Understanding Agent",
    role="Requirement Specialist",
    goal="Understand the user's intention and extract clear prompt requirements.",
    backstory="You are an expert in analyzing user needs before writing prompts.",
    llm=MODEL,
)

Prompt_Agent = Agent(
    name="Prompt Engineering Agent",
    role="Prompt Engineer",
    goal="Create the perfect optimized AI prompt based on user requirements.",
    backstory="You design powerful prompts trusted by top AI companies.",
    llm=MODEL,
)

Enhancement_Agent = Agent(
    name="Enhancement Agent",
    role="Prompt Improver",
    goal="Enhance the prompt for clarity, tone, structure, and effectiveness.",
    backstory="You refine prompts to make them extremely effective for LLMs.",
    llm=MODEL,
)


# -------------------------
# TASKS
# -------------------------

req_task = Task(
    description="Extract clear structured requirements from the user's input: {user_input}",
    expected_output="A structured requirement summary.",
    agent=Requirement_Agent,
)

prompt_task = Task(
    description="Using requirements, write a complete optimized AI prompt.",
    expected_output="A fully structured professional prompt.",
    agent=Prompt_Agent,
)

enhance_task = Task(
    description="Polish the prompt to perfection.",
    expected_output="A final production-ready prompt.",
    agent=Enhancement_Agent,
)


# -------------------------
# CREW
# -------------------------

crew = Crew(
    agents=[Requirement_Agent, Prompt_Agent, Enhancement_Agent],
    tasks=[req_task, prompt_task, enhance_task],
    process=Process.sequential,
)


def generate_prompt(user_input: str):
    try:
        result = crew.kickoff({"user_input": user_input})
        return result
    except Exception as e:
        return f"Error generating prompt: {str(e)}"
