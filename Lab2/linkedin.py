from social_network import SocialNetwork

class LinkedIn(SocialNetwork):
    def __init__(self):
        self.email = None
        self.password = None

    def login(self, email: str, password: str) -> None:
        self.email = email
        self.password = password
        print(f"Logged in to LinkedIn with email: {self.email}")

    def post_message(self, message: str) -> None:
        print(f"Posted message on LinkedIn: {message}")
