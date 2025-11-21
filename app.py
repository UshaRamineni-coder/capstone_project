import streamlit as st

st.title("Government Schemes & Scholarships Agent")

# Simple user input
name = st.text_input("Your name")
age = st.number_input("Your age", min_value=1, step=1)
is_student = st.radio("Are you a student?", ("yes", "no")) == "yes"
category = st.text_input("Category (General/SC/ST/OBC)")
city = st.text_input("City/village")
stream = st.text_input("Stream/course")

common_schemes = [
    {"name": "PM Scholarship Scheme", "eligible": lambda p: p["is_student"] and p["age"] <= 25, "description": "Scholarship for students below 25."},
    {"name": "Rural Upliftment Grant", "eligible": lambda p: p["city"] != "bangalore" and p["age"] >= 18, "description": "Support for rural adults."}
]
scholarships = [
    {"name": "India Merit Scholarship", "eligible": lambda p: p["is_student"] and p["age"] <= 22, "description": "Merit-based for college students."}
]

def get_matching_items(profile, item_list):
    matched = []
    for item in item_list:
        try:
            if item["eligible"](profile):
                matched.append(item)
        except Exception:
            pass
    return matched

if st.button("Get Recommendations"):
    user_profile = {
        "name": name, "age": age, "is_student": is_student,
        "category": category, "city": city, "stream": stream
    }
    matched_schemes = get_matching_items(user_profile, common_schemes)
    matched_scholarships = get_matching_items(user_profile, scholarships)

    st.subheader("Schemes for People and Students")
    for scheme in matched_schemes:
        st.write(f"Scheme: {scheme['name']}")
        st.write(f"Description: {scheme['description']}")
    if not matched_schemes:
        st.write("No matching schemes found.")

    st.subheader("Scholarships for Students")
    for scholarship in matched_scholarships:
        st.write(f"Scholarship: {scholarship['name']}")
        st.write(f"Description: {scholarship['description']}")
    if not matched_scholarships:
        st.write("No matching scholarships found.")

    st.write("Thank you! Your feedback helps us improve.")
