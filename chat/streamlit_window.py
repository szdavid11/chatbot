import streamlit as st
from llama_index import (
    StorageContext,
    ServiceContext,
    load_index_from_storage,
)
from llama_index.llms import OpenAI

# Specify the OpenAI model you want to use
service_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt-3.5-turbo"))


# load the existing index
storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context)

custom_prompt = "You are a helpful assistant with good sense of humor and positivity. " \
                "You can answer everything about the book Hitchhiker's Guide to the Galaxy." \
                "You know that Hitchhiker's Guide to the Galaxy is without doubt the best book ever!" \
                "Come on it has a towel in it!"

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

st.write("Ask me anything about the book Hitchhiker's Guide to the Galaxy!")

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
    user_message = st.text_input("", key="new_message", on_change=None, placeholder="Type your question here")
    send_button = st.button('Send', on_click=send_message)