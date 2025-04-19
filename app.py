# app.py

import streamlit as st
from rag_pipeline import build_qa_pipeline, query_pipeline
import os

st.set_page_config(page_title="AI Research Assistant", layout="wide")

st.title("🤖 AI Research Assistant")
st.markdown("Upload a `.txt` research file and ask questions based on its content.")

# State to hold the pipeline
if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = None

# Upload section
uploaded_file = st.file_uploader("📄 Upload your `.txt` research file", type=["txt"])

# File processing
if uploaded_file:
    try:
        # Save uploaded file to disk
        file_path = f"uploaded_{uploaded_file.name}"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())

        st.success("✅ File uploaded successfully.")
        st.write("🧠 Building pipeline, please wait...")

        # Build pipeline
        qa_chain = build_qa_pipeline(file_path)
        st.session_state.qa_chain = qa_chain
        st.success("🚀 RAG pipeline ready!")
    except Exception as e:
        st.error(f"❌ Error loading pipeline: {e}")
        st.stop()

# Ask a question
if st.session_state.qa_chain:
    query = st.text_input("🔍 Ask a question related to the uploaded content:")
    if query and st.button("Get Answer"):
        with st.spinner("Thinking..."):
            try:
                answer = query_pipeline(st.session_state.qa_chain, query)
                st.markdown("### 💬 Answer")
                st.write(answer)
            except Exception as e:
                st.error(f"❌ Failed to get response: {e}")
else:
    st.info("Please upload a `.txt` research file to begin.")
