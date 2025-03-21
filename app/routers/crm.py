from fastapi import APIRouter
from app.services.active_campaign import get_contacts, get_contact_by_email

router = APIRouter(prefix="/crm", tags=["CRM"])

@router.get("/contacts", response_model=dict)
def list_contacts():
    """Obtiene la lista de contactos desde ActiveCampaign."""
    return get_contacts()

@router.get("/contacts/{email}", response_model=dict)
def retrieve_contact(email: str):
    """Obtiene la información de un contacto por email."""
    return get_contact_by_email(email)