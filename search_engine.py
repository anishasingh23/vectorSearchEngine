import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from nltk.corpus import wordnet as wn
import os

# Load model and data
model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index("output/faiss_index.bin")
documents = pickle.load(open("output/document_store.pkl", "rb"))

# Query expansion using WordNet
def expand_query(query):
    words = query.split()
    expanded = set(words)
    for word in words:
        for syn in wn.synsets(word):
            for lemma in syn.lemmas():
                expanded.add(lemma.name().replace("_", " "))
    return " ".join(expanded)

# Search function
def search(query, top_k=5):
    expanded = expand_query(query)
    query_vec = model.encode([expanded])[0]
    distances, indices = index.search(np.array([query_vec]), top_k)
    results = []
    for i in indices[0]:
        if i < len(documents):
            doc = documents[i]
            summary = doc["content"][:150] + "..." if len(doc["content"]) > 150 else doc["content"]
            results.append({
                "title": doc["title"],
                "id": doc["id"],
                "summary": summary
            })
    return results
