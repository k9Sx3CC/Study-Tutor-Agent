from crewai.tools import tool


@tool("Calculator")
def calculator(expression: str) -> str:
    """Calculate a basic mathematical expression."""

    try:
        allowed_characters = "0123456789+-*/(). "

        if not all(char in allowed_characters for char in expression):
            return "I can only calculate basic mathematical expressions."

        result = eval(expression, {"__builtins__": {}}, {})

        return str(result)

    except Exception:
        return "I could not calculate that expression."


@tool("Study Planner")
def study_planner(topic: str, days: int) -> str:
    """Create a simple study plan for a topic."""

    if days < 1:
        return "The number of days must be at least 1."

    if days > 30:
        return "Please choose a study period of 30 days or less."

    plan = []

    for day in range(1, days + 1):
        plan.append(
            f"Day {day}: Study an important part of {topic} and complete practice questions."
        )

    return "\n".join(plan)
