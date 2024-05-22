import numpy as np
from gpt4all import GPT4AllEmbeddings

def generate_embeddings(text: str) -> np.ndarray:
    """
    Generates embeddings for the given text using GPT4AllEmbeddings.
    
    :param text: The input text to generate embeddings for.
    :return: A numpy array representing the embeddings.
    """
    embeddings = GPT4AllEmbeddings()
    return np.array([embeddings.embed_text(text)])
