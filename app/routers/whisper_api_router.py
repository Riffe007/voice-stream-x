# app/routers/whisper_api_router.py

from fastapi import APIRouter, HTTPException, Depends
from ..services.whisper_service import WhisperService

router = APIRouter()

@router.get("/whisper/{text}")
async def get_whisper_transcription(text: str, service: WhisperService = Depends()):
    try:
        transcription = await service.get_transcription(text)
        return {"message": "Transcription successful", "transcription": transcription}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
