#  Vector Sense — A Modern Semantic Search Platform

AnishaSearchEngine is an intelligent, semantic search engine powered by **FAISS**, **Sentence-BERT**, and **Retrieval-Augmented Generation (RAG)**. It enables highly relevant document retrieval through **vector similarity**, **query expansion**, and a **streamlined Streamlit frontend**.

<br>

🎯 **Key Features**
---
-  **FAISS-based Vector Search** for fast and scalable similarity matching  
-  **Sentence-BERT Embeddings** for deep semantic understanding of queries  
-  **Query Expansion** using NLP techniques for enhanced recall  
-  **Retrieval-Augmented Generation (RAG)** support for future answer generation  
-  **Interactive Streamlit UI** for real-time query input and result visualization  
-  Clean, modular Python backend with persistent index & document store

<br>

📽️ **Demo Video**
---
> [🎥 Click here to watch the project demo](#) *(Add your YouTube/GIF/loom link here)*

<br>

🚀 **Getting Started**
---
Follow these steps to set up and run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/anisha-search-engine.git
cd anisha-search-engine
```

### 2. Create and Activate Virtual Environment

```bash
# Create venv
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> ⚠️ Note: Make sure you're using Python 3.10+ and `torch>=2.1.0`

### 4. Build the FAISS Index

```bash
python index_builder.py
```

This will:
- Read documents from `data/documents.json`
- Preprocess and embed the content
- Store the FAISS index in `faiss_index.bin`
- Store metadata in `document_store.pkl`

### 5. Launch the App

```bash
streamlit run app.py
```

> The Streamlit interface will open in your browser at `http://localhost:8501`

<br>

📁 **Project Structure**
---
```
anisha-search-engine/
│
├── data/
│   └── documents.json         # Your text corpus
│
├── faiss_index.bin            # FAISS vector index (auto-generated)
├── document_store.pkl         # Metadata store (auto-generated)
│
├── index_builder.py           # Embedding + Index creation
├── search_engine.py           # Core vector search + query expansion logic
├── app.py                     # Streamlit frontend
├── requirements.txt
└── README.md
```

<br>

🧠 **What's Unique About This Project?**
---
| Feature                      | Traditional Search       | **AnishaSearchEngine**   |
|-----------------------------|--------------------------|---------------------------|
| Exact keyword matching      | ✅                       | ✅                        |
| Semantic similarity         | ❌                       | ✅                        |
| Fast vector retrieval (FAISS) | ❌                    | ✅                        |
| Query expansion (NLP)       | ❌                       | ✅                        |
| RAG integration (Coming!)   | ❌                       | ✅                        |
| Modern UI (Streamlit)       | ❌                       | ✅                        |

<br>

📌 **Next Steps**
---
- [ ] Add support for **RAG-based answer generation** using `transformers`  
- [ ] Connect to larger corpora and real-time crawlers  
- [ ] Add feedback loop to improve result accuracy over time  
- [ ] Dockerize the project for easy deployment

<br>



---
