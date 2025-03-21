from sqlalchemy.orm import Session
from app.db.database import SessionLocal, Articles

# 🔹 Obtener una sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 🔹 Seleccionar todas las huellas de carbono
def get_articles_ecodes(db: Session):
    """Obtiene los últimos 25 artículos y los convierte en diccionarios serializables."""
    articles = db.query(Articles).order_by(Articles.created.desc()).limit(25).all()
    
    return [
        {
            "id": article.id,
            "title": article.title,
            "introtext": article.introtext,
            "fulltext": article.fulltext,
            "created": article.created.isoformat()  # Convertimos `datetime` a string ISO 8601
        }
        for article in articles
    ]

