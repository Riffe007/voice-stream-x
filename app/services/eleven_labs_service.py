# app/services/eleven_labs_service.py

import requests
from typing import Optional, Dict, Any

class ElevenLabsService:
    def __init__(self, api_key: str, base_url: str = "https://api.elevenlabs.io"):
        self.api_key = api_key
        self.base_url = base_url

    def _send_request(self, endpoint: str, payload: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Send a request to the Eleven Labs API.

        Args:
            endpoint (str): The API endpoint to target.
            payload (Dict[str, Any]): The payload for the POST request.
        
        Returns:
            Optional[Dict[str, Any]]: The response data as a dictionary, or None if request fails.
        """
        headers = {"Content-Type": "application/json", "xi-api-key": self.api_key}
        response = requests.post(f"{self.base_url}/{endpoint}", json=payload, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error in Eleven Labs API request: {response.status_code} - {response.text}")
            return None

    def generate_speech(self, text: str, voice_id: str, model_id: str = "eleven_monolingual_v1") -> Optional[str]:
        """
        Generate speech from text using Eleven Labs API.

        Args:
            text (str): The text to convert to speech.
            voice_id (str): The ID of the voice to use for speech synthesis.
            model_id (str, optional): The model identifier. Defaults to "eleven_monolingual_v1".
        
        Returns:
            Optional[str]: The URL to the generated speech audio, or None if the request fails.
        """
        payload = {
            "model_id": model_id,
            "pronunciation_dictionary_locators": [],
            "text": text,
            "voice_settings": {
                "similarity_boost": 1,
                "stability": 1,
                "style": 1,
                "use_speaker_boost": True
            }
        }
        response = self._send_request(f"v1/text-to-speech/{voice_id}/stream", payload)
        return response.get("audio") if response else None

# Example usage
# eleven_labs_service = ElevenLabsService(api_key="Your-API-Key")
# speech_url = eleven_labs_service.generate_speech("Hello world", "voice_id_here")
# print(speech_url)
