import os.path
from llama_index import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)

if __name__ == "__main__":
    # check if storage already exists
    if not os.path.exists("./storage"):
        # load the documents and create the index
        documents = SimpleDirectoryReader("data").load_data()
        index = VectorStoreIndex.from_documents(documents)
        # store it for later
        index.storage_context.persist()
    else:
        # load the existing index
        storage_context = StorageContext.from_defaults(persist_dir="./storage")
        index = load_index_from_storage(storage_context)

    custom_prompt = (
        "You are a helpful assistant with super humor and try to make me feel better. "
        "You can answer everything about the book Hitchhiker's Guide to the Galaxy."
        "Which is without doubt the best book ever!"
    )

    # Initialize the chat engine
    chat_engine = index.as_chat_engine(
        chat_mode="openai", system_prompt=custom_prompt, verbose=True
    )

    while True:
        question = input("You: ")
        response = chat_engine.chat(question)
        print(response)
