import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.title("BERT Fine Tuned Model on IMBD dataset")

st.header("try with reviews")
question = st.text_input("Review")

if st.button("Get Answer"):
    if question:
        print(f"{API_URL}/qa/")
        response = requests.post(f"{API_URL}/qa/", json={"command": question})
        if response.status_code == 200:
            answer = response.json()
            st.write(f"**Review**: {answer['review']}")
            st.write(f"**Sentiment**: {answer['sentiment']}")
            st.write(f"**Probs**: {answer['probs']}")
        else:
            st.error(f"Error: {response.json().get('detail', 'Unknown error')}")
    else:
        st.error("Please provide both context and question.")
