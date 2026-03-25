from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.database import sessionLocal
from app.schemas.user_schema import UserCreate, UserLogin
from app.services.auth_service import (create_user,get_user_by_email,verify_password,create_access_token)

router=APIRouter()

def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/signup")
def signup(user:UserCreate,db:Session=Depends(get_db)):
    existing=get_user_by_email(db,user.email)
    if existing:
        raise HTTPException(status_code=400,detail="User Already Exist")
    User=create_user(db,user.username,user.email,user.password)

    return{
        "message":"User has been Created Successfully",
        "user":{
            "username":User.username,
            "email":User.email
        }
    }

@router.post("/login")
def login(user:UserLogin,db:Session=Depends(get_db)):
    db_user=get_user_by_email(db,user.email)

    if not db_user:
        raise HTTPException(status_code=401,detail="Invalid Credentials_username")
    
    if not verify_password(user.password,db_user.password_hashed):
        raise HTTPException(status_code=401,detail="Invalid Credentials_password")
    
    token=create_access_token({"sub":user.email})

    return{
        "access_token":token,
        "token_type":"bearer",
        "user":{
            "username":db_user.username,
            "email":db_user.email
        }
    }