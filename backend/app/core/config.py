import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
JWT_SECRET = os.getenv("JWT_SECRET")
MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY")
