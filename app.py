import streamlit as st
from search_engine import search

st.set_page_config(page_title="Anisha Search", layout="centered")

st.title("Vector Based Search Engine")
st.markdown("Type a natural language query below to search documents semantically.")

query = st.text_input("Enter your search query")

if query:
    with st.spinner("Searching..."):
        results = search(query)

    st.markdown("---")
    st.subheader("Top Results")
    for result in results:
        st.markdown(f"### 📄 {result['title']}")
        st.markdown(f"{result['summary']}")
        st.caption(f"Document ID: `{result['id']}`")
        st.markdown("---")

st.markdown("<br><hr><center>Made with ❤️ using Streamlit, FAISS & Transformers</center>", unsafe_allow_html=True)
