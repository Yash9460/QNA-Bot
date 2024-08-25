import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
import os
import pickle
from pathlib import Path
import streamlit_authenticator as stauth

os.environ['GOOGLE_API_KEY'] = "Your-Api-Key"

llm = ChatGoogleGenerativeAI(model="gemini-pro")

st.title("Gemini Q&A Chatbot")
names = ["Yash Bansal", "Alex Clan"]
usernames = ["ybansal", "aclan"]

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "qna_dashboards", "abcdef", cookie_expiry_days=30)
name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/Password is incorrect")

if authentication_status == None:
    st.warning("Please enter your details")

if authentication_status:
    authenticator.logout("Logout", "sidebar")

    st.sidebar.title(f"Welcome {name}")
    st.sidebar.title("Instructions")
    st.sidebar.write(
        """
        Enter your question in the text box below and hit "Submit".
        The chatbot will provide an answer using the Gemini model.
        """
    )
    
    query = st.text_input("Enter your query:")
    
    if st.button("Submit"):
        if query:
            with st.spinner("Thinking..."):
                result = llm.invoke(query)
                st.write("### Answer:")
                st.write(result.content)
        else:
            st.write("Please enter a query to get a response.")
