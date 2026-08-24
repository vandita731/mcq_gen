import streamlit as st
from src.generator import generate_mcqs

st.title("MCQS Generator")

input_type = st.radio("How do you want to provide content?", ["topic", "text", "file"])
source = None
if input_type == "topic":
    source = st.text_input("Enter a topic: ")
elif input_type == "text":
    source = st.text_area("enter your text here")
else:
    uploaded_file = st.file_uploader("Upload a file", type=["txt", "pdf"])
    if uploaded_file is not None:
        with open(uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getbuffer())
        source = uploaded_file.name

num_questions = st.number_input("Number of questions:", min_value=3, max_value=50)
difficulty = st.selectbox("Select difficulty level:", ["easy", "medium", "hard"])
tone = st.selectbox("Select tone:", ["formal", "informal", "humorous"])
mcq_type = st.selectbox("Select MCQ type:", ["conceptual", "factual", "application-based", "tricky"])


if st.button("Generate MCQs"):
    if not source:
        st.warning("Please provide a topic, text, or upload a file.")
    else:
        with st.spinner("Generating your MCQs..."):
            try:
                mcqs = generate_mcqs(input_type, source, num_questions, difficulty, tone, mcq_type)
                st.success("MCQs generated successfully!")
                for i, mcq in enumerate(mcqs, start=1):
                    st.subheader(f"Q{i}: {mcq['question']}")
                    for key, value in mcq['options'].items():
                        st.write(f"{key}. {value}")
                    with st.expander("Show answer"):
                        st.write(mcq['correct_answer'])
                    st.write("---")
            except Exception as e:
                st.error("Something went wrong while generating MCQs. Please try again.")