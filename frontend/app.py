import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.title("Question Answering with Pre-trained Model")

st.header("Ask a Question")
question = st.text_input("Question")

if st.button("Get Answer"):
    if question:
        print(f"{API_URL}/qa/")
        response = requests.post(f"{API_URL}/qa/", json={"command": question})
        if response.status_code == 200:
            answer = response.json()
            st.write(f"**review**: {answer['review']}")
            st.write(f"**sentiment**: {answer['sentiment']}")
            st.write(f"**probs**: {answer['probs']}")
        else:
            st.error(f"Error: {response.json().get('detail', 'Unknown error')}")
    else:
        st.error("Please provide both context and question.")
