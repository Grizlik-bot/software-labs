from social_network_factory import SocialNetworkFactory
from facebook import Facebook
from social_network import SocialNetwork

class FacebookFactory(SocialNetworkFactory):
    def create_social_network(self) -> SocialNetwork:
        return Facebook()
