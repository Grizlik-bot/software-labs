from abc import ABC, abstractmethod

class SocialNetwork(ABC):
    @abstractmethod
    def login(self, username_or_email: str, password: str) -> None:
        pass

    @abstractmethod
    def post_message(self, message: str) -> None:
        pass