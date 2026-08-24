import PyPDF2

def get_content(input_type, source):
    if input_type == "topic":
        return source
    elif input_type == "text":
        return source   
    elif input_type == "file":
        if source.endswith(".txt"):
            with open(source,"r") as f:
                return f.read()
        elif source.endswith(".pdf"):
            text = ""
            reader = PyPDF2.PdfReader(source)
            for page in reader.pages:
                text += page.extract_text() 
            return text
        else:
            raise ValueError("Unsupported file type. Please provide a .txt or .pdf file.")
