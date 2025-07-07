import json
import pickle
import os
import faiss
from sentence_transformers import SentenceTransformer
import numpy as np

# Paths
DATA_PATH = "data/documents.json"
OUTPUT_DIR = "output"
INDEX_PATH = os.path.join(OUTPUT_DIR, "faiss_index.bin")
DOC_STORE_PATH = os.path.join(OUTPUT_DIR, "document_store.pkl")

# Load documents
with open(DATA_PATH, "r", encoding="utf-8") as f:
    documents = json.load(f)

# Extract content
corpus = [doc["content"] for doc in documents]

# Model
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(corpus, show_progress_bar=True)

# FAISS Index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

# Save index
os.makedirs(OUTPUT_DIR, exist_ok=True)
faiss.write_index(index, INDEX_PATH)

# Save doc store
with open(DOC_STORE_PATH, "wb") as f:
    pickle.dump(documents, f)

print("✅ Index and document store saved.")
