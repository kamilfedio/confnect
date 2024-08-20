from abc import ABC, abstractmethod
import jwt

class Token(ABC):
    
    @abstractmethod
    def create_token(self, payload: dict) -> str:
        pass