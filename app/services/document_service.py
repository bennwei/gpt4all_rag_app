import numpy as np
import faiss
from app.utils.pdf_extractor import extract_text_from_pdf
from app.utils.embedding_generator import generate_embeddings

class DocumentService:
    def __init__(self):
        self.dimension = 768  # Example dimension, adjust as needed
        self.index = faiss.IndexFlatL2(self.dimension)
        self.documents = []  # List to store documents
    
    def process_and_index_pdf(self, pdf_file_path: str):
        text = extract_text_from_pdf(pdf_file_path)
        embeddings = generate_embeddings(text)
        self.index.add(embeddings)
        self.documents.append(text)  # Store the document text
    
    def get_document_by_index(self, index):
        return self.documents[index]

# Example initialization and usage
# document_service = DocumentService()
# document_service.process_and_index_pdf('path/to/pdf/file.pdf')
# query_service = QueryService(document_service)
# response = query_service.query_documents(QueryRequest(query="What is the main topic?"))


