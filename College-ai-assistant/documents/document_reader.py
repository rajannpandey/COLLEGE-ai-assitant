import os
from documents.pdf_reader import read_pdf
from documents.docx_reader import read_docx
from documents.txt_reader import read_txt
def read_document(file_path):
    extension = os.path.splitext(file_path)[1].lower()
    if extension == ".pdf":
        return read_pdf(file_path)
    elif extension == ".docx":
        return read_docx(file_path)
    elif extension == ".txt":
        return read_txt(file_path)
    else:
        raise ValueError(
            "Unsupported file type. Please use PDF, DOCX, or TXT."
        )
