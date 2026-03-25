from sqlalchemy.orm import Session
from passlib.context import CryptContext
from datetime import datetime,timedelta
from jose import jwt 
from app.models.user_model import User
from app.config import ACCESS_TOKEN_EXPIRE_MINUTES,SECRETS_KEY,ALGORITHM

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str,hashed_password: str):
    return pwd_context.verify(plain_password,hashed_password)

def create_user(db: Session,username: str,email: str,password: str):
    hashed_password=hash_password(password)
    user=User(username=username,email=email,password_hashed=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_email(db:Session,email:str):
    return db.query(User).filter(User.email==email).first()

def create_access_token(data: dict):
    to_encode=data.copy()
    expire=datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    return jwt.encode(to_encode,SECRETS_KEY,algorithm=ALGORITHM)