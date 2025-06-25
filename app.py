import streamlit as st
from Chatbot import run_chatbot

st.set_page_config(page_title="ExAMark", page_icon="🧠", layout="centered")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🧠 ExAMark")

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle new input
if user_input := st.chat_input("Ask me anything about Exabits..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    response = run_chatbot(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.markdown(response)
