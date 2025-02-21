import streamlit as st
import google.generativeai as genai
import time

api_key = "AIzaSyDWOQrTwjDG0huHdNfm1hMkyLvAOYbhZ98"
st.set_page_config("Metro-AI")
st.header("Hello there!")
st.title("Metro-AI")
prompt = st.chat_input("Enter your prompt...")
if prompt:
    st.subheader("User Prompt:")
    st.write(prompt)
    with st.spinner("Processing... Please wait!"):
        time.sleep(5)

    genai.configure(api_key="AIzaSyBapetxcxggUPFawhsECEOa9Fo0atlSIXA")

    # Model Initialize Karna
    model = genai.GenerativeModel("tunedModels/metroaifinetune-rcd7bc0y61uw")

    # Query Send Karna
    response = model.generate_content(prompt)
    st.subheader("AI response:")
    st.write(response.text)

