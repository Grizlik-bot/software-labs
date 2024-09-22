from social_network_factory import SocialNetworkFactory
from linkedin import LinkedIn
from social_network import SocialNetwork

class LinkedInFactory(SocialNetworkFactory):
    def create_social_network(self) -> SocialNetwork:
        return LinkedIn()
