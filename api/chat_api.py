from fastapi import FastAPI, HTTPException, Depends, Cookie, Request
from llama_index import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware
origins = [
    "https://szalaidatasolutions.online",  # Allow your hostinger domain
    "http://localhost",  # Allow requests from localhost (for local testing)
    "https://builder.hostinger.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory storage for chat engine instances
chat_engines = {}

custom_prompt = "You are a helpful assistant with super humor and try to make me feel better. " \
                "You can answer everything about the book Hitchhiker's Guide to the Galaxy." \
                "Which is without doubt the best book ever!"


class ChatRequest(BaseModel):
    question: str


def start_session(session_token):
    storage_context = StorageContext.from_defaults(persist_dir="chat/storage")
    index = load_index_from_storage(storage_context)
    # Initialize the chat engine
    chat_engine = index.as_chat_engine(chat_mode="openai", system_prompt=custom_prompt, verbose=False)
    chat_engines[session_token] = chat_engine


def get_chat_engine(session_token: str = Cookie(None)):
    if session_token not in chat_engines:
        start_session(session_token)
    return chat_engines[session_token]


@app.post("/chat_with_ai")
async def chat_with_ai(chat_request: ChatRequest, request: Request):
    print(chat_request)

    # Extract the session token from headers
    session_token = request.headers.get('Session-Token')

    # Obtain the chat engine using the session token
    chat_engine = get_chat_engine(session_token)

    # Get the response from the chat engine
    response = chat_engine.chat(chat_request.question)

    return {"response": response}
