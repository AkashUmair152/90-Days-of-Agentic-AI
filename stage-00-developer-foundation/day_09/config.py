import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_app_name() -> str:
    return os.getenv("APP_NAME", "Default App")

def get_environment() -> str:
    return os.getenv("ENVIRONMENT", "development")

def get_api_key() -> str:
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        raise ValueError("OPENAI_API_KEY is not set in environment variables.")
    return key

def get_model_name() -> str:
    return os.getenv("MODEL_NAME", "gpt-3.5-turbo")