from llm import llm
from tools import (
    marks_to_grade_points,
    calculate_semester_gpa,
    calculate_new_cgpa,
    required_gpa_for_target,
    get_semester_courses,
    get_remaining_credit_hours,
    save_report
)
from langgraph.prebuilt import create_react_agent

# List of all available tools for the agent
tools = [
    marks_to_grade_points,
    calculate_semester_gpa,
    calculate_new_cgpa,
    required_gpa_for_target,
    get_semester_courses,
    get_remaining_credit_hours,
    save_report
]

SYSTEM_PROMPT = """You are a helpful academic assistant for PUCIT BS(CS) students.
You help students calculate their GPA, CGPA, and plan their target grades.

Instructions:
- Always use the given tools for calculations. Do not calculate numbers in your head.
- If any important detail like semester, current CGPA, or target is missing, ask the student politely.
- If a target CGPA is too high for a single semester, check multiple remaining semesters using the tools to suggest a realistic plan.
- Only save reports to a file if the student asks you to do so.
"""

agent = create_react_agent(model=llm, tools=tools, prompt=SYSTEM_PROMPT)