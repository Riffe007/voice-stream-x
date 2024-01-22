# app/dependencies.py
# This file contains common dependencies for the FastAPI application

# Example of a dependency
from fastapi import Header, HTTPException

async def verify_api_key(x_api_key: str = Header(...)):
    # Replace 'your_api_key' with your actual API key or a method to validate the key
    if x_api_key != "your_api_key":
        raise HTTPException(status_code=400, detail="Invalid API Key")
    return x_api_key

# Add other dependencies as needed. For example, database connections, user authentication, etc.
