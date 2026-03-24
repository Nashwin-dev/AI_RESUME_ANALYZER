from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import base,engine
from app.routes import auth_routes

app=FastAPI()

base.metadata.create_all(bind=engine)

app.include_router(auth_routes.router,prefix="/auth",tags=["Auth"])
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def root():
    return {"message":"Backend is Running Successfully"}