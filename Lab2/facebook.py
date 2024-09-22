from social_network import SocialNetwork

class Facebook(SocialNetwork):
    def __init__(self):
        self.username = None
        self.password = None

    def login(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
        print(f"Logged in to Facebook with username: {self.username}")

    def post_message(self, message: str) -> None:
        print(f"Posted message on Facebook: {message}")
