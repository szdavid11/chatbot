import streamlit as st
from dotenv import load_dotenv
load_dotenv()

from llama_index import (
    StorageContext,
    load_index_from_storage,
)

# load the existing index
storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context)

custom_prompt = "You are a helpful assistant with super humor and try to make me feel better. " \
                "You can answer everything about the book Hitchhiker's Guide to the Galaxy." \
                "Which is without doubt the best book ever!"

# Initialize the chat engine
chat_engine = index.as_chat_engine(chat_mode="openai", system_prompt=custom_prompt, verbose=True)


def respond_to_message(question):
    try:
        answer = chat_engine.chat(question)
        return answer.response
    except Exception as e:
        return f'Unexpected error: {e}'


def send_message():
    user_message = st.session_state.new_message
    if user_message:
        st.session_state.chat_history.append("**You**: " + user_message)
        response = respond_to_message(user_message)
        st.session_state.chat_history.append("**AI**: " + response)
        st.session_state.new_message = ""


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
    user_message = st.text_input("", key="new_message", on_change=None)
    send_button = st.button('Send', on_click=send_message)