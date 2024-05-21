import gradio as gr
import requests

def upload_pdf(file):
    response = requests.post("http://localhost:8000/upload_pdf", files={"file": file})
    return response.json()["status"]

def query_rag_system(query):
    response = requests.post("http://localhost:8000/query", json={"query": query})
    return response.json()["response"]

with gr.Blocks() as demo:
    with gr.Tab("Upload PDF"):
        upload = gr.File(label="Upload your PDF")
        upload_output = gr.Textbox()
        upload_button = gr.Button("Upload")
        upload_button.click(upload_pdf, inputs=upload, outputs=upload_output)
    
    with gr.Tab("Query System"):
        query_input = gr.Textbox(label="Enter your query")
        query_output = gr.Textbox()
        query_button = gr.Button("Query")
        query_button.click(query_rag_system, inputs=query_input, outputs=query_output)

if __name__ == "__main__":
    demo.launch()

