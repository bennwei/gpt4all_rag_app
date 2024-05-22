from langchain_community.document_loaders import PyMuPDFLoader


def extract_text_from_pdf(pdf_file_path: str) -> str:
    """
    Extracts text from a PDF file using PyMuPDFLoader.
    
    :param pdf_file_path: The path to the PDF file.
    :return: Extracted text as a single string.
    """
    loader = PyMuPDFLoader(file_path=pdf_file_path)
    documents = loader.load()
    text = "".join([doc.page_content for doc in documents])
    return text



if __name__ == "__main__":
    # test the extract_text_from_pdf function
    pdf_file_path = "/Users/ericliao/Desktop/projects/gpt4all_rag_app/app/data/2019_Mortality_Report_FINAL_052022.pdf"
    print(extract_text_from_pdf(pdf_file_path))