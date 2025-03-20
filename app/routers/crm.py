from fastapi import APIRouter
from app.services.active_campaign import get_contacts, create_contact

router = APIRouter(prefix="/crm", tags=["CRM"])

@router.get("/contacts")
def list_contacts():
    return get_contacts()

@router.post("/contacts")
def add_contact(email: str, first_name: str, last_name: str):
    return create_contact(email, first_name, last_name)
