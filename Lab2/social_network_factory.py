from abc import ABC, abstractmethod
from social_network import SocialNetwork

class SocialNetworkFactory(ABC):
    @abstractmethod
    def create_social_network(self) -> SocialNetwork:
        pass

    def post(self, login: str, password: str, message: str) -> None:
        network = self.create_social_network()
        network.login(login, password)
        network.post_message(message)
