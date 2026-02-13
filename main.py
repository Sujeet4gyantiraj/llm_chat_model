from typing import Any, Dict, List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI(title="Llama 3.3 70B API")


def build_dynamic_prompt(
    query: Optional[str] = None,
    system_prompt: Optional[str] = None,
    context: Optional[List[str]] = None,
    metadata: Optional[Dict[str, Any]] = None
) -> str:
    """
    Build a dynamic prompt by combining system instructions, context, metadata, and user query.
    """
    prompt_parts = []
    
    # Add system prompt if provided
    if system_prompt:
        prompt_parts.append(f"System Instructions: {system_prompt}")
    else:
        prompt_parts.append("System Instructions: You are a helpful customer support chatbot.")
    
    # Add metadata if provided
    if metadata:
        metadata_str = ", ".join([f"{k}: {v}" for k, v in metadata.items()])
        prompt_parts.append(f"Metadata: {metadata_str}")
    
    # Add context if provided
    if context:
        context_section = "\n".join([f"Knowledgebase Passage {i+1}: {text}" for i, text in enumerate(context)])
        prompt_parts.append(f"Knowledgebase Context:\n{context_section}")
    
    # Add user query
    if query:
        prompt_parts.append(f"User Query: {query}")
    else:
        prompt_parts.append("User Query: How can I assist you today?")
    
    return "\n\n".join(prompt_parts)


# Request schema
class PromptRequest(BaseModel):
    # Text of the user query / prompt
    prompt: Optional[str] = None
    query: Optional[str] = None

    # Generation parameters
    temperature: Optional[float] = None
    top_k: Optional[int] = None
    top_p: Optional[float] = None

    # Advanced context and control
    context: Optional[List[str]] = None  # Now expects a list of knowledgebase text passages
    metadata: Optional[Dict[str, Any]] = None
    system_prompt: Optional[str] = None

@app.post("/ask")
async def ask_llama(request: PromptRequest):
    try:
        # Get the user query (support both "query" and "prompt" fields)
        user_query = request.query or request.prompt
        
        # Build dynamic prompt from all components
        prompt_text = build_dynamic_prompt(
            query=user_query,
            system_prompt=request.system_prompt,
            context=request.context,
            metadata=request.metadata
        )

        # Build options block only with values that were provided
        options: Dict[str, Any] = {}
        if request.temperature is not None:
            options["temperature"] = request.temperature
        if request.top_k is not None:
            options["top_k"] = request.top_k
        if request.top_p is not None:
            options["top_p"] = request.top_p

        payload: Dict[str, Any] = {
            "model": "qwen3-coder:480b-cloud",
            "prompt": prompt_text,
            "stream": False,
        }

        if options:
            payload["options"] = options

        # Forward request to Ollama's local API (default: port 11434)
        response = requests.post(
            "http://localhost:11434/api/generate",
            json=payload,
        )
        response.raise_for_status()
        result = response.json()
        
        return {"response": result.get("response", "")}
        
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Ollama Connection Error: {str(e)}")

# Root health check
@app.get("/")
async def root():
    return {"status": "Llama 3.3 API is running"}
