COURSES = {
    1: [
        ("MS-251", "Probability & Statistics", 3.0),
        ("GE-160", "Applications of ICT", 3.0),
        ("GE-169", "Applied Physics", 3.0),
        ("GE-167", "Discrete Structures", 3.0),
        ("HQ-001", "Quran Translation - I", 0.5),
        ("GE-190", "Functional English", 3.0)
    ],
    2: [
        ("CC-112", "Programming Fundamentals", 3.0),
        ("CC-112-L", "Programming Fundamentals Lab", 1.0),
        ("CC-110", "Digital Logic Design", 2.0),
        ("CC-110-L", "Digital Logic Design Lab", 1.0),
        ("MS-252", "Linear Algebra", 3.0),
        ("GE-191", "Expository Writing", 3.0),
        ("GE-163", "Islamic Studies", 2.0),
        ("HQ-002", "Quran Translation - II", 0.5)
    ],
    3: [
        ("CC-211", "Object Oriented Programming", 3.0),
        ("CC-211-L", "Object Oriented Programming Lab", 1.0),
        ("CC-215", "Database Systems", 3.0),
        ("CC-215-L", "Database Systems Lab", 1.0),
        ("CC-210", "Computer Organization & Assembly Language", 3.0),
        ("GE-162", "Calculus & Analytical Geometry", 3.0),
        ("GE-192", "Introduction to Management", 2.0),
        ("HQ-003", "Quran Translation - III", 0.5)
    ],
    4: [
        ("CC-213", "Data Structures", 3.0),
        ("CC-213-L", "Data Structures Lab", 1.0),
        ("CC-312", "Information Security", 3.0),
        ("CC-214", "Computer Networks", 3.0),
        ("CC-212", "Software Engineering", 3.0),
        ("DC-220", "Advanced Database Management Systems", 3.0),
        ("HQ-004", "Quran Translation - IV", 0.5)
    ],
    5: [
        ("CC-313", "Analysis of Algorithms", 3.0),
        ("CC-310", "Artificial Intelligence", 3.0),
        ("DC-320", "Theory of Automata and Formal Languages", 3.0),
        ("DC-321", "Human Computer Interaction", 3.0),
        ("DC-322", "Computer Architecture", 3.0),
        ("EC-330", "Web Technologies / Elective", 3.0),
        ("HQ-005", "Quran Translation - V", 0.5)
    ],
    6: [
        ("CC-311", "Operating Systems", 3.0),
        ("EC-333", "Mobile Application Development / Elective", 3.0),
        ("EC-324", "Software Construction & Development / Elective", 3.0),
        ("EC-335", "Machine Learning / Elective", 3.0),
        ("EC-334", "Game Design and Development / Elective", 3.0),
        ("MS-253", "Multivariable Calculus", 3.0),
        ("HQ-006", "Quran Translation - VI", 0.5)
    ],
    7: [
        ("CC-411", "Final Year Project - I", 2.0),
        ("DC-328", "Parallel & Distributed Computing", 3.0),
        ("EC-345", "Computer Vision / Elective", 3.0),
        ("EC-425", "Software Quality Engineering / Elective", 3.0),
        ("MS-254", "Technical and Business Writing", 3.0),
        ("GE-263", "Entrepreneurship", 2.0),
        ("GE-262", "Professional Practices", 2.0),
        ("HQ-007", "Quran Translation - VII", 0.5)
    ],
    8: [
        ("CC-412", "Final Year Project - II", 4.0),
        ("DC-421", "Compiler Construction", 3.0),
        ("UE-272", "Introduction to Marketing", 3.0),
        ("GE-168", "Ideology and Constitution of Pakistan", 2.0),
        ("GE-363", "Civics and Community Engagement", 2.0),
        ("HQ-008", "Quran Translation - VIII", 0.5)
    ]
}

def marks_to_grade_points(marks: int) -> float:
    """Convert numerical marks (0-100) to corresponding grade points based on PUCIT grade bands."""
    if marks < 0 or marks > 100:
        return "Error: marks must be between 0 and 100"
    if marks >= 85:
        return 4.0
    elif marks >= 80:
        return 3.7
    elif marks >= 75:
        return 3.3
    elif marks >= 70:
        return 3.0
    elif marks >= 65:
        return 2.7
    elif marks >= 61:
        return 2.3
    elif marks >= 58:
        return 2.0
    elif marks >= 55:
        return 1.7
    elif marks >= 50:
        return 1.0
    else:
        return 0.0

def calculate_semester_gpa(grade_points: list[float], credit_hours: list[float]) -> float:
    """Calculate the credit-weighted semester GPA given lists of grade points and corresponding credit hours."""
    if len(grade_points) != len(credit_hours):
        return "Error: lists must have the same length"
    
    total_quality_points = sum(gp * ch for gp, ch in zip(grade_points, credit_hours))
    total_credits = sum(credit_hours)
    
    if total_credits == 0:
        return 0.0
        
    return round(total_quality_points / total_credits, 2)

def calculate_new_cgpa(current_cgpa: float, completed_credit_hours: float, semester_gpa: float, semester_credit_hours: float) -> float:
    """Project and calculate the new CGPA after completing a new semester with a specific semester GPA."""
    old_points = current_cgpa * completed_credit_hours
    new_points = semester_gpa * semester_credit_hours
    total_hours = completed_credit_hours + semester_credit_hours
    
    if total_hours == 0:
        return 0.0
        
    return round((old_points + new_points) / total_hours, 2)

def required_gpa_for_target(target_cgpa: float, current_cgpa: float, completed_credit_hours: float, remaining_credit_hours: float) -> float:
    """Calculate the required GPA needed over remaining credit hours to reach a target CGPA."""
    total_hours = completed_credit_hours + remaining_credit_hours
    total_required_points = target_cgpa * total_hours
    current_points = current_cgpa * completed_credit_hours
    needed_points = total_required_points - current_points
    
    if remaining_credit_hours == 0:
        return 0.0
        
    return round(needed_points / remaining_credit_hours, 2)

def get_semester_courses(semester: int) -> str:
    """Retrieve the list of courses, course codes, titles, and credit hours for a given PUCIT semester number."""
    if semester not in COURSES:
        return "Error: invalid semester number"
        
    result_lines = [f"{code}: {name} ({ch} credit hours)" for code, name, ch in COURSES[semester]]
    return "\n".join(result_lines)

def get_remaining_credit_hours(current_semester: int, last_semester: int = 8) -> float:
    """Calculate total remaining credit hours from the current semester up to the final semester."""
    total_ch = 0.0
    for sem in range(current_semester, last_semester + 1):
        if sem in COURSES:
            for _, _, ch in COURSES[sem]:
                total_ch += ch
    return total_ch

def save_report(filename: str, content: str) -> str:
    """Save the generated academic report summary to a text file and return a confirmation message."""
    if not filename.endswith(".txt"):
        filename += ".txt"
        
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
        return f"Success: Report saved to {filename}"
    except Exception as e:
        return f"Error: {str(e)}"