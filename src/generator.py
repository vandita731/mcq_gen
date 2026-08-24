import json

from src.content_loader import get_content
from src.llm import llm
from src.prompts import mcq_prompt


def generate_mcqs(input_type, source, num_questions, difficulty, tone, mcq_type):
    content = get_content(input_type, source)
    chain = mcq_prompt | llm
    chain_response = chain.invoke({
        "content": content,
        "num_questions": num_questions,
        "difficulty": difficulty,
        "tone": tone,
        "mcq_type": mcq_type
    })

    cleaned = chain_response.content.strip()
    cleaned = cleaned.removeprefix("```json").removesuffix("```").strip()
    mcqs = json.loads(cleaned)
    return mcqs