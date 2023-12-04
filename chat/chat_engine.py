from llama_index import (
    StorageContext,
    load_index_from_storage,
)

# load the existing index
storage_context = StorageContext.from_defaults(persist_dir="chat/storage")
index = load_index_from_storage(storage_context)

custom_prompt = "You are a helpful assistant with super humor and try to make me feel better. " \
                "You can answer everything about the book Hitchhiker's Guide to the Galaxy." \
                "Which is without doubt the best book ever!"

# Initialize the chat engine
chat_engine = index.as_chat_engine(chat_mode="openai", system_prompt=custom_prompt, verbose=False)
