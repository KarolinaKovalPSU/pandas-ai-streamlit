from dotenv import load_dotenv
import os
import streamlit as st
import pandas as pd
from pandasai.llm.openai import OpenAI 

# Load environment variables
load_dotenv()
API_KEY = os.environ['OPENAI_API_KEY']

# Initialize the OpenAI model
llm = OpenAI(api_token=API_KEY)

# Function to generate a response based on the prompt
def generate_response(prompt):
    # Replace 'ask' with the correct method from your OpenAI class
    response = llm.chat_completion(prompt)  # Check your class for the correct method
    return response

# Set up Streamlit
st.title("Prompt-driven analysis with PandasAI")
uploaded_file = st.file_uploader("Upload a CSV file for analysis", type=['csv'])

if uploaded_file is not None:
    # Read the uploaded CSV file
    df = pd.read_csv(uploaded_file)
    
    # Display the first few rows of the DataFrame
    st.write("DataFrame loaded:")
    st.write(df.head(3))

    # Check if df is a valid DataFrame
    if isinstance(df, pd.DataFrame):
        prompt = st.text_area("Enter your prompt:")

        if st.button("Generate"):
            if prompt:
                with st.spinner("Generating response..."):
                    # Generate the response using the OpenAI model
                    response = generate_response(prompt)  # Pass only the prompt
                    st.write(response)
            else: 
                st.warning("Please enter a prompt.")
    else:
        st.error("The uploaded file is not a valid DataFrame.")
