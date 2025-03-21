import requests
from app.config import active_campaign 

# Definir encabezados de autenticación para ActiveCampaign
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Api-Token": active_campaign.API_KEY  # ✅ Ahora es más claro y escalable
}

def get_contacts() -> dict:
    """Obtiene la lista de contactos desde ActiveCampaign."""
    if not active_campaign.API_URL:
        raise ValueError("ACTIVE_CAMPAIGN_URL no está configurada.")
    
    try:
        response = requests.get(f"{active_campaign.API_URL}/contacts", headers=headers)
        response.raise_for_status()  # Lanza error si la respuesta no es 200
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Error en la solicitud: {str(e)}"}

def get_contact_by_email(email: str):
    """Obtiene la información de un contacto por email desde ActiveCampaign."""
    if not active_campaign.API_URL:
        raise ValueError("ACTIVE_CAMPAIGN_URL no está configurada.")
    
    url = f"{active_campaign.API_URL}/contacts?email={email}"  # 🔹 Filtro por email

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Error en la solicitud: {str(e)}"}