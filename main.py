from dotenv import load_dotenv
import os
import streamlit as st
import pandas as pd
from pandasai.llm.openai import OpenAI 

load_dotenv()
API_KEY = os.environ['OPENAI_API_KEY']

llm = OpenAI(api_token=API_KEY)

def generate_response(prompt):
    response = llm.chat_completion(prompt) 
    return response

st.title("Prompt-driven analysis with PandasAI")
uploaded_file = st.file_uploader("Upload a CSV file for analysis", type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.write("DataFrame loaded:")
    st.write(df.head(3))

    if isinstance(df, pd.DataFrame):
        prompt = st.text_area("Enter your prompt:")

        if st.button("Generate"):
            if prompt:
                with st.spinner("Generating response..."):
                    response = generate_response(prompt)
                    st.write(response)
            else: 
                st.warning("Please enter a prompt.")
    else:
        st.error("The uploaded file is not a valid DataFrame.")
