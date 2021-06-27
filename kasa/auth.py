"""Authentication class for KASA username / passwords."""
from hashlib import md5


class Auth:
    """Authentication for Kasa KLAP authentication."""

    def __init__(self, user: str = "", password: str = ""):
        self.user = user
        self.password = password

    def authenticator(self):
        """Return the KLAP authenticator for these credentials."""
        return self.md5auth()

    def owner(self):
        """Return the MD5 hash of the username in this object."""
        return self.md5user()

    def md5user(self):
        """Return md5 digest of user."""
        return md5(self.user.encode()).digest()

    def md5password(self):
        """Return MD5 digest of password."""
        return md5(self.password.encode()).digest()

    def md5auth(self):
        """Return MD5 digest of user and password combined."""
        return md5(self.md5user() + self.md5password()).digest()
