# MCQ Generator 🧠

An AI-powered web app that generates multiple choice questions (MCQs) from a **topic**, **pasted text**, or an **uploaded PDF/TXT file** — built with **LangChain**, **Google Gemini**, and **Streamlit**.

🔗 **Live demo:** [Add your Streamlit Cloud URL here]

---

## Features

- **Three input modes**
  - Type a topic (e.g. `"Newton's laws of motion"`)
  - Paste a paragraph of text
  - Upload a `.pdf` or `.txt` file
- **Customizable generation**
  - Number of questions
  - Difficulty level (easy / medium / hard)
  - Tone (formal / informal / humorous)
  - MCQ type (conceptual / factual / application-based / tricky)
- **Clean, structured output** — each question with 4 options and a collapsible "show answer" section
- **Robust error handling** — friendly warnings for missing input, graceful failure if generation fails
- **Powered by Google Gemini** (`gemini-2.5-flash`) via LangChain's LCEL pipeline

---

## Tech Stack

| Layer | Tool |
|---|---|
| LLM | Google Gemini (`gemini-2.5-flash`) |
| Orchestration | LangChain (LCEL) |
| UI | Streamlit |
| PDF parsing | PyPDF2 |
| Env management | python-dotenv, conda |

---

## Project Structure

```
mcq_gen/
├── src/
│   ├── __init__.py
│   ├── llm.py             # Gemini LLM setup
│   ├── prompts.py         # MCQ prompt template
│   ├── content_loader.py  # Handles topic / text / file input
│   └── generator.py       # Core pipeline: content → prompt → LLM → parsed MCQs
├── experiment/
│   └── mcq.ipynb          # Prototyping notebook
├── app.py                 # Streamlit web app
├── requirements.txt
├── setup.py
└── .env                   # Local API key (not committed)
```

---

## How It Works

1. **Input** — user provides a topic, pasted text, or uploads a file (`get_content()` normalizes all three into plain text)
2. **Prompt** — a `PromptTemplate` builds a structured request for Gemini, specifying question count, difficulty, tone, and MCQ type
3. **Generation** — the prompt is piped into the Gemini LLM via LangChain (`prompt | llm`)
4. **Parsing** — Gemini's JSON response is cleaned and parsed into Python objects
5. **Display** — Streamlit renders each question with options and a hidden answer

---

## Running Locally

**1. Clone the repo**
```bash
git clone https://github.com/vandita731/mcq_gen.git
cd mcq_gen
```

**2. Create and activate a virtual environment**
```bash
conda create -p env python=3.11
conda activate ./env
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Add your Gemini API key**

Create a `.env` file in the project root:
```
GOOGLE_API_KEY=your_api_key_here
```
Get a free key from [Google AI Studio](https://aistudio.google.com/app/apikey).

**5. Run the app**
```bash
streamlit run app.py
```

---

## Deployment

Deployed on [Streamlit Community Cloud](https://share.streamlit.io). The `GOOGLE_API_KEY` is stored securely via Streamlit's **Secrets** manager and is never committed to the repository.

---

## Author

**Vandita** — [GitHub](https://github.com/vandita731)