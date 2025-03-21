from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.ecodes import get_articles_ecodes, get_db

router = APIRouter(prefix="/ecodes", tags=["ECODES"])

@router.get("/articles_ecodes")
def list_articles_ecodes(db: Session = Depends(get_db)):
    """Obtiene los últimos 25 artículos de Ecodes."""
    return get_articles_ecodes(db)
