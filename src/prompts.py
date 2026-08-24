from langchain_core.prompts import PromptTemplate

mcq_prompt = PromptTemplate(
    input_variables=["content", "num_questions", "difficulty", "tone", "mcq_type"],
    template="""
    Generate {num_questions} multiple choice questions about {content}.
    Difficulty level: {difficulty} and also with the tone of {tone} and this {mcq_type} type of mcqs.

    Return ONLY valid JSON, no extra text, in this exact format:
    [
      {{
        "question": "...",
        "options": {{"A": "...", "B": "...", "C": "...", "D": "..."}},
        "correct_answer": "A"
      }}
    ]
    """
)