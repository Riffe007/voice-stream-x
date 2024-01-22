# app/services/whisper_service.py

import requests
from typing import Optional, Dict, Any

class WhisperService:
    def __init__(self, api_key: str, base_url: str = "https://api.openai.com"):
        self.api_key = api_key
        self.base_url = base_url

    def _send_request(self, endpoint: str, payload: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Send a request to the Whisper API.

        Args:
            endpoint (str): The API endpoint to target.
            payload (Dict[str, Any]): The payload for the POST request.
        
        Returns:
            Optional[Dict[str, Any]]: The response data as a dictionary, or None if request fails.
        """
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.post(f"{self.base_url}/{endpoint}", json=payload, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error in Whisper API request: {response.status_code} - {response.text}")
            return None

    def transcribe_audio(self, audio_url: str) -> Optional[str]:
        """
        Transcribe audio using Whisper API.

        Args:
            audio_url (str): The URL of the audio file to transcribe.
        
        Returns:
            Optional[str]: The transcribed text, or None if the request fails.
        """
        payload = {
            "audio_url": audio_url
        }
        response = self._send_request("v1/whisper", payload)
        return response.get("text") if response else None

# Example usage
# whisper_service = WhisperService(api_key="Your-API-Key")
# transcription = whisper_service.transcribe_audio("audio_url_here")
# print(transcription)
