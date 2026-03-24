import os
from dotenv import load_dotenv

load_dotenv()

SECRETS_KEY=os.getenv("SECRETS_KEY")
DB_URL=os.getenv("DATABASE_URL")
ALGORITHM=os.getenv("ALGORITHM","HS256")
ACCESS_TOKEN_EXPIRE_MINUTES=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES",60))