from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Define la base
Base = declarative_base()

# Aquí puedes agregar tu motor y sesión
DATABASE_URL = "mysql+mysqlconnector://root:@localhost/hospital_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
