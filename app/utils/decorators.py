# app/utils/decorators.py
# This file contains decorators for various functionalities

import functools
import time
from fastapi import HTTPException, status

def async_timing_decorator(func):
    """Decorator to measure and log the execution time of an asynchronous function."""
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = await func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Function {func.__name__} took {end_time - start_time} seconds to complete.")
        return result
    return wrapper

def sync_timing_decorator(func):
    """Decorator to measure and log the execution time of a synchronous function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Function {func.__name__} took {end_time - start_time} seconds to complete.")
        return result
    return wrapper

def api_key_required(api_key: str):
    """Decorator to check for a valid API key."""
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            if "api_key" not in kwargs or kwargs["api_key"] != api_key:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API key")
            return await func(*args, **kwargs)
        return wrapper
    return decorator

# Add other decorators as needed
