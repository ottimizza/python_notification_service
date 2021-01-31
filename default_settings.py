import binascii, os

# Application
SECRET_KEY = binascii.hexlify(os.urandom(24))

# Database
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# OAuth2 JWT Public Key
JWT_PUBLIC_KEY = os.getenv("JWT_PUBLIC_KEY", "")
