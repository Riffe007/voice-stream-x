from pydantic import BaseModel

class WhisperRequestModel(BaseModel):
    audio_file_path: str
    # Other parameters like language or model specifics
