import numpy as np
import faiss
from langchain.embeddings import OpenAIEmbeddings
from gpt4all import GPT4All
from app.models.query_model import QueryRequest, QueryResponse

class QueryService:
    def __init__(self, document_service):
        self.document_service = document_service
        self.embeddings = OpenAIEmbeddings()
        self.model = GPT4All()
    
    def query_documents(self, query_request: QueryRequest) -> QueryResponse:
        query = query_request.query
        query_embedding = self.embeddings.embed_text(query)
        
        # Search for relevant documents using FAISS
        D, I = self.document_service.index.search(np.array([query_embedding]), k=5)  # Get top 5 results
        relevant_docs = [self.document_service.documents[i] for i in I[0]]
        
        # Generate response using GPT4All
        response = self.model.generate(relevant_docs + [query])
        
        return QueryResponse(response=response, relevant_documents=relevant_docs)

# In the main setup, you would initialize the DocumentService and QueryService
# document_service = DocumentService()
# query_service = QueryService(document_service)
