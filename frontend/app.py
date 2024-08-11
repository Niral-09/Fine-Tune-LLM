import streamlit as st
import requests

API_URL = "http://localhost:8001"

st.title("Question Answering with Pre-trained Model")

st.header("Ask a Question")
context = st.text_area("Context", height=200)
question = st.text_input("Question")

if st.button("Get Answer"):
    if context and question:
        response = requests.post(f"{API_URL}/qa/", json={"question": question})
        if response.status_code == 200:
            answer = response.json()
            st.write(f"**Answer**: {answer['answer']}")
            st.write(f"**Confidence**: {answer['score']:.2f}")
        else:
            st.error(f"Error: {response.json().get('detail', 'Unknown error')}")
    else:
        st.error("Please provide both context and question.")

st.header("Configure Model")
model_name = st.text_input("Model Name (e.g., distilbert-base-uncased-distilled-squad)")

if st.button("Load Model"):
    if model_name:
        response = requests.post(f"{API_URL}/config/", json={"model_name": model_name})
        if response.status_code == 200:
            st.success(response.json()['message'])
        else:
            st.error(f"Error: {response.json().get('detail', 'Unknown error')}")
    else:
        st.error("Please provide a model name.")
