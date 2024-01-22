from pydantic import BaseModel

class VoiceRequestModel(BaseModel):
    text: str
    voice_id: str
    # Additional parameters for voice customization
