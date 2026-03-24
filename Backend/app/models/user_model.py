from sqlalchemy import Integer,Column,String,DateTime
from datetime import datetime
from app.database import base

class User(base):
    __tablename__='users'

    id=Column(Integer,primary_key=True,index=True)
    username=Column(String(100),nullable=False)
    email=Column(String(150),nullable=False,index=True)
    password_hashed=Column(String(225),nullable=False)
    created_at=Column(DateTime,default=datetime.utcnow)
