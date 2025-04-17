import streamlit as st

st.set_page_config(page_title="Inquirmed", layout="centered")
st.title("🩺 Inquirmed: GenAI Clinical Assistant")

st.markdown("Enter a medical question or symptom description below:")

user_input = st.text_input("Your Query", placeholder="e.g., What are symptoms of pneumonia?")

if st.button("Submit") and user_input:
    # Placeholder logic
    st.info("🔍 Processing...")
    st.success(f"🧠 Placeholder response for: **{user_input}**")
