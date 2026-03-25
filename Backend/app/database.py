from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from app.config import DB_URL

engine=create_engine(
    DB_URL,
    pool_pre_ping=True,
    connect_args={"sslmode":"require"}
    )

sessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)

base=declarative_base()