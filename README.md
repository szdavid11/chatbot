# Hitchhiker's Guide to the Galaxy Chatbot

## Introduction

This repository contains a Streamlit-based web application powered by LlamaIndex and OpenAI's GPT-3.5 model, designed to create an interactive chatbot. The chatbot is specialized in answering questions about Douglas Adams' famous book, "Hitchhiker's Guide to the Galaxy."

## Features

- **Interactive Chatbot**: Engage in a conversation with the AI about "Hitchhiker's Guide to the Galaxy."
- **Customized Responses**: The chatbot is programmed with a sense of humor and positivity, enhancing the user experience.
- **Streamlit Interface**: A simple and intuitive web interface for users to interact with the chatbot.

## Requirements

To run this application, you will need:

- Python 3.10 or later
- Streamlit
- LlamaIndex library
- OpenAI's GPT-3.5 API access

## Installation

1. **Clone the Repository**

   ```bash
   git clone [repository URL]
   cd [repository name]
   ```

2. **Set Up a Python Environment** (optional but recommended)

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Set your OpenAI API key**

   You need to set your OpenAI API key as an environment variable.

   For MacOS/Linux:

   ```bash
   export OPENAI_API_KEY=your_api_key_here
   ```

   For Windows:

   ```bash
   set OPENAI_API_KEY=your_api_key_here
   ```

2. **Running the Application**

   Launch the application by running:

   ```bash
   streamlit run streamlit_window.py
   ```

3. **Interact with the Chatbot**

   Once the application is running, navigate to the provided localhost URL in your web browser to interact with the chatbot.

## Customizing the Chatbot

The chatbot's behavior and knowledge base are set by a custom prompt defined in the script. You can modify the `custom_prompt` in `app.py` to change the chatbot's responses or focus on a different topic.
