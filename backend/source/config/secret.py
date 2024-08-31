import os

from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(__file__), '../../.env')
load_dotenv(dotenv_path=env_path)

class SecretConfig:
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = 'bcrypt'
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7

    
secret_config = SecretConfig()
