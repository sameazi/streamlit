import streamlit as st

# Data for institution scales and course types
institution_scale = {
    "Acadia University": 7,
    "Memorial University": 6,
    "Simon Fraser University": 7,
    "University of Alberta": 7,
    "University of Moncton": 7,
    "St. Francis Xavier University": 3,
    "Algoma University": 3,
    "Université de Montréal": 7,
    "Saint Mary's University": 7,
    "Athabasca University": 7,
    "Mount Allison University": 7,
    "University of St. Thomas": 7,
    "Bishop's University": 3,
    "Mount Royal University": 7,
    "Université Sainte-Anne": 7,
    "Brandon University": 7,
    "Mount Saint Vincent University": 7,
    "Thompson Rivers University": 7,
    "Brock University": 3,
    "University of New Brunswick": 7,
    "Toronto School of Theology": 7,
    "University of Calgary": 7,
    "Nipissing University": 3,
    "University of Toronto": [3, 7],
    "Cape Breton University": 3,
    "Ontario College of Art & Design University": 3,
    "Trent University": 3,
    "Carleton University": 7,
    "Ontario Tech University": 7,
    "Trinity Western University": 7,
    "Concordia University": 7,
    "University of Ottawa": 7,
    "University of British Columbia": 7,
    "Dalhousie University": [3, 7],
    "University of Prince Edward Island": 3,
    "University of Northern British Columbia": 7,
    "University of Guelph": 3,
    "Université du Québec": 7,
    "University of Victoria": [3, 7],
    "Lakehead University": 3,
    "Queen's University": [3, 7],
    "University of Waterloo": [3, 7],
    "Laurentian University": 7,
    "Quest University Canada": 8,
    "University of Western Ontario": 3,
    "Université Laval": 7,
    "University of Regina": 3,
    "Wilfrid Laurier University": 7,
    "University of Lethbridge": 7,
    "Royal Military College of Canada": [4, 7],
    "University of Windsor": [3, 7],
    "University of Manitoba": 9,
    "Royal Roads University": 7,
    "University of Winnipeg": 7,
    "McGill University": 8,
    "University of Saskatchewan": 3,
    "York University": 9,
    "McMaster University": 7,
    "Université de Sherbrooke": 7
}

course_types = {"Half Year": 1, "Full Year": 2, "Three Quarters": 1.5, "Lab": 0.5}

