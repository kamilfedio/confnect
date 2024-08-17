from dotenv import load_dotenv
import os


env_path = os.path.join(os.path.dirname(__file__), '../../.env')
load_dotenv(env_path)

class Config:
    title: str = 'convnect'
    description: str ='...'
    version: str ='0.0.1'
    debug: bool = True

class ConfigMiddleware:
    allow_origins: list[str] = ['*']
    allow_credentials: bool = True
    allow_methods: list[str] = ["*"]
    allow_headers: list[str] = ["*"]