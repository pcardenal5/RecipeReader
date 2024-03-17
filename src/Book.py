from PyPDF2 import PdfReader

class Book:
    def __init__(self, path:str) -> None:
        self.path = path


    def read(self):
        text = ''
        pdfFile = PdfReader(self.path)
        for page in pdfFile.pages:
            text += page.extract_text()
        return text