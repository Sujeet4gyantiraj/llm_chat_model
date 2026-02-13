"""
Chatbot implementation using Llama 3.3:70b model via Ollama
"""
import ollama
import sys


def chat_with_llama():
    """
    Interactive chatbot using Llama 3.3:70b model
    """
    model_name = "llama3.3:70b"
    print(f"Chatbot using {model_name}")
    print("Type 'quit', 'exit', or 'bye' to end the conversation")
    print("-" * 50)
    
    # Initialize conversation history
    conversation_history = []
    
    while True:
        # Get user input
        user_input = input("\nYou: ").strip()
        
        # Check for exit commands
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Goodbye! Thanks for chatting.")
            break
        
        # Skip empty inputs
        if not user_input:
            continue
        
        # Add user message to conversation history
        conversation_history.append({
            'role': 'user',
            'content': user_input
        })
        
        try:
            # Get response from Llama model
            print("\nAssistant: ", end="", flush=True)
            
            response_content = ""
            stream = ollama.chat(
                model=model_name,
                messages=conversation_history,
                stream=True
            )
            
            # Stream the response
            for chunk in stream:
                content = chunk['message']['content']
                print(content, end="", flush=True)
                response_content += content
            
            print()  # New line after response
            
            # Add assistant response to conversation history
            conversation_history.append({
                'role': 'assistant',
                'content': response_content
            })
            
        except Exception as e:
            print(f"\nError: {e}")
            print("Make sure Ollama is installed and the llama3.3:70b model is available.")
            print("You can install the model with: ollama pull llama3.3:70b")
            sys.exit(1)


if __name__ == "__main__":
    chat_with_llama()
