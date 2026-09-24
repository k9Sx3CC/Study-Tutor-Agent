from crewai.tools import tool


# =========================================================
# CALCULATOR TOOL
# =========================================================

@tool("Calculator")
def calculator(expression: str) -> str:
    """
    Calculate a basic mathematical expression.

    Example:
    25 * 18
    """

    try:

        allowed_characters = (
            "0123456789+-*/(). "
        )

        if not all(
            character in allowed_characters
            for character in expression
        ):

            return (
                "I can only calculate basic "
                "mathematical expressions."
            )


        result = eval(
            expression,
            {
                "__builtins__": {}
            },
            {},
        )


        return str(result)


    except Exception:

        return (
            "I could not calculate that expression. "
            "Please check the mathematical expression."
        )


# =========================================================
# STUDY PLANNER TOOL
# =========================================================

@tool("Study Planner")
def study_planner(
    topic: str,
    days: int,
) -> str:
    """
    Create a simple study plan for a topic.
    """

    try:

        days = int(days)

    except ValueError:

        return "Please provide the number of study days as a number."


    if days < 1:

        return "The study period must be at least 1 day."


    if days > 30:

        return (
            "For this MVP, please choose a study period "
            "of 30 days or less."
        )


    plan = []

    for day in range(
        1,
        days + 1,
    ):

        plan.append(
            f"Day {day}: Study an important concept "
            f"from {topic} and complete practice questions."
        )


    return "\n".join(plan)
