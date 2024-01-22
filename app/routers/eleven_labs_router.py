# app/routers/eleven_labs_router.py

from fastapi import APIRouter, HTTPException, Depends
from ..services.eleven_labs_service import ElevenLabsService

router = APIRouter()

@router.get("/elevenlabs/{text}")
async def stream_eleven_labs_audio(text: str, service: ElevenLabsService = Depends()):
    try:
        audio_stream = await service.stream_audio(text)
        return {"message": "Audio streaming started", "audio_stream": audio_stream}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
