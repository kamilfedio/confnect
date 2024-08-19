from dotenv import load_dotenv
import os


env_path = os.path.join(os.path.dirname(__file__), '../../.env')
load_dotenv(env_path)

class GoogleAuthorizationConfig:
    GOOGLE_URI = os.getenv("GOOGLE_URI")
    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")

    @property
    def google_uri(self) -> str:
        return f"{self.GOOGLE_URI}"
    
    @property
    def google_client_id(self) -> str:
        return f"{self.GOOGLE_CLIENT_ID}"
    
    @property
    def google_client_secret(self) -> str:
        return f"{self.GOOGLE_CLIENT_SECRET}"

google_auth_config = GoogleAuthorizationConfig()