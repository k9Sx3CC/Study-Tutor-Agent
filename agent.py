import os

from crewai import Agent, Crew, LLM, Task

from tools import calculator, study_planner


class StudyTutor:

    def __init__(self):

        # -----------------------------------------
        # Groq LLM
        # -----------------------------------------

        self.llm = LLM(
            model="groq/openai/gpt-oss-120b",
            api_key=os.getenv("GROQ_API_KEY"),
            temperature=0.3,
        )


        # -----------------------------------------
        # Study Tutor Agent
        # -----------------------------------------

        self.agent = Agent(

            role="Personal Study Tutor",

            goal=(
                "Help students understand academic concepts, "
                "practice what they learn, and build confidence "
                "through clear step-by-step teaching."
            ),

            backstory=(
                "You are a patient and knowledgeable academic tutor. "
                "You teach rather than simply provide answers. "
                "You adapt your explanations to the student's level, "
                "use examples when useful, ask practice questions, "
                "and give constructive feedback. "
                "You should encourage understanding and independent thinking."
            ),

            llm=self.llm,

            tools=[
                calculator,
                study_planner,
            ],

            allow_delegation=False,

            verbose=False,
        )


    # =================================================
    # ASK THE TUTOR
    # =================================================

    def ask(
        self,
        question,
        subject,
        level,
        history,
    ):

        task = Task(

            description=f"""
You are tutoring a student.

SUBJECT:
{subject}

STUDENT LEVEL:
{level}

STUDENT QUESTION:
{question}

PREVIOUS CONVERSATION:
{history}

YOUR INSTRUCTIONS:

1. Answer the student's question clearly.

2. Adapt the explanation to the student's
   selected learning level.

3. Break difficult concepts into smaller
   understandable steps.

4. Use examples when they help understanding.

5. If the student asks a mathematical question
   requiring calculation, use the Calculator tool.

6. If the student asks for a study schedule
   or learning plan, use the Study Planner tool.

7. Do not use tools unnecessarily.

8. If the student asks a follow-up question,
   use the previous conversation to maintain context.

9. Do not pretend that you used a tool if you did not.

10. If the student's question is ambiguous,
    ask a short clarification question.

11. Encourage the student to understand the
    reasoning rather than simply memorizing an answer.

12. Keep explanations appropriate for the
    selected learning level.

RESPONSE STYLE:

Use clear headings when useful.

Prefer:
- Short paragraphs
- Bullet points
- Step-by-step explanations
- Examples
- Practice questions when appropriate

Avoid unnecessarily complicated language.
""",

            expected_output=(
                "A clear, accurate and level-appropriate tutoring response."
            ),

            agent=self.agent,
        )


        crew = Crew(

            agents=[
                self.agent
            ],

            tasks=[
                task
            ],

            verbose=False,

            memory=True,
        )


        result = crew.kickoff()


        return result
