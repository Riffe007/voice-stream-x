# main.py
from fastapi import FastAPI
from app.routers import whisper_api_router, eleven_labs_router

app = FastAPI(title="Voice Streaming Service",
              description="A FastAPI application to integrate ChatGPT Whisper API and Eleven Labs Voice Streaming",
              version="1.0.0")

# Include routers
app.include_router(whisper_api_router.router, prefix="/whisper", tags=["Whisper API"])
app.include_router(eleven_labs_router.router, prefix="/elevenlabs", tags=["Eleven Labs API"])

@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to the Voice Streaming Service"}

# You can add additional routes or configuration as needed.
