
import streamlit as st
import pandas as pd

# ----------------------------------
# 1. Configure Streamlit page
# ----------------------------------

st.set_page_config(
    page_title="Student Grade Manager",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Student Grade Manager")
st.write("Add students and manage their grades.")

# ----------------------------------
# 2. Grading function - Day 2 logic
# ----------------------------------

def get_grade(mark):

    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


# ----------------------------------
# 3. Initialize session state
# ----------------------------------

if "students" not in st.session_state:
    st.session_state.students = []


# ----------------------------------
# 4. Student input form
# ----------------------------------

st.subheader("Add New Student")

with st.form("add_student_form"):

    name = st.text_input("Student Name")

    mark = st.number_input(
        "Student Mark",
        min_value=0,
        max_value=100,
        value=0,
        step=1
    )

    submitted = st.form_submit_button("Add Student")

    if submitted:

        if not name.strip():
            st.error("Please enter a student name.")

        else:

            student = {
                "Name": name.strip(),
                "Mark": mark,
                "Grade": get_grade(mark)
            }

            st.session_state.students.append(student)

            st.success(f"{name} added successfully!")


# ----------------------------------
# 5. Display student records
# ----------------------------------

st.subheader("Student Results")

if st.session_state.students:

    df = pd.DataFrame(st.session_state.students)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    # ----------------------------------
    # 6. Calculate class statistics
    # ----------------------------------

    marks = [student["Mark"]
             for student in st.session_state.students]

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    st.subheader("Class Statistics")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Class Average",
        f"{average:.2f}"
    )

    col2.metric(
        "Highest Mark",
        highest
    )

    col3.metric(
        "Lowest Mark",
        lowest
    )

else:

    st.info("No students added yet. Please add a student.")
