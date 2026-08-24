# Local LLM Token Consumer 

A modular Python application designed to interact with a local Large Language Model (Gemma 2B) via streaming, calculating real-time token consumption and generation speed (TPS).

## Features
* **Real-time Streaming**: Words appear in the terminal as they are generated.
* **Context Memory**: The chat remembers previous messages in the conversation.
* **Metrics**: Calculates Prompt Tokens, Completion Tokens, and Tokens per Second (TPS).
* **Modular Architecture**: Clean separation between API logic and User Interface.

## Prerequisites
1. [Python 3.x](https://www.python.org/downloads/)
2. [Ollama](https://ollama.com/) installed on your machine.

## How to Run

**1. Start the local server and download the model:**
Open a terminal and run:

    ollama serve
    ollama pull gemma:2b

**2. Install the dependencies:**
Open a second terminal in this project's folder and run:

    pip install -r requirements.txt

**3. Start the chat:**

    python main.py
