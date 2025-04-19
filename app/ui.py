import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from retriever.search import search_collection

st.set_page_config(page_title="Inquirmed", layout="centered")
st.title("🩺 Inquirmed: GenAI Clinical Assistant")

st.markdown("Enter a medical question or symptom description below:")

# Choose data source
source = st.selectbox("Select Data Source", options=["fda", "pubmed"], index=0)

# Query input
user_input = st.text_input("Your Query", placeholder="e.g., What are symptoms of pneumonia?")

# Submit and run search
if st.button("Submit") and user_input:
    st.info("🔍 Searching for relevant information...")

    try:
        results = search_collection(query=user_input, source=source, top_k=5)

        if results:
            st.success(f"🧠 Top {len(results)} results from `{source.upper()}`:")
            for i, res in enumerate(results, 1):
                st.markdown(f"""
                **Result {i}**
                - **Score**: `{res['score']}`
                - **Text**: {res['text']}
                """)
        else:
            st.warning("No relevant results found.")
    except Exception as e:
        st.error(f"Something went wrong: {e}")
