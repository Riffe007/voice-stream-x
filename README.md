# VoiceStreamX

## Overview

VoiceStreamX is a sophisticated FastAPI-based application designed for high-performance voice streaming. Utilizing advanced technologies like Eleven Labs and ChatGPT's Whisper API, VoiceStreamX stands at the forefront of voice processing and streaming services. This application serves as a modular component in a larger suite of applications, offering seamless integration and adaptability.

## Features

Eleven Labs Text-to-Speech Integration: Utilizes Eleven Labs API for high-quality, real-time text-to-speech conversion.
ChatGPT's Whisper API for Speech-to-Text: Implements Whisper API for efficient and accurate speech-to-text processing.
FastAPI Framework: Built on the FastAPI framework, ensuring high performance and easy scalability.
Asynchronous Processing: Handles voice streaming and processing asynchronously for optimal performance.
Modular Design: Structured to fit seamlessly within a microservices architecture.

## Getting Started

## Prerequisites

Python 3.8 or higher
FastAPI
Uvicorn (for running the application)
Requests (for API calls)
Websockets (for real-time communication)


## Installation

Clone the repository:


git clone https://github.com/your-github/voice-stream-fastapi.git

Navigate to the project directory:


cd voice-stream-fastapi

Install the required dependencies:


pip install -r requirements.txt

## Usage
Start the FastAPI server:


uvicorn main:app --reload
The application will be available at http://127.0.0.1:8000.

Utilize the provided endpoints for text-to-speech and speech-to-text functionalities.

## API Reference

POST /tts: Endpoint for text-to-speech conversion.
POST /stt: Endpoint for speech-to-text conversion.
Configuration
Configure the API keys and other settings in the config.py file.

## Contributing

Contributions to improve the application are welcome. Please adhere to the coding standards and provide documentation for any new features or fixes.

## License

This project is licensed under the MIT License - see the LICENSE file for more details.

## Acknowledgements

Eleven Labs API
ChatGPT's Whisper API
FastAPI Framework