# Function to convert grade to GPA
def gradeconv(x, y, z):
    x = x.strip()
    scale = institution_scale[y]
    try:
        if scale in [9, 8, 7] and x.strip().upper() in ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E", "F"]:
            if scale == 9:
                grade_to_gpa = {"A+": 4.00, "A": 3.80, "B+": 3.30, "B": 3.00, "C+": 2.30, "C": 2.00, "D+": 1.30, "D": 1.00, "E": 0.00, "F": 0.00}
                gpa = grade_to_gpa.get(x, None)
            elif scale == 8:
                grade_to_gpa = {"A": 4.00, "A-": 3.70, "B+": 3.30, "B": 3.00, "B-": 2.70, "C+": 2.30, "C": 2.00, "C-": 1.70, "D+": 1.30, "D": 1.00, "D-": 0.70, "E": 0.00, "F": 0.00}
                gpa = grade_to_gpa.get(x, None)
            elif scale == 7:
                grade_to_gpa = {"A+": 4.00, "A": 3.90, "A-": 3.70, "B+": 3.30, "B": 3.00, "B-": 2.70, "C+": 2.30, "C": 2.00, "C-": 1.70, "D+": 1.30, "D": 1.00, "D-": 0.70, "E": 0.00, "F": 0.00}
                gpa = grade_to_gpa.get(x, None)
            else:
                st.error("Scale not supported for letter grades")
                return "wrong"
        elif scale in [6, 4, 3]:
            if 0 < float(x) <= 100:
                x = float(x)
                if scale == 6:
                    if x > 100:
                        gpa = None
                    elif x >= 94:
                        gpa = 4.00
                    elif x >= 85:
                        gpa = 3.90
                    elif x >= 80:
                        gpa = 3.70
                    elif x >= 75:
                        gpa = 3.30
                    elif x >= 70:
                        gpa = 3.00
                    elif x >= 65:
                        gpa = 2.70
                    elif x >= 60:
                        gpa = 2.30
                    elif x >= 55:
                        gpa = 2.00
                    elif x >= 50:
                        gpa = 1.00
                    else:
                        gpa = 0.00
                elif scale == 4:
                    if x > 100:
                        gpa = None
                    elif x >= 93:
                        gpa = 4.00
                    elif x >= 84:
                        gpa = 3.90
                    elif x >= 75:
                        gpa = 3.70
                    elif x >= 72:
                        gpa = 3.30
                    elif x >= 69:
                        gpa = 3.00
                    elif x >= 66:
                        gpa = 2.70
                    elif x >= 64:
                        gpa = 2.30
                    elif x >= 62:
                        gpa = 2.00
                    elif x >= 60:
                        gpa = 1.70
                    elif x >= 56:
                        gpa = 1.30
                    elif x >= 53:
                        gpa = 1.00
                    elif x >= 50:
                        gpa = 0.70
                    else:
                        gpa = 0.00
                elif scale == 3:
                    if x > 100:
                        gpa = None
                    elif x >= 90:
                        gpa = 4.00
                    elif x >= 85:
                        gpa = 3.90
                    elif x >= 80:
                        gpa = 3.70
                    elif x >= 77:
                        gpa = 3.30
                    elif x >= 73:
                        gpa = 3.00
                    elif x >= 70:
                        gpa = 2.70
                    elif x >= 67:
                        gpa = 2.30
                    elif x >= 63:
                        gpa = 2.00
                    elif x >= 60:
                        gpa = 1.70
                    elif x >= 57:
                        gpa = 1.30
                    elif x >= 53:
                        gpa = 1.00
                    elif x >= 50:
                        gpa = 0.70
                    else:
                        gpa = 0.00
                else:
                    st.error("Scale not supported for numeric grades")
                    return "wrong"
        return gpa, course_types[z]
    except (ValueError, UnboundLocalError):
        return "wrong"

# Streamlit app
st.title("OMSAS GPA Calculator")

with st.sidebar:
    st.header("Navigation")
    if st.button("OMSAS GPA Calculator"):
        st.experimental_rerun()


form = st.form(key="Form1")
c1, c2 = st.columns(2)
coursenameagr = st.toggle("Course name?")
with c1:
    inst = st.selectbox("What institution do you attend?", sorted(institution_scale.keys()))
with c2:
    course_cnt = st.number_input("How many courses would you like to calculate for?", min_value=1, step=1)

courses = []
for i in range(course_cnt):
    if coursenameagr:
        o = st.text_input(f"Enter your Course Title:", key=f"course_title_{i}")
        st.write(f'<span style="font-size: 16px;">{f"<b>Course: {o}</b>"}</span>', unsafe_allow_html=True)
        grade = st.text_input(f"What is your grade for {o}?", key=f"grade_{i}")
        type = st.selectbox(f"What is your Course Type for {o}?", list(course_types.keys()), key=f"type_{i}")
    else:
        st.write(f'<span style="font-size: 16px;">{f"<b>Course {i+1}</b>"}</span>', unsafe_allow_html=True)
        grade = st.text_input(f"What is your grade for Course {i+1}?", key=f"grade_{i}")
        type = st.selectbox(f"What is your course type for Course {i+1}?", list(course_types.keys()), key=f"type_{i}")
    courses.append((grade, type))

if st.button("Calculate"):
    lst = {}
    for grade, type in courses:
        result = gradeconv(grade, inst, type)
        if result == "wrong":
            st.error("Please enter a valid grade and or course type.")
        else:
            gpa, weight = result
            lst[gpa] = weight
    if lst:
        x = sum(float(gpa) * float(weight) for gpa, weight in lst.items())
        y = sum(float(weight) for weight in lst.values())
        cGPA = x / y
        st.write(f'<span style="font-size: 20px;">{f"cGPA = <b>{cGPA:.2f}</b>"}</span>', unsafe_allow_html=True)
