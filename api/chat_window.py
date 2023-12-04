import streamlit as st
from dotenv import load_dotenv
load_dotenv()

from chat.chat_engine import chat_engine


def respond_to_message(question):
    try:
        answer = chat_engine.chat(question)
        return answer.response
    except Exception as e:
        return f'Unexpected error: {e}'


st.title("Hitchhiker's Guide to the Galaxy")

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Create a container for the chat history and use a column layout
chat_container = st.container()
input_container = st.container()

# Display chat history in the container with a scrollbar
with chat_container:
    for message in st.session_state.chat_history:
        st.markdown(message)

# Move to the input container at the bottom for the message input and send button
with input_container:
    user_message = st.text_input("", key="new_message", placeholder="Type your message here")
    send_button = st.button('Send')

    if send_button:
        if user_message:
            st.session_state.chat_history.append("**You**: " + user_message)
            response = respond_to_message(user_message)
            st.session_state.chat_history.append("**AI**: " + response)
            # Reset the message input
            st.experimental_rerun()
