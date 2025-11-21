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

    summary_prompt = (
        f"User profile: {user_profile}\nMatching schemes: {[s['name'] for s in matched_schemes]}\nMatching scholarships: {[s['name'] for s in matched_scholarships]}\n"
        f"Give a friendly summary and advice for what government support this user should apply for."
    )
    gemini_summary = gemini_answer(summary_prompt)
    st.markdown(f"**Gemini-powered summary & advice:**\n{gemini_summary}")

    st.write("Thank you! Your feedback helps us improve.")
