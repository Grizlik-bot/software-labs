from facebook_factory import FacebookFactory
from linkedin_factory import LinkedInFactory

def main():
    facebook_factory = FacebookFactory()
    facebook_factory.post("facebook_user", "password123", "Hello, Facebook!")

    linkedin_factory = LinkedInFactory()
    linkedin_factory.post("user@example.com", "password456", "Hello, LinkedIn!")

if __name__ == "__main__":
    main()
