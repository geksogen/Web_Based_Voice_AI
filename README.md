# Real-Time Speech Recognition Server Using Vosk and FastAPI

This project is a server application designed for real-time speech recognition using the Vosk model. The application leverages FastAPI to create WebSockets, enabling the handling of audio streams sent by clients.


```mermaid
sequenceDiagram
    participant Client
    participant Server as FastAPI Server
    participant WS as WebSocket
    participant AP as Audio Processor
    participant VM as Vosk Model

    Client->>Server: Connect to WebSocket
    Server->>WS: Accept WebSocket connection
    Client->>WS: Send audio data (WebM format)
    WS->>AP: Receive audio data
    AP->>AP: Convert WebM to WAV
    AP->>AP: Set audio to mono, 16-bit, 16000 Hz
    AP->>VM: Send processed audio data
    VM->>VM: Perform speech recognition
    VM->>WS: Return recognized text
    WS->>Client: Send recognized text
```

## Key Features:

- **Real-Time Processing:** Handles audio streams in real-time via WebSockets.
- **Speech Recognition:** Utilizes the Vosk model to convert audio into text.
- **Format Support:** Converts audio files from WebM to WAV for processing.
- **Lightweight and Performant:** Uses FastAPI and Uvicorn to ensure high performance and scalability.

## Technologies:

- **FastAPI:** For creating WebSockets and handling HTTP requests.
- **Vosk:** For speech recognition.
- **Pydub:** For processing and converting audio files.
- **Uvicorn:** As the ASGI server to run the application.

