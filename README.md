# LLM Chat Model - Llama 3.3:70b Chatbot

An interactive chatbot powered by the Llama 3.3:70b language model using Ollama.

## Features

- Interactive command-line chatbot interface
- Streaming responses for real-time interaction
- Conversation history maintained throughout the session
- Uses the powerful Llama 3.3:70b model (70 billion parameters)

## Prerequisites

1. **Python 3.8 or higher**
2. **Ollama** - Download and install from [ollama.ai](https://ollama.ai)
3. **Llama 3.3:70b model** - Pull the model using Ollama

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Sujeet4gyantiraj/llm_chat_model.git
cd llm_chat_model
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Install Ollama (if not already installed):
   - Visit [ollama.ai](https://ollama.ai) and follow the installation instructions for your operating system

4. Pull the Llama 3.3:70b model:
```bash
ollama pull llama3.3:70b
```

Note: The llama3.3:70b model is quite large (~40GB). Make sure you have sufficient disk space and a good internet connection.

## Usage

Run the chatbot:
```bash
python chatbot.py
```

### Example Interaction

```
Chatbot using llama3.3:70b
Type 'quit', 'exit', or 'bye' to end the conversation
--------------------------------------------------

You: Hello! How are you?