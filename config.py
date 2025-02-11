import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-123')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    GPT_MODEL = 'gpt-4-turbo-preview'