from pydantic import BaseModel

class AudioStreamModel(BaseModel):
    format: str
    duration: float
    sample_rate: int
    channels: int
    # Add other relevant fields
