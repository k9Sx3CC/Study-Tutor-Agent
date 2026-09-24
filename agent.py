import os

from crewai import Agent, LLM

from tools import calculator, study_planner


def create_tutor_agent():
    llm = LLM(
        model="groq/openai/gpt-oss-120b",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.3,
    )

    tutor = Agent(
        role="Study Tutor",
        goal=(
            "Help students understand academic topics clearly, "
            "step by step, at their selected difficulty level."
        ),
        backstory=(
            "You are a patient and supportive study tutor. "
            "You explain difficult concepts using simple language, "
            "examples, and practice questions. "
            "You focus on helping students understand concepts rather "
            "than simply giving them answers."
        ),
        llm=llm,
        tools=[calculator, study_planner],
        verbose=True,
        allow_delegation=False,
    )

    return tutor
