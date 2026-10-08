def analyze_timetable(document_text, question):
    """
    Analyze timetable text.

    The LLM will eventually use this function
    to answer questions about the timetable.
    """

    return {
        "question": question,
        "document_text": document_text,
        "message": "Timetable content received successfully."
    }