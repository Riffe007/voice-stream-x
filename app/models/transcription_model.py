from pydantic import BaseModel

class TranscriptionModel(BaseModel):
    text: str
    confidence: float = None
    # Additional fields like timestamp or speaker identification
