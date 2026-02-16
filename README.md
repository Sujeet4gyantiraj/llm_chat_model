# llm_chat_model

## Features
- **REST API** — `POST /ask` to query the LLM with text
- **Web Chat UI** — `GET /chat` loads a lightweight front-end that calls `/ask`
- **Live Voice Streaming** — `GET /voice` opens a browser-based voice chat UI
  - Press-and-hold the mic button to speak
  - Audio is streamed over WebSocket, transcribed server-side, sent to the LLM, and the reply is spoken back via TTS

## Requirements
```
pip install fastapi uvicorn requests edge-tts SpeechRecognition pydub websockets
sudo apt install ffmpeg   # needed by pydub for audio conversion
```

## Run
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

- **Text API**: `POST http://localhost:8000/ask`
- **Web Chat**: open `http://localhost:8000/chat`
- **Voice UI**: open `http://localhost:8000/voice` in a browser (Chrome recommended for mic access)