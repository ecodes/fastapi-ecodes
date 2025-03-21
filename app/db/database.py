from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import mysql_settings

# 🔹 Crear la URL de conexión a MySQL
DATABASE_URL = f"mysql+pymysql://{mysql_settings.USER}:{mysql_settings.PASSWORD}@{mysql_settings.HOST}:{mysql_settings.PORT}/{mysql_settings.DATABASE}"

# 🔹 Configurar SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 🔹 Definir el modelo de la tabla `jos_content`
class Articles(Base):
    __tablename__ = "jos_content"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    introtext = Column(Text, nullable=True)
    fulltext = Column(Text, nullable=True)
    created = Column(DateTime, nullable=False)

# 🔹 Crear las tablas si no existen
def init_db():
    Base.metadata.create_all(bind=engine)
