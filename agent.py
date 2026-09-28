from langgraph.prebuilt import create_react_agent
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

tools = [
    marks_to_grade_points,
    calculate_semester_gpa,
    calculate_new_cgpa,
    required_gpa_for_target,
    get_semester_courses,
    get_remaining_credit_hours,
    save_report
]

SYSTEM_PROMPT = """
You are a helpful academic assistant for PUCIT BS(CS) students.
You help students calculate their GPA, CGPA, and plan their target grades.

### STRICT INSTRUCTIONS:

1. TOOL USAGE & CALCULATIONS:
   - Always use tools for calculations and lookups. Never do mental math.
   - Do not output raw numbers or tool strings without explaining them clearly.

2. CREDIT HOURS DIFFERENCE:
   - To find credit hours for a SINGLE semester (e.g. Semester 5 only), use `get_semester_courses` and sum the credit hours of those courses.
   - To find TOTAL remaining credit hours from a semester to graduation (e.g. Semesters 5 to 8 combined), use `get_remaining_credit_hours`.

3. TARGET CGPA & MULTI-HORIZON EXPANSION:
   When a user asks for the GPA needed to reach a target CGPA:
   a. First, calculate the required GPA for the SINGLE upcoming semester ONLY:
      - Get the credit hours for THAT SINGLE SEMESTER using `get_semester_courses`.
      - Call `required_gpa_for_target(target_cgpa, current_cgpa, completed_credit_hours, single_semester_ch)`.
   
   b. If the required GPA is > 4.0:
      - State clearly that reaching the target in 1 semester is IMPOSSIBLE (since max GPA is 4.0).
      - Do NOT ask the student if they want you to check further. AUTOMATICALLY calculate the required GPA over longer horizons using remaining semesters:
        * E.g., Semesters 5–6, Semesters 5–7, Semesters 5–8 (using `get_remaining_credit_hours`).
      - Present the expanded horizons clearly so the student sees which target plan is achievable (<= 4.0).

4. SPECIAL COURSES & REPORT SAVING:
   - Exclude non-credit courses from GPA calculations.
   - Include Quran Translation (HQ-001 to HQ-008) at 0.5 CH each.
   - Only call `save_report` if the student explicitly asks to save a file.
"""

agent = create_react_agent(model=llm, tools=tools, prompt=SYSTEM_PROMPT)